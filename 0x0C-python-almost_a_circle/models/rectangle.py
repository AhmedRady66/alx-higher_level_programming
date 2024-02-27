#!/usr/bin/python3
""" Rectangle class """
from models.base import Base


class Rectangle(Base):
    """Define class"""
    def __init__(self, width, height, x=0, y=0, id=None):
     """Initialize class"""
     Base.__init__(self, id)
     self.width = width
     self.height = height
     self.x = x
     self.y = y

     @property
     def width(self):
         """get width"""
         return self.__width

     @width.setter
     def width(self, value):
         """set width"""
         self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
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