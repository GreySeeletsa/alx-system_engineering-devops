#!/usr/bin/python3
"""fetches info and exports it in json format
"""
import json
import requests
import sys


base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":

    user_id = sys.argv[1]

    # get user info from https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # To get info from api
    response = requests.get(user_url)
    data = response.text
    data = json.loads(data)
    user_name = data[0].get('username')

    # To get user info about todo tasks
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # To get info from api
    response = requests.get(tasks_url)
    tasks = response.text
    tasks = json.loads(tasks)

    dict_key = str(user_id)

    # To handle the build of json
    builder = {dict_key: []}
    for task in tasks:
        json_data = {
            "task": task['title'],  # or use get method
            "completed": task['completed'],
            "username": user_name
        }
        builder[dict_key].append(json_data)
    json_encoded_data = json.dumps(builder)
    with open('{}.json'.format(user_id), 'w', encoding='UTF8') as myFile:
        myFile.write(json_encoded_data)
