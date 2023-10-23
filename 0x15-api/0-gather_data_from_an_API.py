#!/usr/bin/python3
""" script that uses API to get info about given empliyee """
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'

    """ user data request """
    usr_res = requests.get(users_url)
    usr_res = usr_res.json()
    usr = usr_res['name']
    """ todos request """
    tdo_res = requests.get(todos_url)
    tdo_res = tdo_res.json()
    completed = 0
    non_completed = 0
    titles_completed = []
    for task in tdo_res:
        if task['userId'] == int(employee_id):
            if task['completed'] is True:
                completed = completed + 1
                titles_completed.append(task['title'])
            else:
                non_completed = non_completed + 1
    total_tasks = completed + non_completed
    statement = f'Employee {usr} is done with tasks({completed}/\
{total_tasks}):'
    print(statement)
    for title in titles_completed:
        print('\t', title)
