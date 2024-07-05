#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print(f"Body response:")
        print(f"    - type: {type(data)}")
        print(f"    - content: {data}")
        print(f"    - utf8 content: {data.decode()}")
