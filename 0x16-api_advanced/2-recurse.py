#!/usr/bin/python3
""" recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], passed_after=""):
    """ returns title of 10 hot posts """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {"user-agent": "me"}
    after = passed_after
    params = {"after": after}
    data = requests.get(url, headers=headers, params=params)
    if data.status_code == 404:
        return None
    data = data.json()
    try:
        for item in data['data']['children']:
            hot_list.append(item['data']['title'])
        passed_after = data['data']['after']
        if passed_after == "":
            return hot_list
        else:
            recurse(subreddit, hot_list, passed_after)
            return hot_list
    except Exception:
        return None
