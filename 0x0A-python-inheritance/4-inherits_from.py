#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited from the specified class"""
    return isinstance(obj, a_class) and type(obj) != a_class
