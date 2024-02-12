#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Define Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize args of the class

        Args:
            height: input height of rectangle
            width: input width of rectangle
        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        """height getter.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
         """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If value is not an int.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
