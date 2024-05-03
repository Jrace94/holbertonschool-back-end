#!/usr/bin/python3
"""Module that exports a CSV file"""
import csv
import sys

response_API = __import__("0-gather_data_from_an_API")

url = response_API.url


if __name__ == "__main__":
    todos, user = response_API.response(sys.argv[1])

    with open("USER_ID.csv", "w") as USER_ID:
        user_writer = csv.writer(
            USER_ID,
            delimiter=",",
            quoting=csv.QUOTE_ALL,
        )
        for todo in todos:
            user_writer.writerow(
                [
                    todo["userId"],
                    user["name"],
                    todo["completed"],
                    todo["title"],
                ]
            )
