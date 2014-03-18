Automatically Generated Examples
--------------------------------

Block, Nondistributed
`````````````````````

Some description of Block, Nondistributed.

The full (undistributed) array:

>>> full_array
array([[  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.],
       [ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.],
       [ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 4,
  'size': 4,
  'start': 0,
  'stop': 1},
 {'dist_type': 'n', 'size': 8})

In process 1:

>>> distbuffer['buffer']
array([[  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 4,
  'size': 4,
  'start': 1,
  'stop': 2},
 {'dist_type': 'n', 'size': 8})

In process 2:

>>> distbuffer['buffer']
array([[ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 2,
  'proc_grid_size': 4,
  'size': 4,
  'start': 2,
  'stop': 3},
 {'dist_type': 'n', 'size': 8})

In process 3:

>>> distbuffer['buffer']
array([[ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])
>>> distbuffer['dim_data']
({'dist_type': 'b',
  'proc_grid_rank': 3,
  'proc_grid_size': 4,
  'size': 4,
  'start': 3,
  'stop': 4},
 {'dist_type': 'n', 'size': 8})

.. image:: ../images/plot_block_nondist.png


Nondistributed, Block
`````````````````````

Engine properties for: Nondistributed, Block.

The full (undistributed) array:

>>> full_array
array([[  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.],
       [ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.],
       [ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  1.,   2.],
       [  9.,  10.],
       [ 17.,  18.],
       [ 25.,  26.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 0,
  'proc_grid_size': 4,
  'size': 8,
  'start': 0,
  'stop': 2})

In process 1:

>>> distbuffer['buffer']
array([[  3.,   4.],
       [ 11.,  12.],
       [ 19.,  20.],
       [ 27.,  28.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 1,
  'proc_grid_size': 4,
  'size': 8,
  'start': 2,
  'stop': 4})

In process 2:

>>> distbuffer['buffer']
array([[  5.,   6.],
       [ 13.,  14.],
       [ 21.,  22.],
       [ 29.,  30.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 2,
  'proc_grid_size': 4,
  'size': 8,
  'start': 4,
  'stop': 6})

In process 3:

>>> distbuffer['buffer']
array([[  7.,   8.],
       [ 15.,  16.],
       [ 23.,  24.],
       [ 31.,  32.]])
>>> distbuffer['dim_data']
({'dist_type': 'n', 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 3,
  'proc_grid_size': 4,
  'size': 8,
  'start': 6,
  'stop': 8})

.. image:: ../images/plot_nondist_block.png


Block, Block
````````````

Engine properties for: Block, Block.

The full (undistributed) array:

>>> full_array
array([[  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.],
       [ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.],
       [ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

>>> distbuffer['buffer']
array([[  1.,   2.,   3.,   4.],
       [  9.,  10.,  11.,  12.]])
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
array([[  5.,   6.,   7.,   8.],
       [ 13.,  14.,  15.,  16.]])
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
array([[ 17.,  18.,  19.,  20.],
       [ 25.,  26.,  27.,  28.]])
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
array([[ 21.,  22.,  23.,  24.],
       [ 29.,  30.,  31.,  32.]])
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

.. image:: ../images/plot_block_block.png


Block, Cyclic
`````````````

Engine properties for: Block, Cyclic.

The full (undistributed) array:

>>> full_array
array([[  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.],
       [ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.],
       [ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

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
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 1:

>>> distbuffer['buffer']
array([[  2.,   4.,   6.,   8.],
       [ 10.,  12.,  14.,  16.]])
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
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 3:

>>> distbuffer['buffer']
array([[ 18.,  20.,  22.,  24.],
       [ 26.,  28.,  30.,  32.]])
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

.. image:: ../images/plot_block_cyclic.png


Cyclic, Cyclic
``````````````

Engine properties for: Cyclic, Cyclic.

The full (undistributed) array:

>>> full_array
array([[  1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.],
       [  9.,  10.,  11.,  12.,  13.,  14.,  15.,  16.],
       [ 17.,  18.,  19.,  20.,  21.,  22.,  23.,  24.],
       [ 25.,  26.,  27.,  28.,  29.,  30.,  31.,  32.]])

In all processes:

>>> distbuffer = local_array.__distarray__()
>>> distbuffer.keys()
['buffer', 'dim_data', '__version__']
>>> distbuffer['__version__']
'1.0.0'

In process 0:

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
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 1:

>>> distbuffer['buffer']
array([[  2.,   4.,   6.,   8.],
       [ 18.,  20.,  22.,  24.]])
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
  'proc_grid_rank': 0,
  'proc_grid_size': 2,
  'size': 8,
  'start': 0})

In process 3:

>>> distbuffer['buffer']
array([[ 10.,  12.,  14.,  16.],
       [ 26.,  28.,  30.,  32.]])
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

.. image:: ../images/plot_cyclic_cyclic.png


