===============================================================================
Distributed Array Protocol v1.0.0
===============================================================================

.. Contents::

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

Some usecases supported by v1.0 of the protocol include:

* Block, cyclic, and block-cyclic distributions for structured decomposition.

* Padded block-distributed arrays, including boundary cells for physical
  boundary conditions, and communication buffers for storing and updating
  values in finite-differencing applications.

* Unstructured distributions for arbitrary mappings between global indices and
  local data.

* Multi-dimensional arrays.

* Different distributions for each array dimension.

* Dense and sparse (or structured and unstructured) arrays.

* Compatibility with array views and slices.


Sources
-------------------------------------------------------------------------------

The primary sources and inspiration for the DAP are:

* Trilinos [#trilinos]_ and PyTrilinos [#pytrilinos]_

* Global Arrays [#globalarrays]_ and Global Arrays in NumPy (GAiN) [#gain]_

* The Chapel [#chapel]_, X10 [#x10]_, and HP-Fortran [#hpfortran]_ languages

* Distributed array implementation in the Julia [#julia]_ language

* NumPy [#numpy]_ and the Revised Buffer Protocol [#bufferprotocol]_


Definitions
-----------

process
    A "process" is the basic unit of execution and is as defined in MPI
    [#mpi]_.  It is also analogous to an IPython.parallel [#ipythonparallel]_
    engine.  Each process has an address space, has one or more namespaces that
    contain objects, and is able to communicate with other processes to send
    and receive data.

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
    boundaries and correspond to the cells or indices that are involved with
    the physical system's boundary conditions in a PDE application, for
    example.  These boundary padding cells would exist even if the array were
    not distributed. 
    
communication padding
    Padding indices that are shared logically with a neighboring local array.
    These padding regions are used often in finite differencing applications
    and reserve room for communication with neighboring arrays when data
    updates are required.


Exporting a Distributed Array
-----------------------------

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
distributed array, with the zeroth dictionary associated with the zeroth
dimension of the array, and so on for each dimension in succession. There is
one dimension dictionary per dimension, **whether or not that dimension is
distributed**.  These dictionaries are intended to include all metadata
required to fully specify a distributed array's distribution information.


Dimension Dictionaries
----------------------

All dimension dictionaries shall have a ``'dist_type'`` key with a value of
type string or `None`.  The dist_type of a dimension specifies the kind of
distribution for this dimension, or no distribution for value `None`.

The following dist_types are currently supported:

============= ========== ===============
  name         dist_type   required keys
============= ========== ===============
undistributed     None    'dist_type', 'data_size'
block             'b'     common, 'start', 'stop'
cyclic            'c'     common, 'start'
block-cyclic      'bc'    common, 'start', 'block_size'
block-padded      'bp'    common, 'start', 'stop', 'padding'
unstructured      'u'     common, 'indices'
============= ========== ===============

where "common" represents the keys common to all distributed dist_types:
``'dist_type'``, ``'data_size'``, ``'proc_grid_size'``, and
``'proc_grid_rank'``.

Other dist_types may be added in future versions of the protocol.

Required key-value pairs
````````````````````````

All dimension dictionaries (regardless of distribution type) must define the
following key-value pairs:

* ``'dist_type'`` : ``{None, 'b', 'c', 'bc', 'bp', 'u'}``

  The distribution type; the primary way to determine the kind of distribution
  for this dimension.

* ``'data_size'`` : ``int``

  Total number of global array elements along this dimension.

All *distributed* dimensions shall have the following keys in their dimension
dictionary, with the associated value:

* ``'proc_grid_size'`` : ``int``, > 1

  The total number of processes in the process grid in this dimension.
  Necessary for computing the global / local index mapping, etc.

  [TODO: to confirm: always greater than 1, never equal to 1?  Otherwise this
  dimension is not distributed and we get into degeneracy between distributed /
  undistributed dimensions that would be cleaner to avoid.]

  Constraint: the product of all proc_grid_sizes for all distributed dimensions
  shall equal the total number of processes in the communicator.

* ``proc_grid_rank`` : ``int``

  The rank of the process for this dimension in the process grid.  This
  information allows the consumer to determine where the neighbor sections of
  an array are located.

  [TODO: Question regarding Cart_create, grid_rank, grid_size, etc:

  What guarantees are there between libraries?  When importing from the
  protocol, importer sees ``proc_grid_rank``, ``proc_grid_size`` for each
  dimension.  If we do an ``MPI_Cart_create`` with ``reorder=False``, what
  guarantees are there to ensure that the MPI cartesian communicator is
  consistent with the communicator on the exporting side of the protocol?]

Optional key-value pairs
````````````````````````

* ``'periodic'`` : ``bool``

  Indicates whether this dimension is periodic.  When not present, indicates
  this dimension is not periodic, equivalent to a value of `False`.

Distribution-type specific key-value pairs
``````````````````````````````````````````

The remaining key-value pairs in each dimension dictionary depend on the
``dist_type`` and are described below:

* undistributed (``dist_type`` is ``None``):

  No additional keys required.

* block (``dist_type`` is ``'b'``):

  * ``start`` : ``int``, >= 0

    The start index (inclusive and 0-based) of the global index space available
    on this process.

  * ``stop`` : ``int``, > ``start`` value

    The stop index (exclusive, as in standard Python indexing) of the global
    index space available on this process.

  For a block-distributed dimension, adjacent processes as determined by the
  dimension dictionary's ``proc_grid_rank`` field shall have adjacent global
  index ranges, i.e., for two processes ``a`` and ``b`` with grid ranks ``i``
  and ``i+1`` respectively, the ``stop`` of ``a`` shall be equal to the
  ``start`` of ``b``.  Processes may contain differently-sized global index
  ranges.

* cyclic (``dist_type`` is ``'c'``):

  * ``start`` : ``int``, >= 0

    The start index (inclusive and 0-based) of the global index space available
    on this process.

    The cyclic distribution is what results from assigning global indices to
    the processes in a distributed dimension in round-robin fashion.  A
    constraint for cyclic is that the Python slice formed from the ``start``,
    ``data_size``, and ``proc_grid_size`` values reproduces the local array's
    indices as in standard NumPy slicing.

* block-cyclic (``dist_type`` is ``'bc'``):

  * ``start`` : ``int``, >= 0

    The start index (inclusive and 0-based) of the global index space available
    on this process.

  * ``block_size`` : ``int``, >= 1

    Indicates the size of the contiguous blocks for this dimension.

    [TODO: what are the bounds on block_size?]

    Block-cyclic can be thought of as analogous to the cyclic distribution, but
    it distributes contiguous blocks of global indices in round robin fashion
    rather than single indices.  In this way block-cyclic is a generalization
    of the block and cyclic distribution types (for an evenly distributed block
    distribution).  When block_size == 1, block-cyclic is equivalent to cyclic;
    when block_size == data_size // proc_grid_size, block cyclic is equivalent
    to block.

    [TODO: write down equations relating start, stop, step, block_size,
    proc_grid_size and proc_grid_rank that yield the global indices under block
    cyclic.  Resolve any ambiguites for ugly combinations of proc_grid_size,
    block_size, step, particularly when "extra" elements are involved.]

* block-padded (``dist_type`` is ``'bp'``)

  Analogous to the block distribution type but with an extra ``padding`` key.
  This distribution type allows adjacent local array sections to overlap in
  global index space.  Whenever an element of the ``padding`` tuple is > 0,
  that indicates this array shares indices with its neighbor (as determined by
  ``proc_grid_rank``), and further, that this neighboring process owns the
  data.

  * ``start`` and ``stop`` as in the block distribution type

  * ``padding`` : 2-tuple of ``int``, each >= 0.

    Indicates the number of "padding" values at the lower and upper limits
    (respectively) of the indices available on this process.  This padding can
    be either "boundary padding" or "communication padding".

* unstructured (``dist_type`` is ``'u'``):

  * ``indices``: list of ``int``

    Global indices available on this process.

  [TODO: fill in details, constraints.]


Examples
-------------------------------------------------------------------------------

Block, Undistributed
````````````````````

Assume we have a process grid with 2 rows and 1 column, and we have a 2x10
array ``a`` distributed over it.  Let ``a`` be a two-dimensional array with a
block-distributed 0th dimension and an undistributed 1st dimension.

In process 0:

.. code:: python

    >>> distbuffer = a0.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '1.0.0'
    >>> distbuffer['buffer']
    array([ 0.2,  0.6,  0.9,  0.6,  0.8,  0.4,  0.2,  0.2,  0.3,  0.5])
    >>> distbuffer['dim_data']
    ({'data_size': 2,
      'dist_type': 'b',
      'proc_grid_rank': 0,
      'proc_grid_size': 2,
      'start': 0,
      'stop': 1},
     {'data_size': 10,
      'dist_type': None})

In process 1:

.. code:: python

    >>> distbuffer = a1.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '1.0.0'
    >>> distbuffer['buffer']
    array([ 0.9,  0.2,  1. ,  0.4,  0.5,  0. ,  0.6,  0.8,  0.6,  1. ])
    >>> distbuffer['dim_data']
    ({'data_size': 2,
      'dist_type': 'b',
      'proc_grid_rank': 1,
      'proc_grid_size': 2,
      'start': 1,
      'stop': 2},
     {'data_size': 10,
      'dist_type': None})

Unstructured
````````````

Assume we have a process grid with 3 rows, and we have a size 30 array ``a``
distributed over it.  Let ``a`` be a one-dimensional unstructured array with 7
elements on process 0, 3 elements on process 1, and 20 elements on process 2.


On all processes:

.. code:: python

    >>> distbuffer = local_array.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '1.0.0'
    >>> len(distbuffer['dim_data']) == 1  # one dimension only
    True

In process 0:

.. code:: python

    >>> distbuffer['buffer']
    array([0.7,  0.5,  0.9,  0.2,  0.7,  0.0,  0.5])
    >>> distbuffer['dim_data']
    ({'data_size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 0,
      'proc_grid_size': 3,
      'indices': [19, 1, 0, 12, 2, 15, 4]},)

In process 1:

.. code:: python

    >>> distbuffer['buffer']
    array([0.1,  0.5,  0.9])
    >>> distbuffer['dim_data']
    ({'data_size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 1,
      'proc_grid_size': 3,
      'indices': [6, 13, 3]},)

In process 2:

.. code:: python

    >>> distbuffer['buffer']
    array([ 0.1,  0.8,  0.4,  0.8,  0.2,  0.4,  0.4,  0.3,  0.5,  0.7,
            0.4,  0.7,  0.6,  0.2,  0.8,  0.5,  0.3,  0.8,  0.4,  0.2])
    >>> distbuffer['dim_data']
    ({'data_size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 2,
      'proc_grid_size': 3,
      'indices': [10, 25,  5, 21,  7, 18, 11, 26, 29, 24, 23, 28, 14,
                  20,  9, 16, 27,  8, 17, 22]},)


References
-------------------------------------------------------------------------------
.. [#mpi] Message Passing Interface.  http://www.open-mpi.org/
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


.. vim:spell:ft=rst:tw=79
