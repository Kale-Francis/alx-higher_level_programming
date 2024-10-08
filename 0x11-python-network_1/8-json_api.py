#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    letter = "" if len(sys.argv) < 2 else sys.argv[1]
    payload = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
