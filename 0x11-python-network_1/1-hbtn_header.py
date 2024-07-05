#!/usr/bin/python3
"""Display the value of the X-Request-Id"""
import urllib.request
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as resp:
        print(dict(resp.headers).get("X-Request-Id"))
