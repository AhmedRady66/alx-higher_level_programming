#!/usr/bin/python3
"""Display the body of the response (decoded in utf-8)"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as resp:
            print(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
