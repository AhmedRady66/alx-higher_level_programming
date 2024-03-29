#!/usr/bin/python3
"""module for add_integer method"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a: first input
        b: second input (default = 98)

    Raises:
        TypeError: if a, b are not integer

    Return:
        sum of integer a and b
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
