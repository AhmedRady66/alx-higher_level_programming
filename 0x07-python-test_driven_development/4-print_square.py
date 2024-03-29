#!/usr/bin/python3
"""Module for print_square method."""

def print_square(size):
    """Method for printing a square with # characters.

    Args:
        size: The int size of the square's side.

    Raises:
        TypeError: If size is not an int or size is a float and is less than 0.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
