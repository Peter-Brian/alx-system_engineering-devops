#!/usr/bin/python3
"""Top ten"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data")
            children = data.get("children")
            for each in children[:10]:
                print(each.get("data").get("title"))
        except Exception as e:
            print(None)
    else:
        print(None)
