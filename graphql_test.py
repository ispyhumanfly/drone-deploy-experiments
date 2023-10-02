#!python

"""Testing connecting to Drone Deploy GraphQL API"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://dronedeploy.com/graphql"

token = os.getenv("DRONE_DEPLOY_API_KEY")

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

