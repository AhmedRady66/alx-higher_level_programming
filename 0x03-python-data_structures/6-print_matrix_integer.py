#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for j in matrix:
        if len(j) == 0:
            print()
    for row in matrix:
        for ele in row:
            print("{:d}".format(ele), end=" ")
        print()
