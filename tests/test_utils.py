# encoding: utf-8
# ---------------------------------------------------------------------------
#  Copyright (C) 2008-2014, Enthought, Inc.
#  Distributed under the terms of the BSD License.  See COPYING.rst.
# ---------------------------------------------------------------------------


import unittest
from utils import num_owned_indices


class NumOwnedIndicesBlock(unittest.TestCase):

    def test_plain_block_edge(self):
        dd = {'size': 50,
              'dist_type': 'b',
              'proc_grid_rank': 0,
              'proc_grid_size': 10,
              'start': 0,
              'stop': 10,
             }
        self.assertEqual(num_owned_indices(dd), 10)

    def test_plain_block_middle(self):
        dd = {'size': 50,
              'dist_type': 'b',
              'proc_grid_rank': 7,
              'proc_grid_size': 10,
              'start': 30,
              'stop': 40,
             }
        self.assertEqual(num_owned_indices(dd), 10)

    def test_padded_block_left_edge(self):
        dd = {'size': 100,
              'dist_type': 'b',
              'proc_grid_rank': 0,
              'proc_grid_size': 10,
              'start': 0,
              'stop': 20,
              'padding': (3, 4),
             }
        self.assertEqual(num_owned_indices(dd), 16)

    def test_padded_block_right_edge(self):
        dd = {'size': 100,
              'dist_type': 'b',
              'proc_grid_rank': 9,
              'proc_grid_size': 10,
              'start': 80,
              'stop': 100,
              'padding': (3, 4),
             }
        self.assertEqual(num_owned_indices(dd), 17)

    def test_padded_block_middle(self):
        dd = {'size': 100,
              'dist_type': 'b',
              'proc_grid_rank': 3,
              'proc_grid_size': 10,
              'start': 50,
              'stop': 70,
              'padding': (3, 4),
             }
        self.assertEqual(num_owned_indices(dd), 13)

    def test_padded_block_one_proc(self):
        dd = {'size': 100,
              'dist_type': 'b',
              'proc_grid_rank': 0,
              'proc_grid_size': 1,
              'start': 0,
              'stop': 100,
              'padding': (3, 4),
             }
        self.assertEqual(num_owned_indices(dd), 100)


class NumOwnedIndicesCyclic(unittest.TestCase):

    def test_cyclic_left_edge(self):
        dd = {'block_size': 1,
              'dist_type': 'c',
              'proc_grid_rank': 0,
              'proc_grid_size': 4,
              'size': 9,
              'start': 0}
        self.assertEqual(num_owned_indices(dd), 3)

    def test_cyclic_right_edge(self):
        dd = {'block_size': 1,
              'dist_type': 'c',
              'proc_grid_rank': 3,
              'proc_grid_size': 4,
              'size': 9,
              'start': 3}
        self.assertEqual(num_owned_indices(dd), 2)

    def test_block_cyclic_left_edge(self):
        dd = {'block_size': 2,
              'dist_type': 'c',
              'proc_grid_rank': 0,
              'proc_grid_size': 4,
              'size': 9,
              'start': 0}
        self.assertEqual(num_owned_indices(dd), 3)

    def test_block_cyclic_right_edge(self):
        dd = {'block_size': 5,
              'dist_type': 'c',
              'proc_grid_rank': 3,
              'proc_grid_size': 4,
              'size': 9,
              'start': 9}
        self.assertEqual(num_owned_indices(dd), 0)


class NumOwnedIndicesUnstructured(unittest.TestCase):

    def test_unstructured(self):

        dd = {'dist_type': 'u',
              'indices': bytearray([4, 3, 2]),
              'proc_grid_rank': 1,
              'proc_grid_size': 2,
              'size': 5}
        self.assertEqual(num_owned_indices(dd), 3)
