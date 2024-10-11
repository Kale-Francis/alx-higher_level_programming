#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    
    # Send a GET request to the GitHub API to retrieve the commits
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:  # Get only the first 10 commits
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print(f"Error: {response.status_code}")
