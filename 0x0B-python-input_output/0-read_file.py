#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """read filename input"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read(), end="")
