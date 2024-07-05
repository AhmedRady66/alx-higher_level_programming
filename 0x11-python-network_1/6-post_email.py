#!/usr/bin/python3
"""Display the value of the variable X-Request-Id in the response header"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
