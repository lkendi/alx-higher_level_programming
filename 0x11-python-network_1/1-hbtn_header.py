#!/usr/bin/python3
"""Script that sends a request to a URL and displays
the value of 'X-Request-Id' variable found in the
response header"""

import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
