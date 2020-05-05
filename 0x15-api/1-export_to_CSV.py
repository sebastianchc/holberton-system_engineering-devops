#!/usr/bin/python3
"""Request from API"""
from csv import writer, QUOTE_ALL
from requests import get
from sys import argv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = get(url).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"
    url = url.format(argv[1])
    tasks = get(url).json()
    info_user = []
    for task in tasks:
        info_user.append([argv[1],
                          user.get("username"),
                          task.get("completed"),
                          task.get("title")])
    with open("{}.csv".format(argv[1]), "w") as csv_file:
        writer = writer(csv_file, quoting=QUOTE_ALL)
        writer.writerows(info_user)
