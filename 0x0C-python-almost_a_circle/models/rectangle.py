#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Define Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width of rectangle"""
        self.__width = value

    @property
    def height(self):
        """get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height of rectangle"""
        self.__height = value

    @property
    def x(self):
        """get x value"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x value"""
        self.__x = value

    @property
    def y(self):
        """get y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y value"""
        self.__y = value
