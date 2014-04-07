===============================================================================
Distributed Array Protocol
===============================================================================

Overview
-------------------------------------------------------------------------------

The Distributed Array Protocol (DAP) is a process-local protocol that allows
two subscribers, called the "producer" and the "consumer" or the "exporter" and
the "importer", to communicate the essential data and metadata necessary to
share a distributed-memory array between them.  This allows two independently
developed components to access, modify, and update a distributed array without
copying.  The protocol formalizes the metadata and buffers involved in the
transfer, allowing several distributed array projects to collaborate,
facilitating interoperability.  By not copying the underlying array data, the
protocol allows for efficient sharing of array data.

The DAP is intended to build on the concepts and implementation of the existing
PEP-3118 buffer protocol [#bufferprotocol]_, and uses PEP-3118 buffers (and
subscribing Python objects such as memoryviews and NumPy arrays) as components.

This version of the DAP is defined for the Python language.  Future versions of
this protocol may provide definitions in other languages.


Usecases
-------------------------------------------------------------------------------

Major usecases supported by the protocol include:

* Sharing large amounts of array data without copying.

* Block, cyclic, and block-cyclic distributions for structured arrays.

* Padded block-distributed arrays for finite differencing applications.

* Unstructured distributions for arbitrary mappings between global indices and
  local data.

* Multi-dimensional arrays.

* Different distributions for each array dimension.

* Dense (structured) and sparse (unstructured) arrays.

* Compatibility with array views and slices.


Sources
-------------------------------------------------------------------------------

The primary sources and inspiration for the DAP are:

* NumPy [#numpy]_ and the Revised Buffer Protocol [#bufferprotocol]_

* Trilinos [#trilinos]_ and PyTrilinos [#pytrilinos]_

* Global Arrays [#globalarrays]_ and Global Arrays in NumPy (GAiN) [#gain]_

* The Chapel [#chapel]_, X10 [#x10]_, and HP-Fortran [#hpfortran]_ languages

* Distributed array implementation in the Julia [#julia]_ language


Definitions
-------------------------------------------------------------------------------

process
    A **process** is the basic unit of execution and is equivalent to a
    conventional OS process.  Each process has an address space, has one or
    more namespaces that contain objects, and is able to communicate with other
    processes to send and receive data.  Note that the protocol does not
    require any inter-process communication and makes no assumptions regarding
    communication libraries.

process rank
    An integer label that uniquely identifies a process.  Ranks are assigned
    contiguously from the range ``0 ... N-1`` for ``N`` processes.

process grid
    The **process grid** is an N-dimensional Cartesian grid.  Each coordinate
    uniquely identifies a process, and the process grid maps process ranks to
    grid coordinates.  Process ranks are assigned to their corresponding grid
    coordinate in "C-order", i.e., the last index varies fastest when iterating
    through coordinates in rank order.  The product of the number of processes
    in each dimension in the process grid shall be equal to the total number of
    processes.

    For example, for an ``N`` by ``M`` process grid over ``N * M`` processes
    with ranks ``0, 1, ..., (N*M)-1``, process grid coordinate ``(i,j)``
    corresponds to the process with rank ``i*M + j``.

    (Note that the protocol's process grid is compatible with MPI's
    ``MPI_Cart_create()`` command, and the MPI standard guarantees that
    Cartesian process coordinates are always assigned to ranks in the same way
    and are "C-order" by default [#mpivirtualtopologies]_.  The protocol makes
    no assumption about which underlying communication library is being used,
    nor does it require subscribing packages to implement a communication
    layer.)

distributed array
    A single logical array of arbitrary dimensionality that is divided among
    multiple processes.

    A distributed array has both a global and a local index space for each
    dimension, and a mapping between the two index spaces.

local index
    A local index specifies a location in an array's data at the process level.

global index
    A global index specifies a location in the array's data as if the array
    were not distributed.

map
    A map object provides two functionalities: the first is the ability to
    translate a global index into a process identifier and a local index on
    that process; the second is the ability to provide the global index that
    corresponds to a given local index.

boundary padding
    Padding indices in a local array that indicate which indices are part of
    the logical *boundary* of the entire domain.  These are physical or real
    boundaries and correspond to the elements or indices that are involved with
    the physical system's boundary conditions in a PDE application, for
    example.  These elements are included in a distributed dimension's
    ``'size'``.

communication padding
    Padding indices that are shared logically with a neighboring local array.
    These padding regions are used often in finite differencing applications
    and reserve room for communication with neighboring arrays when data
    updates are required.  Each of these shared elements are only counted once
    toward the ``'size'`` of each distributed dimension, so the total
    ``'size'`` of a dimension will less than or equal to the sum of the sizes
    all local buffers.


Exporting a Distributed Array
-------------------------------------------------------------------------------

A "producer" object that subscribes to the DAP shall provide a method named
``__distarray__`` that, when called by a consumer, returns a dictionary with
three keys: ``'__version__'``, ``'buffer'``, and ``'dim_data'``.

The value associated with the ``'__version__'`` key shall be a string of the
form ``'major.minor.patch'``, as described in the Semantic Versioning
specification [#semver]_ and PEP-440 [#pep440]_.  As specified in Semantic
Versioning, versions of the protocol that differ in the minor version number
shall be backwards compatible; versions that differ in the major version number
may break backwards compatibility.

The value associated with the ``'buffer'`` key shall be a Python object that is
compatible with the PEP-3118 buffer protocol and contains the data for a local
section of a distributed array.

The value for the ``'dim_data'`` key shall be a tuple of dictionaries, called
"dimension dictionaries", containing one dictionary for each dimension of the
distributed array.  The zeroth dictionary in ``dim_data`` shall describe the
zeroth dimension of the array, the first dictionary shall describe the first
dimension, and so on for each dimension in succession.
These dictionaries include all metadata
required to specify a distributed array's distribution.  The ``dim_data`` tuple
may be empty, indicating a zero-dimensional array.  The number of elements in
the ``'dim_data'`` tuple must match the number of dimensions of the associated
buffer object.


Dimension Dictionaries
-------------------------------------------------------------------------------

All dimension dictionaries shall have a ``'dist_type'`` key with a value of
type string.  The ``dist_type`` of a dimension specifies the kind of
distribution for that dimension.

The following dist_types are currently supported:

=============== =========== ========================== =======================
  name           dist_type   required keys              optional keys
=============== =========== ========================== =======================
block               'b'       common, 'start', 'stop'   'padding', 'periodic'
cyclic              'c'       common, 'start'           'block_size'
unstructured        'u'       common, 'indices'         'one_to_one'
=============== =========== ========================== =======================

where "common" represents the keys common to all dist_types: ``'dist_type'``,
``'size'``, ``'proc_grid_size'``, and ``'proc_grid_rank'``.

Other ``dist_type``\s may be added in future versions of the protocol.

Required key-value pairs
````````````````````````

All dimension dictionaries (regardless of distribution type) must define the
following key-value pairs:

* ``'dist_type'`` : ``{'b', 'c', 'u'}``

  The distribution type; the primary way to determine the kind of distribution
  for this dimension.

* ``'size'`` : ``int``, greater than or equal to 0

  Total number of global array elements along this dimension.

  Indices considered "communication padding" *are not* counted towards this
  value; indices considered "boundary padding" *are* counted towards this
  value.  More explicitly, to calculate the ``size`` along a particular
  dimension, one can sum the result of the function ``num_owned_indices`` (in
  the provided ``utils.py`` or in this document's appendix) run on the
  appropriate dimension dictionary on every process.

* ``'proc_grid_size'`` : ``int``, greater than or equal to 1

  The total number of processes in the process grid in this dimension.
  Necessary for computing the global / local index mapping, etc.

  Constraint: the product of all ``'proc_grid_size'``\s for all dimensions
  shall equal the total number of processes.

* ``'proc_grid_rank'`` : ``int``, greater than or equal to 0, less than
  ``'proc_grid_size'``

  The rank of the process for this dimension in the process grid.  This
  information allows the consumer to determine where the neighbor sections of
  an array are located.

  The mapping of process rank to process grid coordinates is assumed to be row
  major.  For an ``N`` by ``M`` process grid over ``N * M`` processes with
  ranks ``0, 1, ..., (N*M)-1``, process grid coordinate ``(i,j)`` corresponds
  to the process with rank ``i*M + j``.  This generalizes in the conventional
  row-major way.


Distribution-type specific key-value pairs
``````````````````````````````````````````

The remaining key-value pairs in each dimension dictionary depend on the
``dist_type`` and are described below.

block (``dist_type`` is ``'b'``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``start`` : ``int``, greater than or equal to zero.

  The start index (inclusive and 0-based) of the global index space available
  on this process.

* ``stop`` : ``int``, greater than the ``start`` value, less than or equal to
  the ``size`` value.

  The stop index (exclusive, as in standard Python indexing) of the global
  index space available on this process.

  For a block-distributed dimension without communication padding, adjacent
  processes as determined by the dimension dictionary's ``proc_grid_rank``
  field shall have adjacent global index ranges. More explicitly, for two
  processes ``a`` and ``b`` with grid ranks ``i`` and ``i+1`` respectively, the
  ``stop`` of ``a`` shall be equal the ``start`` of ``b``.  With communication
  padding present, the stop of ``a`` may be greater than the ``start`` of
  ``b``.

  Processes may contain differently-sized global index ranges; this is
  sometimes called an "irregular block distribution".

  For every block-distributed dimension ``i``, ``stop - start`` must be equal
  to ``buffer.shape[i]``.

* ``padding`` : 2-tuple of ``int``, each greater than or equal to zero.
  Optional.

  If communication padding, must be less than or equal to the number of indices
  owned by the neighboring process.

  The padding tuple describes the width of the padding region at the beginning
  and end of a buffer in a particular dimension.  Padding represents extra
  allocation for an array, but padding values are in some sense not "owned" by
  the local array and are reserved for other purposes.

  For the dimension dictionary with ``proc_grid_rank == 0``, the first element
  in ``padding`` is the width of the boundary padding; this is extra allocation
  reserved for boundary logic in applications that need it.  For the dimension
  dictionary with ``proc_grid_rank == proc_grid_size-1``, the second element in
  ``padding`` is the width of the boundary padding. All other ``padding`` tuple
  values are for communication padding and represent extra allocation reserved
  for communication between processes. Every communication padding width must
  equal its counterpart on its neighboring process; more specifically, the
  "right" communication padding on rank ``i`` in a 1D grid must equal the
  "left" communication padding on rank ``i+1``.

  For example, consider a one-dimensional block-distributed array distributed
  over four processes.  Let its left boundary padding width be 4, its right
  boundary padding width be 0 and its communication padding widths be (1,) (1,
  2), (2, 3), and (3,). The padding tuple for the local array on each rank
  would be:

  ============== ====== ====== ====== ======
  proc_grid_rank  0      1      2      3
  ============== ====== ====== ====== ======
  padding        (4, 1) (1, 2) (2, 3) (3, 0)
  ============== ====== ====== ====== ======

  If the value associated with ``padding`` is the tuple ``(0,0)`` (the
  default), this indicates the local array is not padded in this dimension.

* ``periodic`` : ``bool``, optional

  Indicates whether this dimension is periodic.  When not present, indicates
  this dimension is not periodic, equivalent to a value of ``False``.

cyclic (``dist_type`` is ``'c'``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``start`` : ``int``, greater than or equal to zero.

  The start index (inclusive, 0-based) of the global index space available on
  this process.

  The cyclic distribution is what results from assigning global indices--or
  contiguous blocks of indices, in the case when ``block_size`` is greater than
  one--to processes in round-robin fashion.  When ``block_size`` equals one, a
  Python slice formed from the ``start``, ``size``, and ``proc_grid_size``
  values selects the global indices that are owned by this local array.

* ``block_size`` : ``int``, greater than or equal to one. Optional.

  Indicates the size of contiguous blocks of indices for this dimension.  If
  absent, equivalent to the case when ``block_size`` is present and equal to
  one.

  If ``block_size == 1`` (the default), this specifies the "true" cyclic
  distribution as described in the ScaLAPACK documentation [#bcnetlib]_.  If
  ``block_size == ceil(size / proc_grid_size)``, this distribution is
  equivalent to an evenly-distributed block distribution.  If ``1 < block_size
  < size // proc_grid_size``, then this specifies a distribution sometimes
  called "block-cyclic" [#bcnetlib]_ [#bcibm]_.

  Block-cyclic is a generalization of (evenly-distributed) block and cyclic
  distribution types.  It can be thought of as as a cyclic distribution with
  contiguous blocks of global indices (rather than single indices) distributed
  in a round robin fashion.

  Note that since this protocol allows for block-distributed dimensions with
  irregular numbers of indices on each process, not all 'block'-distributed
  dimensions describable by this protocol can be represented as 'cyclic' with
  the 'block-size' key.

unstructured (``dist_type`` is ``'u'``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``indices``: buffer (or buffer-compatible) of ``int``

  Global indices available on this process.

  The only constraint that applies to the ``indices`` buffer is that the values
  are locally unique.  The indices values are otherwise unconstrained: they can
  be negative, unordered, and non-contiguous.

* ``one_to_one`` : bool, optional.

  If not present, shall be equivalent to being present with a ``False`` value.

  If ``False``, indicates that some global indices may be duplicated in two or
  more local ``indices`` buffers.

  If ``True``, a global index shall be located in exactly one local ``indices``
  buffer.


Dimension dictionary aliases
````````````````````````````

The following aliases are provided for convenience.  Only one is provided in
the current version of this protocol, but more may be added in future versions.

Empty dimension dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~

An empty dimension dictionary in dimension ``i``, will be interpreted as the
following:

.. code:: python

    {'dist_type': 'b',
     'proc_grid_rank': 0,
     'proc_grid_size': 1,
     'start': 0,
     'stop': buf.shape[i],
     'size': buf.shape[i]}

Where ``buf`` is the associated buffer object.

This is intended to be a shortcut for defining undistributed dimensions.


General comments
````````````````

Empty local buffers
~~~~~~~~~~~~~~~~~~~

It shall be possible for one or more local array sections to contain no data.
This is supported by the protocol and is not an invalid state.  These
situations may arise explicitly or when downsampling or slicing a distributed
array.

The following properties of a dimension dictionary imply an empty local buffer:

* With any ``dist_type``: ``size == 0``
* With the ``'b'`` or ``'c'`` ``dist_type``:  ``start == size``
* With the ``'b'`` ``dist_type``: ``start == stop``
* With the ``'u'`` ``dist_type``: ``len(indices) == 0``

Undistributed dimensions
~~~~~~~~~~~~~~~~~~~~~~~~

A dimension with ``proc_grid_size == 1`` is essentially undistributed; it is
"distributed" over a single process.  Block-distributed dimensions with
``proc_grid_size == 1`` and with the ``periodic`` and ``padding`` keys present
are valid.  The ``periodic == True`` and ``padding`` values indicate this array
is periodic on one processor, with associated padding regions.

Global array size
~~~~~~~~~~~~~~~~~

The global number of elements in an array is the product of the ``size``\s of
the dimension dictionaries, or 1 if the ``dim_data`` sequence is empty.  In
Python syntax, this would be ``reduce(operator.mul, global_shape, 1)`` where
``global_shape`` is a Python sequence of integers such that ``global_shape[i]``
is the ``size`` of the dimension dictionary for dimension ``i``.  If
``global_shape`` is an empty sequence, the result of the reduction above is
``1``, indicating the distributed array is a zero-dimensional scalar.

Identical ``dim_data`` along an axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If ``dim_data`` is the tuple of dimension dictionaries for a process and ``rank
= dim_data[i]['proc_grid_rank']`` for some dimension ``i``, then all processes
with the same ``rank`` for dimension ``i`` must have the same values for other
keys in their respective dimension dictionaries.  Essentially, this says that
dimension dictionary ``dim_data[i]`` is identical for all processes that have
the same value for ``dim_data[i]['proc_grid_rank']``.  The only possible
exception to this is the ``padding`` tuple, which may have different values on
edge processes due to boundary padding.


References
-------------------------------------------------------------------------------
.. [#mpi] Message Passing Interface.  http://www.open-mpi.org/
.. [#mpivirtualtopologies] MPI-2.2 Standard: Virtual Topologies.
                           http://www.mpi-forum.org/docs/mpi-2.2/mpi22-report/node165.htm#Node165
.. [#ipythonparallel] IPython Parallel.
                      http://ipython.org/ipython-doc/dev/parallel/
.. [#bufferprotocol] Revising the Buffer Protocol.
                     http://www.python.org/dev/peps/pep-3118/
.. [#semver] Semantic Versioning 2.0.0.  http://semver.org/
.. [#pep440] PEP 440: Version Identification and Dependency
             Specification.  http://www.python.org/dev/peps/pep-0440/
.. [#trilinos] Trilinos. http://trilinos.sandia.gov/
.. [#pytrilinos] PyTrilinos.
                 http://trilinos.sandia.gov/packages/pytrilinos/
.. [#globalarrays] Global Arrays. http://hpc.pnl.gov/globalarrays/
.. [#gain] Global Arrays in NumPy.
           http://www.pnnl.gov/science/highlights/highlight.asp?id=1043
.. [#chapel] Chapel. http://chapel.cray.com/
.. [#x10] X10. http://x10-lang.org/
.. [#hpfortran] High Perfomance Fortran. http://dacnet.rice.edu/
.. [#julia] Julia. http://docs.julialang.org
.. [#numpy] NumPy. http://www.numpy.org/
.. [#bcnetlib] ScaLAPACK Users' Guide: The Two-dimensional Block-Cyclic Distribution.
               http://netlib.org/scalapack/slug/node75.html
.. [#bcibm] Parallel ESSL Guide and Reference: Block-Cyclic Distribution over Two-Dimensional Process Grids.
            http://publib.boulder.ibm.com/infocenter/clresctr/vxrx/index.jsp?topic=%2Fcom.ibm.cluster.pessl.v4r2.pssl100.doc%2Fam6gr_dvtdpg.htm


.. vim:spell:ft=rst:tw=79
