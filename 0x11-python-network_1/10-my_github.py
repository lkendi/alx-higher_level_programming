#!/usr/bin/python3
"""Script that takes your GitHub credentials and uses
the GitHub API to display your id"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    auth = (username, pwd)
    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        print(data['id'])
    else:
        print("None")
