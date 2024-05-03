#!usr/bin/python3
"""Module to interact with an API"""
import requests
import sys

done_taks = []
url = "https://jsonplaceholder.typicode.com"

response_todos = requests.get(f"{url}/todos?userid={sys.argv[1]}")
response_users = requests.get(f"{url}/users/{sys.argv[1]}")

todos = response_todos.json()
user = response_users.json()

for todo in todos:
    if todo.get("completed"):
        done_taks.append(todo)

print(
    f"Employee {user["name"]} is done with tasks({len(done_taks)}/{len(todos)}):",
)

for todo in done_taks:
    print(f"\t {todo.get("title")}")
