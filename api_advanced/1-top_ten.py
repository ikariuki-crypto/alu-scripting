#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Prints the top 10 hot post titles, or None if invalid."""
    hosts = ["https://www.reddit.com/r/{}/hot.json",
             "https://www.reddit.com/r/{}.json",
             "https://api.reddit.com/r/{}/hot",
             "https://old.reddit.com/r/{}/hot.json",
             "https://www.reddit.com/r/{}/hot/.json"]
    agents = ["linux:alu.api_advanced:v1.0 (by /u/ikariuki)",
              "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"]
    for host in hosts:
        for agent in agents:
            r = requests.get(host.format(subreddit),
                             headers={"User-Agent": agent},
                             params={"limit": 10}, allow_redirects=False)
            print(host[8:20], agent[:7], r.status_code)
