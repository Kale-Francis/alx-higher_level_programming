#!/usr/bin/python3
"""
Sends a POST request with an email to a URL and displays the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('utf-8')

    with urllib.request.urlopen(url, data) as response:
        response_body = response.read().decode('utf-8')
        print("Your email is:", email)
        print(response_body)
