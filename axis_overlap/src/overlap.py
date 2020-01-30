import re
import sys


def validate_input(in_1: str, in_2: str):
    """Validate if input satisfy correct coordinate format (x1, x2)

    Args:
        in_1: first input string
        in_2: second input string

    Returns:
        Bool
    """
    pattern = '^[-]?[0-9]*\\.?[0-9]*\\,[-]?[0-9]*\\.?[0-9]*$'
    return re.search(pattern, in_1) and re.search(pattern, in_2)


def overlaps(coo_1: tuple, coo_2: tuple):
    """Checks whether one line overlaps the other or not

    Args:
        coo_1:
        coo_2:

    Returns:
        Bool
    """

    x1, x2 = coo_1
    x3, x4 = coo_2

    if x1 == x2 == x3 == x4:
        return True

    if (x1 == x3) or (x1 == x4):
        return True

    if (x2 == x3) or (x2 == x4):
        return True

    if (x3 < x1 < x4) or (x3 < x2 < x4):
        return True

    if (x1 < x3 < x2) or (x1 < x4 < x2):
        return True

    return False


def main():
    x_1_2 = input()
    x_3_4 = input()

    if not validate_input(x_1_2, x_3_4):
        print('Please check that your input is written in valid format')
        sys.exit(0)

    x_1_2 = tuple([int(i) for i in x_1_2.split(',')])
    x_3_4 = tuple([int(i) for i in x_3_4.split(',')])

    if overlaps(x_1_2, x_3_4):
        print(f'{x_1_2} and {x_3_4} overlaps')
    else:
        print(f'{x_1_2} and {x_3_4} do not overlap')


if __name__ == '__main__':
    main()
