"""
Utility functions described in the Distributed Array Protocol.
"""


def num_owned_indices(dim_dict):
    """Given a dimension dictionary, return the number of
    indices owned by this process, taking padding into account.
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
