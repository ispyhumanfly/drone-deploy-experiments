#!python

"""Testing connecting to Drone Deploy GraphQL API"""
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

graphql_query = """

{
  projects {
    edges {
      node {
        location {
          lat
          lng
        }
        name
        plans {
          edges {
            node {
              id
              name
              ... on MapPlanTemplate {
                id
                name
                geometry {
                  lat
                  lng
                }
              }
            }
          }
        }
      }
    }
  }
  viewer {
    id
  }
}
"""

response = requests.post(url="https://api.dronedeploy.com/graphql", json={"query": graphql_query}, headers={'Authorization': 'Bearer ' + os.getenv("DRONE_DEPLOY_API_KEY"), 'Content-Type': 'application/json'}, timeout=10)

if response.status_code == 200:
    print("We succeeded")
    print(response.text)
else:
    print(response.status_code)
    print(response.text)

