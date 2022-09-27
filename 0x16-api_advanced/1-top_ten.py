#!/usr/bin/python3
"""function"""
import requests


def top_ten(r):
    """function"""
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(r),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if req.status_code >= 300:
        print('None')

    else:
        mydic = req.json()
        for child in mydic.get("data").get("children"):
            print(child.get("data").get("title"))
