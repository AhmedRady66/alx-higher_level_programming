#!/usr/bin/python3
"""append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing a string"""
    with open(filename, "r", encoding="utf-8") as f:
        line_list = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_list.append(line)
            if search_string in line:
                line_list.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(line_list)
