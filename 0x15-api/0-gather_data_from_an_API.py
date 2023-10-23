#!/usr/bin/python3
"""script that fetches info about a given employee's ID"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # Will get info from api
    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    name = data[0].get('name')

    # Will get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # Will get info from api
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    # init completed count as 0 and find total num of tasks
    completed = 0
    total_tasks = len(tasks)

    # init empty list for completed tasks
    completed_tasks = []
    for task in tasks:

        if task.get('completed'):
            # To print("The tasks are: {}\n".format(task))
            completed_tasks.append(task)
            completed += 1

    # Will print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
