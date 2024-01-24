import sys
import re

NESTED_MORSE = {'A': '.-', 'B': '-...',
                'C': '-.-.', 'D': '-..', 'E': '.',
                'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-',
                'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-',
                'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--',
                'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                '0': '-----', ' ': '/'}


def main():
    """\n\nDescription of the Program

    Parameters:
        argument 1 (str): str contains characters, without special characters
    program:
        convert the argument1 in morse code
    """
    # print(main.__doc__)
    try:
        assert len(sys.argv) == 2
        spaces = sys.argv[1].count(' ')
        alphanum = len(re.findall('[a-zA-Z0-9]', sys.argv[1]))
        assert spaces + alphanum == len(sys.argv[1])
        for x in range(0, len(sys.argv[1])):
            print(NESTED_MORSE[sys.argv[1][x].upper()], end="")
            if (x + 1 < len(sys.argv[1])):
                print(" ", end="")
    except AssertionError as e:
        print("AssertionError: the arguments are bad", e)


if __name__ == "__main__":
    main()
