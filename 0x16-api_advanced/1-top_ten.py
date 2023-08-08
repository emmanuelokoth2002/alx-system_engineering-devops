#!/usr/bin/python3
"""
Module to query the Reddit API and print the titles of the first 10 hot posts for a subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(None)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
