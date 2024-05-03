#!/usr/bin/python3
"""Module to interact with an API"""
import requests
import sys

url = "https://jsonplaceholder.typicode.com"


def response(arg):
    """Return todos and user"""
    response_todos = requests.get(f"{url}/todos?userId={arg}")
    response_users = requests.get(f"{url}/users/{arg}")

    todos = response_todos.json()
    user = response_users.json()

    return todos, user


if __name__ == "__main__":
    todos, user = response(sys.argv[1])
    done_tasks = []

    for todo in todos:
        if todo.get("completed"):
            done_tasks.append(todo)

    name = user.get("name")
    tasks = len(done_tasks)

    print(f"Employee {name} is done with tasks({tasks}/{len(todos)}):")

    for todo in done_tasks:
        print("\t {}".format(todo.get("title")))
