Block, Nondistributed
`````````````````````

4 X 8 array, Block, Nondistributed distribution, over 4 X 1 process grid.

.. image:: ../images/plot_block_nondist.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[ 0.,  1.,  2.,  3.,  4.,  5.,  6.,  7.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 4,
  'size': 4,
  'start': 0,
  'stop': 1},
 {'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 8})

In process 1:

>>> distbuffer['buffer']
array([[  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 4,
  'size': 4,
  'start': 1,
  'stop': 2},
 {'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 8})

In process 2:

>>> distbuffer['buffer']
array([[ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 2,
  'proc_grid_size': 4,
  'size': 4,
  'start': 2,
  'stop': 3},
 {'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 8})

In process 3:

>>> distbuffer['buffer']
array([[ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 3,
  'proc_grid_size': 4,
  'size': 4,
  'start': 3,
  'stop': 4},
 {'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 8})

Nondistributed, Block
`````````````````````

4 X 8 array, Nondistributed, Block distribution, over 1 X 4 process grid.

.. image:: ../images/plot_nondist_block.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   1.],
       [  8.,   9.],
       [ 16.,  17.],
       [ 24.,  25.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 4,
  'size': 8,
  'start': 0,
  'stop': 2})

In process 1:

>>> distbuffer['buffer']
array([[  2.,   3.],
       [ 10.,  11.],
       [ 18.,  19.],
       [ 26.,  27.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 4,
  'size': 8,
  'start': 2,
  'stop': 4})

In process 2:

>>> distbuffer['buffer']
array([[  4.,   5.],
       [ 12.,  13.],
       [ 20.,  21.],
       [ 28.,  29.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 2,
  'proc_grid_size': 4,
  'size': 8,
  'start': 4,
  'stop': 6})

In process 3:

>>> distbuffer['buffer']
array([[  6.,   7.],
       [ 14.,  15.],
       [ 22.,  23.],
       [ 30.,  31.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'proc_grid_rank': 0, 'proc_grid_size': 1, 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 3,
  'proc_grid_size': 4,
  'size': 8,
  'start': 6,
  'stop': 8})

Block, Block
````````````

4 X 8 array, Block, Block distribution, over 2 X 2 process grid.

.. image:: ../images/plot_block_block.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   1.,   2.,   3.],
       [  8.,   9.,  10.,  11.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0,
  'stop': 4})

In process 1:

>>> distbuffer['buffer']
array([[  4.,   5.,   6.,   7.],
       [ 12.,  13.,  14.,  15.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 4,
  'stop': 8})

In process 2:

>>> distbuffer['buffer']
array([[ 16.,  17.,  18.,  19.],
       [ 24.,  25.,  26.,  27.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0,
  'stop': 4})

In process 3:

>>> distbuffer['buffer']
array([[ 20.,  21.,  22.,  23.],
       [ 28.,  29.,  30.,  31.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 4,
  'stop': 8})

Block, Cyclic
`````````````

4 X 8 array, Block, Cyclic distribution, over 2 X 2 process grid.

.. image:: ../images/plot_block_cyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   2.,   4.,   6.],
       [  8.,  10.,  12.,  14.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 1:

>>> distbuffer['buffer']
array([[  1.,   3.,   5.,   7.],
       [  9.,  11.,  13.,  15.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 1})

In process 2:

>>> distbuffer['buffer']
array([[ 16.,  18.,  20.,  22.],
       [ 24.,  26.,  28.,  30.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 3:

>>> distbuffer['buffer']
array([[ 17.,  19.,  21.,  23.],
       [ 25.,  27.,  29.,  31.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 1})

Cyclic, Cyclic
``````````````

4 X 8 array, Cyclic, Cyclic distribution, over 2 X 2 process grid.

.. image:: ../images/plot_cyclic_cyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   2.,   4.,   6.],
       [ 16.,  18.,  20.,  22.]])
>>> distbuffer['dim_data']
({'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 1:

>>> distbuffer['buffer']
array([[  1.,   3.,   5.,   7.],
       [ 17.,  19.,  21.,  23.]])
>>> distbuffer['dim_data']
({'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 1})

In process 2:

>>> distbuffer['buffer']
array([[  8.,  10.,  12.,  14.],
       [ 24.,  26.,  28.,  30.]])
>>> distbuffer['dim_data']
({'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 1},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 3:

>>> distbuffer['buffer']
array([[  9.,  11.,  13.,  15.],
       [ 25.,  27.,  29.,  31.]])
>>> distbuffer['dim_data']
({'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 1},
 {'block_size': 1,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 1})

BlockCyclic, BlockCyclic
````````````````````````

4 X 8 array, BlockCyclic, BlockCyclic distribution, over 2 X 2 process grid.

.. image:: ../images/plot_blockcyclic_blockcyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   1.,   4.,   5.],
       [  8.,   9.,  12.,  13.]])
>>> distbuffer['dim_data']
({'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0},
 {'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 1:

>>> distbuffer['buffer']
array([[  2.,   3.,   6.,   7.],
       [ 10.,  11.,  14.,  15.]])
>>> distbuffer['dim_data']
({'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0},
 {'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 2})

In process 2:

>>> distbuffer['buffer']
array([[ 16.,  17.,  20.,  21.],
       [ 24.,  25.,  28.,  29.]])
>>> distbuffer['dim_data']
({'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2},
 {'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 3:

>>> distbuffer['buffer']
array([[ 18.,  19.,  22.,  23.],
       [ 26.,  27.,  30.,  31.]])
>>> distbuffer['dim_data']
({'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2},
 {'block_size': 2,
  'dist_type': 'c',
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 2})

BlockPadded, BlockPadded
````````````````````````

4 X 8 array, BlockPadded, BlockPadded distribution, over 2 X 2 process grid.

.. image:: ../images/plot_blockpad_blockpad.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  0.,   1.,   2.,   3.],
       [  8.,   9.,  10.,  11.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0,
  'stop': 4})

In process 1:

>>> distbuffer['buffer']
array([[  4.,   5.,   6.,   7.],
       [ 12.,  13.,  14.,  15.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4,
  'start': 0,
  'stop': 2},
 {'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 4,
  'stop': 8})

In process 2:

>>> distbuffer['buffer']
array([[ 16.,  17.,  18.,  19.],
       [ 24.,  25.,  26.,  27.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0,
  'stop': 4})

In process 3:

>>> distbuffer['buffer']
array([[ 20.,  21.,  22.,  23.],
       [ 28.,  29.,  30.,  31.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4,
  'start': 2,
  'stop': 4},
 {'dist_type': 'b',
  'padding': (1, 1),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8,
  'start': 4,
  'stop': 8})

Unstructured, Unstructured
``````````````````````````

4 X 8 array, Unstructured, Unstructured distribution, over 2 X 2 process grid.

.. image:: ../images/plot_unstruct_unstruct.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[ 18.,  16.,  19.,  23.],
       [  2.,   0.,   3.,   7.]])
>>> distbuffer['dim_data']
({'dist_type': 'u',
  'indices': array([2, 0]),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4},
 {'dist_type': 'u',
  'indices': array([2, 0, 3, 7]),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8})

In process 1:

>>> distbuffer['buffer']
array([[ 20.,  17.,  22.,  21.],
       [  4.,   1.,   6.,   5.]])
>>> distbuffer['dim_data']
({'dist_type': 'u',
  'indices': array([2, 0]),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 4},
 {'dist_type': 'u',
  'indices': array([4, 1, 6, 5]),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8})

In process 2:

>>> distbuffer['buffer']
array([[ 26.,  24.,  27.,  31.],
       [ 10.,   8.,  11.,  15.]])
>>> distbuffer['dim_data']
({'dist_type': 'u',
  'indices': array([3, 1]),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4},
 {'dist_type': 'u',
  'indices': array([2, 0, 3, 7]),
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8})

In process 3:

>>> distbuffer['buffer']
array([[ 28.,  25.,  30.,  29.],
       [ 12.,   9.,  14.,  13.]])
>>> distbuffer['dim_data']
({'dist_type': 'u',
  'indices': array([3, 1]),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 4},
 {'dist_type': 'u',
  'indices': array([4, 1, 6, 5]),
  'proc_grid_rank': 1,
  'proc_grid_size': 2,
  'size': 8})

