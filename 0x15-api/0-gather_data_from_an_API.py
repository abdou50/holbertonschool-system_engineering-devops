#!/usr/bin/python3
"""api"""
import requests
from sys import argv

if __name__ == "__main__":
    """api"""


req1 = requests.get('https://jsonplaceholder.typicode.com//todos')
req2 = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(argv[1]))
jj = req1.json()
jk = req2.json()
list = []
todo = 0
complited = 0
for i in jj:
    if (((i["userId"]) == int(argv[1]))):
        todo += 1
        if (i["completed"]):
            y += 1
            list = list + [(i["title"])]
print("Employee {} is done with tasks({}/{}):".format(
    jk["name"], complited, todo))
for i in list:
    print("\t", i)
