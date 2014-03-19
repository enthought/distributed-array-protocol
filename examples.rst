Automatically Generated Examples
--------------------------------

Block, Nondistributed
`````````````````````

4 X 8 array, Block, Nondistributed distribution, distributed over 4 process grid.

Some description of Block, Nondistributed.

.. image:: ../images/plot_block_nondist.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[ 0.  1.  2.  3.  4.  5.  6.  7.]],
 [[  8.   9.  10.  11.  12.  13.  14.  15.]],
 [[ 16.  17.  18.  19.  20.  21.  22.  23.]],
 [[ 24.  25.  26.  27.  28.  29.  30.  31.]]]

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
 {'dist_type': 'n', 'size': 8})

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
 {'dist_type': 'n', 'size': 8})

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
 {'dist_type': 'n', 'size': 8})

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
 {'dist_type': 'n', 'size': 8})

Nondistributed, Block
`````````````````````

4 X 8 array, Nondistributed, Block distribution, distributed over 4 process grid.

.. image:: ../images/plot_nondist_block.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[  0.   1.]
 [  8.   9.]
 [ 16.  17.]
 [ 24.  25.]],
 [[  2.   3.]
 [ 10.  11.]
 [ 18.  19.]
 [ 26.  27.]],
 [[  4.   5.]
 [ 12.  13.]
 [ 20.  21.]
 [ 28.  29.]],
 [[  6.   7.]
 [ 14.  15.]
 [ 22.  23.]
 [ 30.  31.]]]

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
({'dist_type': 'n', 'size': 4},
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
({'dist_type': 'n', 'size': 4},
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
({'dist_type': 'n', 'size': 4},
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
({'dist_type': 'n', 'size': 4},
 {'dist_type': 'b',
  'proc_grid_rank': 3,
  'proc_grid_size': 4,
  'size': 8,
  'start': 6,
  'stop': 8})

Block, Block
````````````

4 X 8 array, Block, Block distribution, distributed over 2 X 2 process grid.

.. image:: ../images/plot_block_block.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[  0.   1.   2.   3.]
 [  8.   9.  10.  11.]],
 [[  4.   5.   6.   7.]
 [ 12.  13.  14.  15.]],
 [[ 16.  17.  18.  19.]
 [ 24.  25.  26.  27.]],
 [[ 20.  21.  22.  23.]
 [ 28.  29.  30.  31.]]]

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

4 X 8 array, Block, Cyclic distribution, distributed over 2 X 2 process grid.

.. image:: ../images/plot_block_cyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[  0.   2.   4.   6.]
 [  8.  10.  12.  14.]],
 [[  1.   3.   5.   7.]
 [  9.  11.  13.  15.]],
 [[ 16.  18.  20.  22.]
 [ 24.  26.  28.  30.]],
 [[ 17.  19.  21.  23.]
 [ 25.  27.  29.  31.]]]

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

4 X 8 array, Cyclic, Cyclic distribution, distributed over 2 X 2 process grid.

.. image:: ../images/plot_cyclic_cyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[  0.   2.   4.   6.]
 [ 16.  18.  20.  22.]],
 [[  1.   3.   5.   7.]
 [ 17.  19.  21.  23.]],
 [[  8.  10.  12.  14.]
 [ 24.  26.  28.  30.]],
 [[  9.  11.  13.  15.]
 [ 25.  27.  29.  31.]]]

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

BlockCyclic[2], BlockCyclic[2]
``````````````````````````````

4 X 8 array, BlockCyclic[2], BlockCyclic[2] distribution, distributed over 2 X 2 process grid.

.. image:: ../images/plot_blockcyclic_blockcyclic.png

The full (undistributed) array:

>>> full_array
array([[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.],
       [  8.,   9.,  10.,  11.,  12.,  13.,  14.,  15.],
       [ 16.,  17.,  18.,  19.,  20.,  21.,  22.,  23.],
       [ 24.,  25.,  26.,  27.,  28.,  29.,  30.,  31.]])

get_localarrays():

>>> get_localarrays()
[[[  0.   1.   4.   5.]
 [  8.   9.  12.  13.]],
 [[  2.   3.   6.   7.]
 [ 10.  11.  14.  15.]],
 [[ 16.  17.  20.  21.]
 [ 24.  25.  28.  29.]],
 [[ 18.  19.  22.  23.]
 [ 26.  27.  30.  31.]]]

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

