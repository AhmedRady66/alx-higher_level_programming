#!/usr/bin/python3
"""Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define Rectangle class"""
    def __init__(self, width, height):
        """intialize of objects"""
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
        
    def area(self):
        """Method to find area"""
        return self.__width * self.__height

    def __str__(self):
        """Method to return string"""
        return f"[Rectangle] {self.__width}/{self.__height}"
