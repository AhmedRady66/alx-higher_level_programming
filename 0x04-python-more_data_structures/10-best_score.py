#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxa = 0
    maxk = None
    for x, y in a_dictionary.items():
        if y > maxa:
            maxa = y
            maxk = x
    return maxk
