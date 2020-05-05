#!/usr/bin/python3
"""Request from API"""
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    req = get(url).json()
    print("Employee {} is done with tasks".format(req.get("name")), end="")
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(argv[1])
    tasks = get(url).json()
    complete = []
    for task in tasks:
        if task.get("completed"):
            complete.append(task)
    print("({}/{}):".format(len(complete), len(tasks)))
    for task in complete:
        print("\t {}".format(task.get("title")))
