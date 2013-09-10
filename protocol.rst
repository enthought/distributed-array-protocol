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
    contained in a contiguous Tpetra::Array.  A Vector's Tpetra::Map is
    responsible for converting local indices to and from global indices.  A
    Vector's Tpetra::Comm communicator is analogous to an MPI communicator
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

  * Process: a "process" is the basic unit of execution; each process has an
    address space, local objects, and is able to communicate with other
    processes to send and receive data.  Same as an MPI process, an IPython
    engine, etc.

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

The DAP is a process-local protocol and allows two subscribers, called
the "producer" and the "consumer", to communicate the essential data and
metadata necessary to share a distributed array between them.  This allows two
independently developed components to access, modify, and update a distributed
array without copying.

The DAP is intended to build on the concepts and implementation of the
existing PEP-3118 buffer protocol, and uses PEP-3118 buffers (and subscribing
Python objects, such as memoryviews and NumPy arrays) as an integral
component.

This version of the DAP is defined for the Python language.  Future versions
of this protocol may provide definitions in other languages.

A "producer object" that subscribes to the DAP shall provide a method named
"__distarray__" that, when called by a consumer, returns a dictionary with two
keys, "buffer" and "maps".

The value associated with the "buffer" key shall be a buffer that is
compatible with the PEP-3118 buffer protocol and contains the data for a local
section of a distributed array.

The value for the "maps" key is a tuple of dictionaries, called "dimension
dictionaries", one dictionary for each dimension of the distributed array,
with the zeroth dictionary associated with the zeroth dimension of the array,
etc.  These dictionaries are intended to include all metadata required to
fully specify the distributed array.

All dimension dictionaries shall have the following key-value pairs:

  * "disttype" : string

    The disttype indicates the type of distribution along this dimension of
    the array.  The values can be one of the following:

    'b' block distribution with no padding.
    'c' cyclic distribution.
    'bc' block cyclic.
    'bp' block-padded.
    'u' unstructured.

  * 'gridrank' : integer

  * 'gridsize' : integer

  * 'datasize' : integer

  * 'indices' : 3-element tuple of integers

  * 'blocksize' : 


.. vim:spell:ft=rst
