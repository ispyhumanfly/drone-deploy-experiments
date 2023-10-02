#!python

"""Testing connecting to Drone Deploy GraphQL API"""

import requests
import json

endpoint = "https://dronedeploy.com/graphql"

token = "752d4602fe6441f6b4c5a91567a5e8c7"

query = """

query {
    viewer {
        login
    }
}
"""

response = requests.post(endpoint, json={'query': query}, headers={'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json'}, timeout=10)

if response.status_code == 200:
    print("We succeeded")
else:
    print(response.status_code)
    print(response.text)

