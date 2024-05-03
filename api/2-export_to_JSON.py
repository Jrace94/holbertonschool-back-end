#!/usr/bin/python3
"""Module that exports a JSON file"""
import json
import requests
import sys

response_API = __import__("0-gather_data_from_an_API")

url = response_API.url


if __name__ == "__main__":
    dict_user = {}
    task_user = []
    data_user = {}

    todos, user = response_API.response(sys.argv[1])

    for todo in todos:
        data_user["task"] = todo["title"]
        data_user["completed"] = todo["completed"]
        data_user["username"] = user["username"]
        task_user.append(data_user)
        data_user = {}

    dict_user[str(sys.argv[1])] = task_user

    with open(f"{sys.argv[1]}.json", "w") as json_file:
        json.dump(dict_user, json_file)
