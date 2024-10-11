#!/usr/bin/python3
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(kale-francis, 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))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")

