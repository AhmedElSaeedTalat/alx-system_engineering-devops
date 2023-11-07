#!/usr/bin/python3
""" script to make an api request """
import requests


def number_of_subscribers(subreddit):
    """ return number of subscribers """
    url = 'https://www.reddit.com/r/' + subreddit + '.json'
    headers = {"user-agent": "me"}
    data = requests.get(url, headers=headers)
    data = data.json()
    try:
        return data['data']['children'][1]['data']['subreddit_subscribers']
    except Exception:
        return 0
