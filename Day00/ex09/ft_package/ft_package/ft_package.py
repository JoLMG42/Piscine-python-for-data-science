def count_in_list(lst, find) -> int:
    """
        Count number of 'find' in lst
    """
    res = 0
    for i in lst:
        if i == find:
            res += 1
    return (res)
