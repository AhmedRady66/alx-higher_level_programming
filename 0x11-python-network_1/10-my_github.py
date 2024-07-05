#!/usr/bin/python3
""" Python script that takes your GitHub credentials """
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get('https://api.github.com/user', auth=authentication)
    print(r.json().get("id"))
