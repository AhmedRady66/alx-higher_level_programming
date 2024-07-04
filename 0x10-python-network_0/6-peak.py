#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """peak of list of integers"""
    result = 0
    if len(list_of_integers) == 0:
        return None
    for peak in range(len(list_of_integers)):
        if peak == 0 and list_of_integers[peak] >= list_of_integers[peak+1]:
            result = list_of_integers[peak]
        elif peak == list_of_integers[-1] and \
                list_of_integers[peak] >= list_of_integers[peak-1]:
            result = list_of_integers[peak]
        elif list_of_integers[peak] >= list_of_integers[peak-1] \
                and list_of_integers[peak] >= list_of_integers[peak+1]:
            result = list_of_integers[peak]
    return result
