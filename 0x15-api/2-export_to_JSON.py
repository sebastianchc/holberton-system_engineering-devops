#!/usr/bin/python3
"""Request from API"""
from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(argv[1])
    tasks = get(url).json()
    info_user = {argv[1]: []}
    for task in tasks:
        info_user[argv[1]].append({"task": task.get("title"),
                                   "completed": task.get("completed"),
                                   "username": user.get("username")})
    with open("{}.json".format(argv[1]), "w") as json_file:
        dump(info_user, json_file)
