#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """Define BaseGeometry class"""
    def area(self):
        """Method to find area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
