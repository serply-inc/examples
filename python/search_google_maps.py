import os
import urllib
import requests

API_KEY = os.environ.get("API_KEY")
# set the api key in headers
headers = {"apikey": API_KEY}

# format the query
# q: the search term
# hl: return results in English
query = {"q": "coffee and donuts in portlan"}

# build to url to make request
url = f"https://api.serply.io/v1/maps/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(url)

import csv

f = csv.writer(open("places.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["place", "description", "address", "website", "reviews"])

for entry in results["places"]:
    f.writerow([
        entry['place'], 
        entry['description'], 
        entry['address'],
        entry['website']["url"] if entry['website'] else None,
        entry['reviews']["link"],
    ])