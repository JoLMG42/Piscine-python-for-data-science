import sys


try:
    len = len(sys.argv)
    assert len != 1, ""
    assert len == 2, "AssertionError: more than one argument is provided"
    err = "AssertionError: argument is not an integer"
    assert ((sys.argv[1]).lstrip('+-')).isnumeric() is True, err
    assert sys.argv[1].count('+') + sys.argv[1].count('-') <= 1, err
    print("I'm Even." if int(sys.argv[1]) % 2 == 0 else "I'm Odd.")

except AssertionError as e:
    print(e)
