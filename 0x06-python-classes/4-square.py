#!/usr/bin/python3
"""class of square"""
class Square:
    """define the class"""
    def __init__(self, size=0):
        """attributes
        size: size of square
        """
        self.size = size
        
    def area(self):
        """Return the area of square"""
        return self.__size**2
    @property
    def size(self):
        """return size as getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size using setter method"""
        self.__size = value
        if type(value) != int:
             raise TypeError("size must be an integer")
        if value < 0:
             raise ValueError("size must be >= 0")
