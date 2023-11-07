#!/usr/bin/python3
""" title of 10 hot posts """
import requests


def top_ten(subreddit):
    """ returns title of 10 hot posts """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {"user-agent": "me"}
    data = requests.get(url, headers=headers)
    if data.status_code == 404:
        print(None)
        return
    data = data.json()
    length = len(data['data']['children'])
    if length > 10:
        length = 10
    for i in range(length):
        print(data['data']['children'][i]['data']['title'])
    return
