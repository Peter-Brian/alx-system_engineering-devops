#!/usr/bin/python3
"""
    that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress
"""


import json
import requests
import sys

domain_name = "https://jsonplaceholder.typicode.com"


def is_valid_json(data) -> bool:
    """
        check if a data is a json
    """
    try:
        data.json()
        return True
    except Exception:
        return False


def get_employee_information(employee_id: int):
    """
        get employee informations
    """
    try:
        response = requests.get(
            url="{}/users/{}/".format(domain_name, employee_id))

        if not is_valid_json(response):
            raise ValueError("Not a valid JSON")

        content = response.json()

        if len(content) == 0:
            raise ValueError("No result")

        return content

    except Exception as exception:
        print(exception.args[0])


def get_employee_tasks(employee_id):
    """
        get employee task list
    """
    try:
        response = requests.get(
            url="{}/users/{}/todos".format(domain_name, employee_id))

        if not is_valid_json(response):
            raise ValueError("Not a valid JSON")

        content = response.json()

        if len(content) == 0:
            raise ValueError("No result")

        return content

    except Exception as exception:
        print(exception.args[0])


def get_employee_completed_tasks(task_list: json):
    """
        get employee completed task list
    """
    return [x for x in task_list if x['completed'] is True]


def print_employee_completed_tasks(employee_id: int):
    """
        print employee completed task list
    """
    employee_infos = get_employee_information(sys.argv[1])
    employee_tasks = get_employee_tasks(sys.argv[1])
    employee_completed_tasks = get_employee_completed_tasks(employee_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_infos.get("name"),
        len(employee_completed_tasks),
        len(employee_tasks))
    )
    for task in employee_completed_tasks:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("Usage 0-gather_data_from_an_API.py <USERID>")

    print_employee_completed_tasks(sys.argv[1])


