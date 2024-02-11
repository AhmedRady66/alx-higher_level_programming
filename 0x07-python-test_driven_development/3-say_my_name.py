#!/usr/bin/python3
"""module for say_my_name method"""

def say_my_name(first_name, last_name=""):
    """Prints My name is <first name> <last name>

    Args:
        first_name: input first name
        last_name: input last name

    Raises:
        TypeError: if first_name and last_name not strings

    Return:
        0 success
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name,last_name))
