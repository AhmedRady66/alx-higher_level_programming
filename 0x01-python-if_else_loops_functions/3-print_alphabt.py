#!/usr/bin/python3
alpha = 'a'
while alpha <= 'z':
    if alpha == 'q' or alpha == 'e':
        alpha = chr(ord(alpha) + 1)
        continue
    print("{:s}".format(alpha), end="")
    alpha = chr(ord(alpha) + 1)
