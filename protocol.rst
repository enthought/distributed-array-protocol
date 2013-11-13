==============================================================================
Distributed Array Protocol -- v0.0.1
==============================================================================

Goal
-------------------------------------------------------------------------------

To define the core data structures and API for the protocol such that it can be
implemented by a subscribing library.

Overview
-------------------------------------------------------------------------------

Usecases
-------------------------------------------------------------------------------

The principal usecases supported by v1.0 of the protocol are as follows:

    * Block, cyclic, block cyclic distributions for structured decomposition

    * Block distribution can be padded to allow for ghosts (boundary cells for
      boundary conditions -- part of the physical problem) and halos
      (communication buffers for storing and updating values in finite
      differencing applications).

    * Unstructured decomposition -- arbitrary map between local data and
      global indexes.

    * Each dimension can have a different distribution


Supported usecases include:

    * Multiple dimensions

    * Structured and unstructured distributions.

    * Dense and sparse 

    * Ghost vectors / halos

    * Should work with array views and slices.


Sources
-------------------------------------------------------------------------------

The primary sources and inspiration for the DAP are:

  * Trilinos distributed data structures

  * Global Arrays / Global Arrays in NumPy 

  * The Chapel, X10, HP-Fortran languages

  * Distributed array implementation in the Julia language


Components
-------------------------------------------------------------------------------

Based on the discussions at SciPy 2013, what follows is an outline of the
essential components of the DAP:

  *  WFS and KWS are in agreement that the DAP should build on the existing
    PEP-3118 buffer protocol, as it is supported in Python, NumPy and Cython.

   * Trilinos Tpetra distributed Vectors are the fundamental distributed data
     structure in Trilinos.  A Vector has three components: an Array to store
     the local data, a Map, and a communicator.  A Vector's local data is
     contained in a contiguous Teuchos::Array.  A Vector's Tpetra::Map is
     responsible for converting local indices to and from global indices.  A
     Vector's Teuchos::Comm communicator is analogous to an MPI communicator
     which encapsulates all distributed communication, etc.

  * The essential components of the DAP, then, are the local data buffers,
    which are compatible with PEP-3118 buffers, and the index mapping
    infrastructure, which describes the data distribution.

  * The Map provides two functions / methods::

        ordinal_t get_gid(ordinal_t lid) -> returns the global ID / index given a local ID / index.

        (process_id, ordinal_t) get_lid(ordinal_t gid) -> returns the (process rank, local index on that process) tuple / structure given a global index.

  * To generalize this to multi-dimensional arrays, the global index and local
    index are generalized into tuples of indices into each dimension.  The
    local data buffer is generalized into a multi-dimensional buffer.

  * Trilinos supports one-to-many global-to-local index mappings to allow for
    ghost vectors in finite-differencing applications.  This brings in the
    concept of "ownership" of a distributed array index: every distributed
    array index is owned by a specific process, and that process is
    responsible for performing calculations on that location.  Non-owning
    processes that share that index can be updated with the data from the
    owned index.

Distributed Array Protocol v1.0
-------------------------------------------------------------------------------

Definitions:

  * Process: a "process" is the basic unit of execution and is as defined in
    MPI.  Analogous with an IPython.parallel engine.  Each process has an
    address space, one or more namespaces that contain objects, and is able to
    communicate with other processes to send and receive data.

  * A distributed array is a single logical array, of arbitrary
    dimensionality, that is divided among multiple processes.  

  * A distributed array has both a global and a local index space for each
    dimension, and a mapping between the two index spaces.  A local index
    specifies a location in the array's data at the process level.  A global
    index specifies a location in the array's data as if the array were not
    distributed.  The map object provides two functionalities: the first is
    the ability to translate a global index into a process identifier and a
    local index on that process; the second takes a local index and provides
    the global index that corresponds to that local index.

The DAP is a process-local protocol and allows two subscribers, called the
"producer" and the "consumer" or the "exporter" and the "importer", to
communicate the essential data and metadata necessary to share a distributed
array between them.  This allows two independently developed components to
access, modify, and update a distributed array without copying.

The DAP is intended to build on the concepts and implementation of the
existing PEP-3118 buffer protocol, and uses PEP-3118 buffers (and subscribing
Python objects, such as memoryviews and NumPy arrays) as components.

This version of the DAP is defined for the Python language.  Future versions
of this protocol may provide definitions in other languages.

A "producer object" that subscribes to the DAP shall provide a method named
"__distarray__" that, when called by a consumer, returns a dictionary with
three keys, "buffer", "dimdata", and "__version__".

The value associated with the "__version__" key shall be a tuple of two or
more integers, and this tuple shall be a conventional version tuple, with the
first integer specifying the major version, the next integer the minor
version, etc.  Versions of the protocol that differ in the minor version
number shall be backwards compatible; versions that differ in the major
version number may break backwards compatibility.

The value associated with the "buffer" key shall be a Python object that is
compatible with the PEP-3118 buffer protocol and contains the data for a local
section of a distributed array.

The value for the "dimdata" key shall be a tuple of dictionaries, called
"dimension dictionaries", one dictionary for each dimension of the distributed
array, with the zeroth dictionary associated with the zeroth dimension of the
array, etc.  These dictionaries are intended to include all metadata required
to fully specify the array.  There is one dimension dictionary per dimension,
**whether or not that dimension is distributed**.

The primary key-value pair that all dimension dictionaries shall have
specifies the type of distribution for this dimension.  The key is the string
"disttype" and the value is of type string.  The following disttypes are
currently supported: undistributed, block, cyclic, block cyclic, block padded,
and unstructured.  Other disttypes may be added in future versions of the
protocol.

All dimension dictionaries (regardless of distribution type) define the
following key-value pairs:

  * 'disttype' : string or None.

    The distribution type, the primary way to determine the kind of
    distribution for this dimension.

  * 'periodic' : bool

    Indicates whether this dimension is periodic.

  * 'datasize' : integer

    Total number of logical array elements along this dimension.

All distributed dimensions shall have the following keys in the dictionary,
with the associated value described:

   * 'gridsize' : integer, greater than 1.
 
     The total number of processes in the process grid in this dimension.
     Necessary for computing the global / local index mapping, etc.

     [TODO: to confirm: always greater than 1?  Otherwise this dimension is
     not distributed and we get into degeneracy between distributed /
     undistributed dimensions that would be cleaner to avoid.]

     Constraint: the product of all gridsizes for all distributed dimensions
     shall equal the total number of processes in the communicator.

   * 'gridrank' : integer
 
     The rank of this process for this dimension in the process grid.  This
     information allows the consumer to determine where the neighbor sections
     of an array are located.

     [TODO: To be resolved:
        Question regarding Cart_create, grid_rank, grid_size, etc:
            What guarantees are there between libraries?  When importing from
            the protocol, importer sees grid_rank, grid_size for each
            dimension.  If we do an MPI_Cart_create with reorder=False, what
            guarantees are there to ensure that the MPI cartesian communicator
            is consistent with the communicator on the exporting side of the
            protocol?
     ]

The remaining key-value pairs in each dimension dictionary depends on the dist
type, and are described below:

    * Undistributed, dist type None.

      This is here for consistency's sake.

    * block, dist type of "b":

        * 'start' : integer >= 0.

        The start index (inclusive and 0-based) of the global index space for
        this array.

        * 'stop' : integer, > 'start' value.

        The stop index (exclusive, as in standard Python indexing) of the
        global index space for this array.

        * 'step' : integer, >= 1.

        [TODO: in what circumstances can step be non unitary?  Should this be
        supported?  If 'step' is always 1 for block, then it should not be
        included as a key.]

        For a block distributed dimension, adjacent processes as determined by
        the dimension dictionary's 'gridrank' field shall have adjacent global
        index ranges, i.e., for two processes `a` and `b` with grid ranks `i`
        and `i+1`, resp., the 'stop' of `a` shall be equal to the 'start' of
        `b`.

    * cyclic, dist type of "c":

        * 'start' : integer, >= 0.

        The start index (inclusive and 0-based) of the global index space.

        * 'stop' : integer, > 'start' value.

        The stop index (exclusive, as in standard Python indexing) of the
        global index space.

        * 'step' : integer, equal to the 'gridsize' value.

        [TODO: 'step' is not strictly necessary; should this k/v pair be part
        of the protocol for cyclic?  THere are more constraints on the 'step'
        value, need to be specified.]

        The cyclic distribution is what results from assigning global indices
        to the processes in a distributed dimension in round-robin fashion.  A
        constraint for cyclic is that the Python slice formed from the start,
        stop, and step values reproduces the local array's indices as in
        standard NumPy slicing.

    * block cyclic, dist type of "bc":

        * 'start' : integer, >= 0.

        The start index (inclusive and 0-based) of the global index space.

        * 'stop': integer, > 'start' value.

        The stop index (exclusive, as in standard Python indexing) of the
        global index space.

        * 'step' : integer >= 0.

        * 'blocksize' : integer, >= 1.
        
            Indicates the size of the contiguous blocks for this dimension.

            [TODO: what are the bounds on blocksize?]

        Block cyclic can be thought of as analogous to the cyclic
        distribution, but it distributes contiguous blocks of global indices
        in round robin fashion rather than single indices.  In this way block
        cyclic is a generalization of the block and cyclic dist. types for
        evenly distributed block.  When blocksize == 1, block cyclic is
        equivalent to cyclic; when blocksize == datasize // gridsize,
        block cyclic is equivalent to block distribution.

        [TODO: write down equations relating start, stop, step, blocksize,
        gridsize and gridrank that yield the global indices under block
        cyclic.  Resolve any ambiguites for ugly combinations of gridsize,
        blocksize, step, particularly when "extra" elements are involved.]

    * block padded, dist type of "bp":

        Analogous to block dist type, with an extra padding key.

        * 'start', 'stop', 'step' as in block dist type.

        * 'padding' : tuple of 2 integers, each >= 0.
        
            Indicates the number of shared indices on the lower and upper
            range of indices.

            Padded distribution allows adjacent local array sections overlap
            in index space via the padding parameter.  Whenever an integer in
            the padding tuple is > 0, then that indicates this array is
            sharing indices with its neighbor according to gridrank and,
            further, the neighbor process owns the data.

    * unstructured, dist type of "u":

       * 'indices': list of integers of global indices.

       [TODO: fill in details, constraints.]


Examples
-------------------------------------------------------------------------------


.. vim:spell:ft=rst
