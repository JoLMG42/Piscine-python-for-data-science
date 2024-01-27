from ft_filter import ft_filter
import sys
import re


def print_words(obj):
    if len(obj) > int(sys.argv[2]):
        return (1)
    return (0)


def main():
    """\n\nDescription of the Program

    Parameters:
        argument 1 (list): list of args contains strings
        argument 2 (int):  number represent a len
    program:
        print strings of len > argument2
    """
    # print(main.__doc__)
    # print(ft_filter.__doc__)
    try:
        assert len(sys.argv) == 3
        assert ((sys.argv[2]).lstrip('+-')).isnumeric() == 1
        assert sys.argv[2].count('+') + sys.argv[2].count('-') <= 1
        spaces = sys.argv[1].count(' ')
        alpha = len(re.findall('[a-zA-Z]', sys.argv[1]))
        assert spaces + alpha == len(sys.argv[1])
        print(ft_filter(print_words, str(sys.argv[1]).split(' ')))
        s = sys.argv[1].split(' ')
        print(ft_filter(lambda x: len(x) > int(sys.argv[2]), s))

    except AssertionError as e:
        print("AssertionError: the arguments are bad", e)


if __name__ == "__main__":
    main()
