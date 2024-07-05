#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    reqe = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(reqe) as resp:
        data = resp.read()
        print(f"Body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {data.decode()}")
