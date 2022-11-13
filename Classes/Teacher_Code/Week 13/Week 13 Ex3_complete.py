# Use requests to load the API page
# Parse JSON to find the latitude and longitude
# Print the current position
# http://api.open-notify.org/iss-now.json

import requests
import json

response = requests.get("http://api.open-notify.org/iss-now.json")

if response:
    data = json.loads(response.text)
    print(json.dumps(data, indent = 4))
    lat = data["iss_position"]["latitude"]
    long = data["iss_position"]["longitude"]
    print("Latitude:", lat)
    print("Longitude:", long)
    
else:
    print("Sorry, could not connect.")