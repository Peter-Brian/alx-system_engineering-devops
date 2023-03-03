#!/usr/bin/python3
"""Top ten"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Return a list of titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'MyAPI/0.0.1'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json().get("data")
            after = data.get("after", None)
            children = data.get("children", None)
            for each in children:
                hot_list.append(each.get("data").get("title", None))
        except Exception as e:
            return None
    else:
        return None

    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list

    return recurse(subreddit, hot_list, after)
