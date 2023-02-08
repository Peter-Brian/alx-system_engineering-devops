#!/usr/bin/python3
"""Gather data from API"""

from requests import get
from sys import argv, exit
import csv

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
        USER_ID = id
        USERNAME = jsuser[0].get('username')

        # export data in the CSV format
        with open(id + '.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',',
                                   quotechar='"', quoting=csv.QUOTE_ALL)
            for task in jstodo:
                TASK_COMPLETED_STATUS = task.get('completed')
                TASK_TITLE = task.get('title')
                csvwriter.writerow([USER_ID,
                                    USERNAME,
                                    TASK_COMPLETED_STATUS,
                                    TASK_TITLE])
