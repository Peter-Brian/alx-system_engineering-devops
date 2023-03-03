#!/usr/bin/python3
"""reddit api"""
import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    response = requests.get(url)

    if response.status_code == 200:
        r = requests.get(url, headers=headers)
        json = r.json()
        if json:
            data = json.get("data")
            if data:
                subscribers = data.get("subscribers")
                return subscribers
            return 0
        return 0
    return 0
