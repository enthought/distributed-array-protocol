==============================================================================
Distributed Array Protocol -- v0.0.1
==============================================================================

This document is a chalkboard to design the distributed array protocol (DAP).

Goal
-------------------------------------------------------------------------------

To define the core data structures and API for the protocol such that it can be
implemented by a subscribing package / project.

The need and focus is on making the protocol concrete such that it is
unambiguously implementable.

Initial focus is on a simple-enough protocol that can provide initial 

Overview
-------------------------------------------------------------------------------

Usecases
-------------------------------------------------------------------------------

This list needs to be prioritized and fleshed out -- what follows is not in
order of importance:

    * Multiple dimensions

    * Structured and unstructured meshes

    * Dense and sparse arrays / matrices

    * Regular and irregular data distributions

    * Overlapping data distributions

    * Ghost vectors / halos

    * Global address space -- global indexing and local indexing

    * Array slicing:

        * Regular slicing -- uniform step, results in a numpy view.

        * Fancy indexing -- results in a numpy copy.

    * Distributed ufunc operations between 2 distributed arrays: c = a *op* b :

        * a & b must be conformable

        * General case: a & b arbitrarily distributed arrays, require
          communication

        * Who does computation (source or destination) when communication
          required?  Allow user control with some default?  Allow user to
          control performance / convenience trade off with decorators / context
          managers.

    * User-defined kernels that are vectorized in a distributed fashion:

        * `elemental` semantics in Fortran 90 / 95; easy to apply, restricts
          kernel to functional programming with no side effects.

        * What communication, if any, is allowed in kernels?


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


.. vim:spell:ft=rst
