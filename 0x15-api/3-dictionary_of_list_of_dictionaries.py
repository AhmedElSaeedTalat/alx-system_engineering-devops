#!/usr/bin/python3
""" script that uses API to get info about given empliyee """
import json
import requests


if __name__ == "__main__":
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    """ user data request """
    usr_res = requests.get(users_url)
    usr_res = usr_res.json()
    """ todos request """
    tdo_res = requests.get(todos_url)
    tdo_res = tdo_res.json()
    """ file to insert into """
    file_name = "todo_all_employees.json"
    list_obects = []
    usr_name = ""
    id = ""
    employees_dict = {}
    for task in tdo_res:
        if usr_name and id == task['userId']:
            list_obects.append({'username': usr_name,
                                'task': task['title'],
                                'completed': task['completed']})
        else:
            if usr_name and id != task['userId']:
                employees_dict[id] = list_obects
                list_obects = []
            for usr in usr_res:
                if task['userId'] == usr['id']:
                    usr_name = usr['username']
                    id = usr['id']
                    break
            list_obects.append({'username': usr_name,
                                'task': task['title'],
                                'completed': task['completed']})
    list_obects.append({'username': usr_name,
                        'task': task['title'],
                        'completed': task['completed']})
    employees_dict[id] = list_obects
    with open(file_name, 'w') as f:
        json.dump(employees_dict, f)
