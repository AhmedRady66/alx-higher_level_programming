#!/usr/bin/python3
'''Module for Square class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Representation of a string"""
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - "\
               f"{self.width}"

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = height

    def __update(self, id=None, size=None, x=None, y=None):
        """Internal method that updates instance attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)
