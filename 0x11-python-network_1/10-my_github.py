#!/usr/bin/python3
"""Script that takes your GitHub credentials and uses
the GitHub API to display your id"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    pwd = sys.argv[2]
    url = f"https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, pwd))
    data = response.json()
    print(data.get('id'))
