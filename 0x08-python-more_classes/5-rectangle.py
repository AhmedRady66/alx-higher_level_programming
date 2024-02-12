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

    def area(self):
        """calculate area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """calculate perimeter of rectangle"""
        if (self.__width) == 0 or (self.__height) == 0:
            return 0
        return 2*(self.__height + self.__width)

    def __str__(self):
        """return printing the rectangle with the character #"""
        result = ""
        if (self.__width) != 0 or (self.__height) != 0:
            result += "\n".join("#" * self.__width
                                for i in range(self.__height))
        return result

    def __repr__(self):
        """return the rectangle with the character # for developer"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deleteing rectangle"""
        print("Bye rectangle...")
