#!/usr/bin/python3
"""Module for inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if obj isinstance from class inherited"""
    return isinstance(obj, a_class) and type(obj) != a_class
