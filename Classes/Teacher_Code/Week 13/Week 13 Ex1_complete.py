# Use requests to load current information on SDSU basketball
# https://dgoldberg.sdsu.edu/315/sdsu_basketball.txt

import requests

response = requests.get("https://dgoldberg.sdsu.edu/315/sdsu_basketball.txt")
print(response)
print(response.status_code)

if response:
    print(response.text)
else:
    print("Sorry, could not connect.")