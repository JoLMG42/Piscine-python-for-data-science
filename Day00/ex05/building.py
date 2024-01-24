import re
import sys


def main():
    """\n\nDescription of the Program

    Parameters:
        argument 1 (string): string contains characters

    program:
        count the number of different character in the string:
        total of characters, upper/lower case, punctuation, spaces, digits\n\n
   """
    # print(main.__doc__)
    try:
        assert len(sys.argv) <= 2, "AssertionError: wrong number of argument"
        if len(sys.argv) == 1:
            s = input("Please provide something -> ")
        else:
            s = sys.argv[1]
        print("The text contains", len(s), "characters:")
        print(len(re.findall(r'[A-Z]', s)), "upper letters")
        print(len(re.findall(r'[a-z]', s)), "lower letters")
        pon = "punctuation marks"
        print(len(re.findall(r'[^\w\s]', s)), pon)
        print((s).count(' '), "spaces")
        print(len(re.findall(r'\d', s)), "digits")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
