#!/usr/bin/python3
"""class of square"""
class Square:
    """define the class"""
    def __init__(self, size=0):
        """attributes
        size: size of square
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
