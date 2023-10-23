#!/usr/bin/python3
""" script that uses API to get info about given empliyee """
import requests
import sys
import csv


if __name__ == "__main__":
    employee_id = sys.argv[1]
    users_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    """ user data request """
    usr_res = requests.get(users_url)
    usr_res = usr_res.json()
    usr = usr_res['username']
    """ todos request """
    tdo_res = requests.get(todos_url)
    tdo_res = tdo_res.json()
    file_name = employee_id + ".csv"
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        for task in tdo_res:
            if task['userId'] == int(employee_id):
                writer.writerow([task['userId'], usr, task['completed'],
                                task['title']])
