# Ask the user for a word to search
# Load synonyms from Datamuse API
# https://api.datamuse.com/words?ml=

import requests

search = input("What word to lookup? ")
url = "https://api.datamuse.com/words?ml=" + search

response = requests.get(url)
print(response)

if response:
    print(response.text)
else:
    print("Could not connect successfully.")