import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    try:
        assert family.__class__ == list, "Bad type for family / provide a list"
        assert len(family) > 0, "Bad size"
        tmp = len(family[0])
        for x in family:
            assert len(x) == tmp, "Bad shape for 2D array"
        print("My shape is :", np.shape(family))
        family = family[start:end:]
        print("My new shape is :", np.shape(family))
        return (family)
    except AssertionError as e:
        print(e)
        return (family)