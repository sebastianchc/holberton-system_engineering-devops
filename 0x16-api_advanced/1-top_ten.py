#!/usr/bin/python3
"""Request from Reddit API"""
from requests import get


def top_ten(subreddit):
    """Top 10 hot posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {"User-Agent": "Chrome"}
    hot_posts = get(url, headers=header, allow_redirects=False).json()
    if hot_posts.get("error") == 404:
        print(None)
    else:
        info = hot_posts.get("data")
        posts = info.get("children")
        for post in posts[:10]:
            data = post.get("data")
            print(data.get("title"))
