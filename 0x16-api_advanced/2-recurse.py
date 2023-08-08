#!/usr/bin/python3
"""
Module to recursively query the Reddit API and return a list containing the
titles of all hot articles for a subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the
    titles of all hot articles for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The "after" parameter for pagination.
        
    Returns:
        list: A list containing the titles of all hot articles. If no results
        are found, returns None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100, "after": after}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        
        if len(posts) == 0:
            return hot_list
        
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)
        
        after = data["data"]["after"]
        
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        result = recurse(subreddit_name)
        if result is not None:
            print(len(result))
        else:
            print("None")
