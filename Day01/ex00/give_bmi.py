def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    try:
        assert len(height) == len(weight), "Len of lists differ"
        ret = []
        for n in range(0, len(height)):
            assert height[n].__class__ == int or float, "Bad Type 1"
            assert weight[n].__class__ == int or float, "Bad Type 3"
            ret.append(weight[n] / height[n]**2 if height[n] > 0 else 0)
    except AssertionError as e:
        print(e)
        exit(0)
    return (ret)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret = []
    for k in bmi:
        if k > limit:
            ret.append(True)
        else:
            ret.append(False)
    return (ret)
