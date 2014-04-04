===============================================================================
Examples
===============================================================================

Block, Block
````````````

Assume we have a process grid with 2 rows and 1 column, and we have a 2x10
array ``a`` distributed over it.  Let ``a`` be a two-dimensional array with a
block distribution in both dimensions.  Note that since the ``proc_grid_size``
of the first dimension is ``1``, it is essentially undistributed.  Because of
this, having a cyclic ``dist_type`` for this dimension would be equivalent.

In process 0:

.. code:: python

    >>> distbuffer = a0.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '0.9.0'
    >>> distbuffer['buffer']
    array([ 0.2,  0.6,  0.9,  0.6,  0.8,  0.4,  0.2,  0.2,  0.3,  0.5])
    >>> distbuffer['dim_data']
    ({'size': 2,
      'dist_type': 'b',
      'proc_grid_rank': 0,
      'proc_grid_size': 2,
      'start': 0,
      'stop': 1},
     {'size': 10,
      'dist_type': 'b',
      'proc_grid_rank': 0,
      'proc_grid_size': 1,
      'start': 0,
      'stop': 10})

In process 1:

.. code:: python

    >>> distbuffer = a1.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '0.9.0'
    >>> distbuffer['buffer']
    array([ 0.9,  0.2,  1. ,  0.4,  0.5,  0. ,  0.6,  0.8,  0.6,  1. ])
    >>> distbuffer['dim_data']
    ({'size': 2,
      'dist_type': 'b',
      'proc_grid_rank': 1,
      'proc_grid_size': 2,
      'start': 1,
      'stop': 2},
     {'size': 10,
      'dist_type': 'b',
      'proc_grid_rank': 0,
      'proc_grid_size': 1,
      'start': 0,
      'stop': 10})


Block with padding
``````````````````

Assume we have a process grid with 2 processes, and we have an 18-element array
``a`` distributed over it.  Let ``a`` be a one-dimensional array with a
block-padded distribution for its 0th (and only) dimension.

Since the ``'padding'`` for each process is ``(1, 1)``, the local array on each
process has one element of padding on the left and one element of padding on
the right.  Since each of these processes is at one edge of the process grid
(and the array has no ``'periodic'`` dimensions), the "outside" element on each
local array is an example of "boundary padding", and the "inside" element on
each local array is an example of "communication padding".  Note that the
``'size'`` of the distributed array is not equal to the combined buffer sizes
of `a0` and `a1` , since communication padding is not counted toward the size
(though the boundary padding is).

For this example, the global index arrangement on each processor, with 'B' for
boundary and 'C' for communication elements, are arranged as follows::

    Process 0: B 1 2 3 4 5 6 7 8 C
    Process 1:                 C 9 10 11 12 13 14 15 16 B

The 'B' element on process 0 occupies global index 0, and the 'B' element on
process 1 occupies global index 17.  Each 'B' element counts towards the
array's `size`.  The communication elements on each process overlap with a data
element on the other process to indicate which data elements these
communication elements are meant to communicate with.

The protocol data structure on each process is as follows.

In process 0:

.. code:: python

    >>> distbuffer = a0.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '0.9.0'
    >>> distbuffer['buffer']
    array([ 0.2,  0.6,  0.9,  0.6,  0.8,  0.4,  0.2,  0.2,  0.3,  0.9])
    >>> distbuffer['dim_data']
    ({'size': 18,
      'dist_type': 'b',
      'proc_grid_rank': 0,
      'proc_grid_size': 2,
      'start': 0,
      'stop': 10,
      'padding': (1, 1)})

In process 1:

.. code:: python

    >>> distbuffer = a1.__distarray__()
    >>> distbuffer.keys()
    ['__version__', 'buffer', 'dim_data']
    >>> distbuffer['__version__']
    '0.9.0'
    >>> distbuffer['buffer']
    array([ 0.3,  0.9,  0.2,  1. ,  0.4,  0.5,  0. ,  0.6,  0.8,  0.6])
    >>> distbuffer['dim_data']
    ({'size': 18,
      'dist_type': 'b',
      'proc_grid_rank': 1,
      'proc_grid_size': 2,
      'start': 8,
      'stop': 18,
      'padding': (1, 1)})


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
    '0.9.0'
    >>> len(distbuffer['dim_data']) == 1  # one dimension only
    True

In process 0:

.. code:: python

    >>> distbuffer['buffer']
    array([0.7,  0.5,  0.9,  0.2,  0.7,  0.0,  0.5])
    >>> distbuffer['dim_data']
    ({'size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 0,
      'proc_grid_size': 3,
      'indices': array([19, 1, 0, 12, 2, 15, 4])},)

In process 1:

.. code:: python

    >>> distbuffer['buffer']
    array([0.1,  0.5,  0.9])
    >>> distbuffer['dim_data']
    ({'size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 1,
      'proc_grid_size': 3,
      'indices': array([6, 13, 3])},)

In process 2:

.. code:: python

    >>> distbuffer['buffer']
    array([ 0.1,  0.8,  0.4,  0.8,  0.2,  0.4,  0.4,  0.3,  0.5,  0.7,
            0.4,  0.7,  0.6,  0.2,  0.8,  0.5,  0.3,  0.8,  0.4,  0.2])
    >>> distbuffer['dim_data']
    ({'size': 30,
      'dist_type': 'u',
      'proc_grid_rank': 2,
      'proc_grid_size': 3,
      'indices': array([10, 25,  5, 21,  7, 18, 11, 26, 29, 24, 23, 28, 14,
                  20,  9, 16, 27,  8, 17, 22])},)

.. include:: examples.rst
