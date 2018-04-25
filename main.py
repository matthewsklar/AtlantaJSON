import requests
import json

response = requests.get("https://api.wunderground.com/api/43b25c75d7f17987/conditions/q/GA/Atlanta.json").json()

with open('atlanta.json', 'w') as file:
    json.dump(response, file, indent=4)
