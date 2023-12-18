#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    ele = 0
    try:
        while ele is not x:
            print(my_list[ele], end="")
            ele += 1
    except IndexError:
        None
    print(end="\n")
    return ele 
