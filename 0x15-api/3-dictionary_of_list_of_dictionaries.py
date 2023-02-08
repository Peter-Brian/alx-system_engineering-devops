#!/usr/bin/python3
"""Gather data from API"""

from requests import get
from sys import argv, exit
import json

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    url_user = url + "users"
    url_todo = url + "todos"

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
        jsresult = {}
        user_names = {}
        for user in jsuser:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            jsresult[USER_ID] = []
            user_names[USER_ID] = USERNAME

        # create the value of the dict of the final json file
        # jslist = jsresult[USER_ID]
        for task in jstodo:
            TASK_TITLE = task.get('title')
            TASK_COMPLETED_STATUS = task.get('completed')
            # write the internal dict
            user_id = task.get("userId")
            taskdict = {"task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": user_names.get(user_id)}

            if jsresult.get(user_id) is not None:
                jsresult.get(user_id).append(taskdict)

        # generate the jsonfile
        with open('todo_all_employees.json', 'w', newline='') as jsonfile:
            json.dump(jsresult, jsonfile)
