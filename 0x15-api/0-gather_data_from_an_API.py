#!/usr/bin/python3
"""Gather data from API"""

from requests import get
from sys import argv, exit

if __name__ == "__main__":
    try:
        id = argv[1]
        is_integer = int(id)
    except Exception:
        exit()

    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users?id=" + id
    url_todo = url + "todos?userId=" + id

    request_user = get(url_user)
    request_todo = get(url_todo)
    # Connection and have an access to the json
    try:
        jsuser = request_user.json()
        jstodo = request_todo.json()
    except ValueError:
        print("No Json")

    # Assign values
    if jsuser and jstodo:
        EMPLOYEE_NAME = jsuser[0].get('name')
        NUMBER_OF_DONE_TASKS = 0
        for task in jstodo:
            if task.get('completed'):
                NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS = len(jstodo)

        # Print first line
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))

        # Second and N lines
        for doing in jstodo:
            TASK_TITLE = doing.get('title')
            if doing.get('completed'):
                print("\t {}".format(TASK_TITLE))
