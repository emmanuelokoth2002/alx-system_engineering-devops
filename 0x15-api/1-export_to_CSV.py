#!/usr/bin/python3

"""
Module to fetch and export employee TODO list progress to CSV format.
"""

import requests
import sys
import csv


def get_employee_data(employee_id):
    """
    Fetches employee data and TODO list progress based on given employee ID.

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
                completed_tasks.append(todo['title'])

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


def export_to_csv(employee_id, employee_name, completed_tasks):
    """
    Exports employee TODO list progress to CSV format.

    Args:
        employee_id (int): The employee ID.
        employee_name (str): The name of the employee.
        completed_tasks (list): List of completed tasks.

    Returns:
        None
    """
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in completed_tasks:
            csv_writer.writerow([employee_id, employee_name, "True", task])
        # Include entries for tasks not completed as well (False status)
        total_tasks = len(completed_tasks)
        for _ in range(total_tasks, 20):
            csv_writer.writerow([employee_id, employee_name, "False", ""])

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks = get_employee_data(employee_id)
    export_to_csv(employee_id, employee_name, completed_tasks)
