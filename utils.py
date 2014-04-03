"""
Utility functions described in the Distributed Array Protocol.
"""


def num_owned_indices_from_block(dim_dict):
    """Given a dimension dictionary with dist_type 'b', return the number of
    indices owned, taking padding into account.
    """
    count = dim_dict['stop'] - dim_dict['start']
    padding = dim_dict.get('padding', (0,0))
    left_process = 0
    right_process = dim_dict['proc_grid_size'] - 1

    # Communication padding doesn't count.
    if dim_dict['proc_grid_rank'] != left_process:
        # We're not at the left boundary;
        # padding[0] is communication padding.
        count -= padding[0]
    if dim_dict['proc_grid_rank'] != right_process:
        # We're not at the right boundary;
        # padding[1] is communication padding.
        count -= padding[1]

    return count


def num_owned_indices_from_cyclic(dd):
    """Given a dimension dictionary `dd` with dist_type 'c', return the number
    of indices owned.
    """
    block_size = dd.get('block_size', 1)
    global_nblocks, partial = divmod(dd['size'], block_size)
    local_nblocks = ((global_nblocks - 1 - dd['proc_grid_rank']) //
                     dd['proc_grid_size']) + 1
    local_partial = partial if dd['proc_grid_rank'] == 0 else 0
    local_size = local_nblocks * dd['block_size'] + local_partial
    return local_size


def num_owned_indices_from_unstructured(dd):
    """Given a dimension dictionary `dd` with dist_type 'u', return the number
    of indices owned.
    """
    indices_buffer = memoryview(dd['indices'])
    return len(indices_buffer)


def num_owned_indices(dd):
    """Given a dimension dictionary `dd` with dist_type 'b', return the number
    of indices owned.
    """
    dist_type = dd['dist_type']
    selector = {'b': num_owned_indices_from_block,
                'c': num_owned_indices_from_cyclic,
                'u': num_owned_indices_from_unstructured,
               }
    return selector[dist_type](dd)
