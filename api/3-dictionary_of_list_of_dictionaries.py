#!/usr/bin/python3
"""Module that exports a JSON file"""
import json
import requests
import sys

response_API = __import__("0-gather_data_from_an_API")

url = response_API.url


if __name__ == "__main__":
    dict_user = {}
    tasks = []
    i = 0
    j = 20

    reponse_todos = requests.get(f"{url}/todos")
    response_users = requests.get(f"{url}/users")

    todos = reponse_todos.json()
    users = response_users.json()

    for user in users:
        for todo in todos[i:j]:
            tasks_user = {
                "username": user["username"],
                "task": todo["title"],
                "completed": todo["completed"],
            }
            tasks.append(tasks_user)
            tasks_user = {}
        i += 20
        j += 20
        dict_user[user["id"]] = tasks
        tasks = []

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(dict_user, json_file)
