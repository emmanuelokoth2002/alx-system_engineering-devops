#!/usr/bin/python3

"""
Module to fetch and export employee TODO list progress to JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, user_id)).json()
    tasks = requests.get("{}users/{}/todos".format(url, user_id)).json()
    data_dict = {
                user_id: [{"task": task.get("title"),
                           "completed": task.get("completed"),
                           "username": user.get("username")} for task in tasks]
            }
    with open("{}.json".format(user_id), "w", newline="") as file:
        json.dump(data_dict, file)
