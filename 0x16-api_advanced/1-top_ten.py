#!/usr/bin/python3
"""function"""
from webbrowser import get
import requests


def top_ten(r):
    """function"""
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10".format(r),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0
    mydic = req.json()
    i = 0
    for child in mydic.get("data").get("children"):
	    print(child.get("data").get("title"))
