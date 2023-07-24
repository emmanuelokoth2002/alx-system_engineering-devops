#!/usr/bin/python3

"""
Module to fetch and export employee TODO list progress to JSON format.
"""

import requests
import sys
import json

def get_employee_data(employee_id):
    """
    Fetches employee data and TODO list progress based on the given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        tuple: A tuple containing employee name and a list of completed tasks.
    """
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        # Fetch employee information
        response = requests.get(user_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data['name']

        # Fetch employee's TODO list
        response = requests.get(todos_url)
        response.raise_for_status()
        todos_data = response.json()

        # Extract completed tasks
        completed_tasks = []
        for todo in todos_data:
            if todo['completed']:
                completed_tasks.append({"task": todo['title'], "completed": True, "username": employee_name})
            else:
                completed_tasks.append({"task": todo['title'], "completed": False, "username": employee_name})

        return employee_name, completed_tasks

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid data received from the API.")
        sys.exit(1)

def export_to_json(employee_id, employee_name, completed_tasks):
    """
    Exports employee TODO list progress to JSON format.

    Args:
        employee_id (int): The employee ID.
        employee_name (str): The name of the employee.
        completed_tasks (list): List of completed tasks.

    Returns:
        None
    """
    data = {str(employee_id): completed_tasks}
    filename = f"{employee_id}.json"
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks = get_employee_data(employee_id)
    export_to_json(employee_id, employee_name, completed_tasks)
