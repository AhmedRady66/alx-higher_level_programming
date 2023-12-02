#!/usr/bin/python3
def max_integer(my_list=[]):
    maxi = my_list[0]
    if my_list == []:
        return None
    for i in my_list:
        if my_list[i] > maxi:
            maxi = my_list[i]
            return my_list[i]
