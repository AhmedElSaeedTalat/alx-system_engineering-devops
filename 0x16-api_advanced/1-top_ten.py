#!/usr/bin/python3
""" title of 10 hot posts """
import requests


def top_ten(subreddit):
    """ returns title of 10 hot posts """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {"user-agent": "me"}
    params = {"limit": 10}
    data = requests.get(url, headers=headers, params=params)
    if data.status_code == 404:
        print(None)
        return
    data = data.json()
    try:
        for item in data['data']['children']:
            print(item['data']['title'])
        return
    except Exception:
        print('None')
        return
