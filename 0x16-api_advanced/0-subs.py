#!/usr/bin/python3
import requests


def number_of_subscribers(r):

    req = requests.get("https://www.reddit.com/r/{}/about.json".format(r),
                       headers={"User-Agent": "My-User-Agent"},
                       allow_redirects=False)
    if req.status_code >= 300:
        return 0
    mydic = req.json()
    return mydic["data"]["subscribers"]
