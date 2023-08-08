#!/usr/bin/python3
"""
Module to recursively query the Reddit API, parse hot article titles, and
print keyword counts.
"""

import requests


def count_words(subreddit, word_list, after=None):
    """
    Recursively queries the Reddit API, parses hot article titles, and prints
    a sorted count of keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The "after" parameter for pagination.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom User Agent"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if len(posts) == 0:
            sorted_words = sorted(word_list)
            for word in sorted_words:
                print(f"{word}: 0")
            return

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                keyword = word.lower()
                if f" {keyword} " in f" {title} ":
                    word_list[word] = word_list.get(word, 0) + 1

        after = data["data"]["after"]

        if after is None:
            sorted_words = sorted(word_list, key=lambda x: (-word_list[x], x))
            for word in sorted_words:
                print(f"{word}: {word_list[word]}")
        else:
            count_words(subreddit, word_list, after)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
    else:
        subreddit_name = sys.argv[1]
        keywords = sys.argv[2:]
        word_dict = {word: 0 for word in keywords}
        count_words(subreddit_name, word_dict)
