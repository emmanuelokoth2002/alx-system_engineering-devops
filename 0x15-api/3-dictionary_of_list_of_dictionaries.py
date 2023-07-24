#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url_users = 'https://jsonplaceholder.typicode.com/users'
    url_todos = 'https://jsonplaceholder.typicode.com/todos'

    response_users = requests.get(url_users)
    response_todos = requests.get(url_todos)

    if response_users.status_code == 200 and response_todos.status_code == 200:
        users = response_users.json()
        todos = response_todos.json()

        todo_dict = {}
        for user in users:
            user_id = str(user.get('id'))
            username = user.get('username')
            todo_dict[user_id] = []
            for task in todos:
                if task.get('userId') == int(user_id):
                    task_dict = {
                        "username": username,
                        "task": task.get('title'),
                        "completed": task.get('completed'),
                    }
                    todo_dict[user_id].append(task_dict)

        with open('todo_all_employees.json', 'w') as json_file:
            json.dump(todo_dict, json_file)

    else:
        print("Error: Could not fetch data.")
