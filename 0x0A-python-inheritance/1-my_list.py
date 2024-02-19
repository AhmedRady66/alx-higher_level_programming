#!/usr/bin/python3
"""Module for Mylist class"""

class MyList(list):
    """Define class"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
