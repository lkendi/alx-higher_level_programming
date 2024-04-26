#!/usr/bin/python3
"""Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    with urllib.request.urlopen(url, data=email.encode('utf-8')) as response:
        body = response.read().decode('utf-8')
        print(body)
