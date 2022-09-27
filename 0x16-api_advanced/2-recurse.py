#!/usr/bin/python3
"""function"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """function"""
    data = requests.get("https://www.reddit.com/r/"
                        "{}/hot.json?limit=100&after={}"
                        .format(subreddit, after),
                        headers={"User-Agent": "My-User-Agent"},
                        allow_redirects=False)
    if data.status_code != 200:
        return None
    else:
        dic_data = data.json()
        if len(dic_data.get("data").get("children")) == 0:
            return hot_list
        else:
            for child in dic_data.get("data").get("children"):
                hot_list.append(child.get("data").get("title"))
            after = dic_data.get("data").get("after")
            if after is None:
                return hot_list
            return recurse(subreddit, hot_list, after=after)
