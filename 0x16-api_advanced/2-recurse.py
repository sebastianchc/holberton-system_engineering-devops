#!/usr/bin/python3
"""Request from Reddit API"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """All titles recursively"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}"
    url = url.format(subreddit, after)
    header = {"User-Agent": "Chrome"}
    all_posts = get(url, headers=header, allow_redirects=False).json()
    if all_posts.get("error") == 404:
        return None
    else:
        info = all_posts.get("data")
        posts = info.get("children")
        for post in posts:
            data = post.get("data")
            hot_list.append(data.get("title"))
        page = info.get("after")
        if page is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, page)
