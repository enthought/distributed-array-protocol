import unittest
import numpy as np

from . import validator


class TestValidDimData(unittest.TestCase):

    def test_block(self):
        dim_data = ({'dist_type': 'b',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 0,
            'stop': 10},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(10),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_cyclic(self):
        dim_data = ({'dist_type': 'c',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 0},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(50),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_block_cyclic(self):
        dim_data = ({'dist_type': 'c',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 1,
            'start': 5,
            'block_size': 5},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(50),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_unstructured(self):
        dim_data = ({'dist_type': 'u',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 1,
            'indices': np.array([1, 22, 44, 49, 9, 33, 21], dtype=np.uint32)
            },)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(len(dim_data[0]['indices'])),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_extra_process(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':0,
            'start' : 0,
            }
        distbuffer = {'__version__': '1.0.0',
                'buffer' : b'a',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_empty_process(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':3,
            'start' : 3,
            }
        distbuffer = {'__version__': '1.0.0',
                'buffer' : b'',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)

    def test_empty_dict_alias(self):
        dimdata = {}
        distbuffer = {'__version__': '1.0.0',
                'buffer' : b'',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)


class TestMissingKeys(unittest.TestCase):

    def test_missing_buffer(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':3,
            'start' : 3,
            }
        distbuffer = {'__version__': '1.0.0',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(not is_valid, msg)

    def test_missing_version(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':3,
            'start' : 3,
            }
        distbuffer = {'buffer' : b'',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(not is_valid, msg)

    def test_missing_dim_data(self):
        distbuffer = {'__version__': '1.0.0',
                'buffer' : b'',}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(not is_valid, msg)


class TestInvalidKeys(unittest.TestCase):

    def test_bad_buffer(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':3,
            'start' : 3,
            }
        distbuffer = {'__version__': '1.0.0',
                'dim_data' : (dimdata,),
                'buffer' : [1,2,3,4],}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(not is_valid, msg)

    def test_bad_version(self):
        dimdata = {
            'dist_type':'c',
            'size':3,
            'proc_grid_size':4,
            'proc_grid_rank':3,
            'start' : 3,
            }
        distbuffer = {'__version__': 'v1.0.0alpha',
                'buffer' : b'',
                'dim_data' : (dimdata,)}
        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(not is_valid, msg)


class TestInvalidDimData(unittest.TestCase):

    def test_bad_dist_type(self):
        """Test stop > size."""
        dim_data = ({'dist_type': 'q',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 0,
            'stop': 51},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(51),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_block_stop_0(self):
        """Test stop > size."""
        dim_data = ({'dist_type': 'b',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 0,
            'stop': 51},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(51),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_block_stop_1(self):
        """Test stop < start."""
        dim_data = ({'dist_type': 'b',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 10,
            'stop': 9},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones((0,)),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_block_start(self):
        """Test negative start."""
        dim_data = ({'dist_type': 'b',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': -1,
            'stop': 10},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(11),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_block_padding(self):
        """Test padding not ints."""
        dim_data = ({'dist_type': 'b',
            'size': 50,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'start': 0,
            'stop': 10,
            'padding': ('a','b')},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(10),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_cyclic_block_size(self):
        """Test negative block size in cyclic."""
        dim_data = ({'dist_type': 'c',
            'size': 100,
            'proc_grid_size': 3,
            'proc_grid_rank': 0,
            'start': 0,
            'block_size': -10},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(10),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)

    def test_bad_unstructured_indices(self):
        """Test non-buffer for unstructured indices."""
        dim_data = ({'dist_type': 'u',
            'size': 100,
            'proc_grid_size': 2,
            'proc_grid_rank': 0,
            'indices': [1, 2, 3, 4]},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(4),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertFalse(is_valid, msg)


class TestCornerCases(unittest.TestCase):

    def test_undistributed_padded_periodic(self):
        dim_data = ({'dist_type': 'b',
            'size': 10,
            'proc_grid_size': 1,
            'proc_grid_rank': 0,
            'start': 0,
            'stop': 10,
            'padding': (2,2),
            'periodic': True,},)
        distbuffer = {'__version__': '1.0.0',
                'buffer': np.ones(10),
                'dim_data': dim_data}

        is_valid, msg = validator.validate(distbuffer)
        self.assertTrue(is_valid, msg)
