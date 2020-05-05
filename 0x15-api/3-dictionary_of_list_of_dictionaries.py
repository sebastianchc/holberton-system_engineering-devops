#!/usr/bin/python3
"""Request from API"""
from json import dump
from requests import get


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    users = get(url).json()
    all_u = {}
    for user in users:
        all_u[user.get("id")] = []
        url = "https://jsonplaceholder.typicode.com/todos?userId={}"
        url = url.format(user.get("id"))
        tasks = get(url).json()
        for task in tasks:
            all_u[user.get("id")].append({"username": user.get("username"),
                                          "task": task.get("title"),
                                          "completed": task.get("completed")})
    with open("todo_all_employees.json", "w") as json_file:
        dump(all_u, json_file)
