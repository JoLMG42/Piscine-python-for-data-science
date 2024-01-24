def ft_filter(function, object):
    new = [x for x in object if function(x)]
    return (new)
