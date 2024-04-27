#!/usr/bin/python3
"""Script that  takes in a letter and sends a POST request to
a URL with the letter as a parameter in the variable q. """

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post(url=url, data={"q": q})
    try:
        data = response.json()
        if data:
            (f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
