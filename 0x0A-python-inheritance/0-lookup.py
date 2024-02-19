#!/usr/bin/python3
"""Module for lookup"""


def lookup(obj):
    """returns the list of available attributes and methods
    Args:
        obj: object input
    Return:
        list of attributes
    """
    return dir(obj)
