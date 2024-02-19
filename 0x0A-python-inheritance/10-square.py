#!/usr/bin/python3
"""Square class"""
Rectangle  = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define class"""
    def __init__(self, size):
        """Intialize objects"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method to find area"""
        return self.__size ** 2
