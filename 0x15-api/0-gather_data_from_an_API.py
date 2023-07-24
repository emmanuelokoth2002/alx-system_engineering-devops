#!/usr/bin/python3

"""
Module to fetch and display employee TODO list progress from a REST API.
"""
import requests
import sys


def get_employee_data(employee_id):
    """
    Fetches employee data and TODO list progress based on given employee ID.

    Args:
        employee_id (int): The employee ID.

    Returns:
        None
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

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Display progress
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}): ")
        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Invalid data received from the API.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: ./gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)
