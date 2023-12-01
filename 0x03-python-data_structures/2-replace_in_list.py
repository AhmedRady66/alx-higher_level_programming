#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i in my_list:
        if idx < 0 or idx > len(my_list):
            return None
        elif idx == i:
            my_list[i] = element
            return my_list
