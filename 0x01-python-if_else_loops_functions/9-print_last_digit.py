#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        result = number % 10
    else:
        result = abs(number % -10)
    print(f"{result}", end="")
    return result
