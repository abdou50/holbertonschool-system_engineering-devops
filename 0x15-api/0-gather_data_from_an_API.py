#!/usr/bin/python3
"""api"""

import requests
from sys import argv

if __name__ == "__main__":
    """api"""
    list = []
    req1 = requests.get('https://jsonplaceholder.typicode.com/todos')
    req2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1]))
    req1 = req1.json()
    req2 = req2.json()
    al = 0
    done = 0
    for i in req1:
        if (((i["userId"]) == int(argv[1]))):
            al += 1
            if (i["completed"]):
                done += 1
                list = list + [(i["title"])]
    print("Employee {} is done with tasks({}/{}):".format(
        req2["name"], done, al))
    for i in list:
        print("\t", i)
