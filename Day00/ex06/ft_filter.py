def ft_filter(function, object):
    """
        Call the 'function' for all item in object
    """
    new = [x for x in object if function(x)]
    return (new)
