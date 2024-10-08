#!/usr/bin/python3
"""
Fetches the X-Request-Id value from the response header of a URL.
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
