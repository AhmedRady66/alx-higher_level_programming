#!/usr/bin/python3
alpha = 'a'
while alpha <= 'z':
    print("{:s}".format(alpha), end="")
    alpha = chr(ord(alpha) + 1)
