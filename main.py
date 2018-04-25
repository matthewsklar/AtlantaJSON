import urllib.request as request
import json

response = json.loads((request
                       .urlopen("https://api.wunderground.com/api/43b25c75d7f17987/conditions/q/GA/Atlanta.json")
                       .read()
                       .decode("utf-8")))

with open('atlanta.json', 'w') as file:
    json.dump(response, file, indent=4)
