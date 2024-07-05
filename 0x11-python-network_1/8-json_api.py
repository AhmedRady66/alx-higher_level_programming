#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user letter as a param"""
import requests
import sys


if __name__ == "__main__":

    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    payload = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        resp = r.json()

        if resp == {}:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
