#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    r = requests.get(url)
    print("Body Response:")
    print("    - type: {}".format(type(r.text)))
    print("    - content: {}".format(r.text))
