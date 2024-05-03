#!usr/bin/python3
"""Module to interact with an API"""
import requests
import sys

done_tasks = []
url = "https://jsonplaceholder.typicode.com"

response_todos = requests.get(f"{url}/todos?userid={sys.argv[1]}")
response_users = requests.get(f"{url}/users/{sys.argv[1]}")

todos = response_todos.json()
user = response_users.json()

for todo in todos:
    if todo.get("completed"):
        done_tasks.append(todo)

name = user.get("name")
tasks = len(done_tasks)
print(f"Employee {name} is done with tasks({tasks}/{len(todos)}):")

for todo in done_tasks:
    print(f"\t {todo.get("title")}")
