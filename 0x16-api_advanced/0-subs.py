#!/usr/bin/python3
"""Request from Reddit API"""
from requests import get


def number_of_subscribers(subreddit):
    """Number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "Chrome"}
    subreddit = get(url, headers=header, allow_redirects=False).json()
    if subreddit.get("error") == 404:
        return 0
    else:
        data = subreddit.get("data")
        return data.get("subscribers")
