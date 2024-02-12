#!/usr/bin/python3
"""
Define a class Rectangle
"""


class Rectangle:
    """Represent of a rectangle"""
    def __init__(self, width=0, height=0):
        """Intialize the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """width getter for the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter for the attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter for the attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter for the attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
