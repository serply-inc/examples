import os
import urllib
import requests

API_KEY = os.environ.get("API_KEY")
# set the api key in headers
headers = {"apikey": API_KEY}

# format the query
# q: the search term
# hl: return results in English
query = {"q": "donuts in portland"}

# build to url to make request
url = f"https://api.serply.io/v1/maps/" + urllib.parse.urlencode(query)
print(url)

resp = requests.get(url, headers=headers)
results = resp.json()
print(results)

import csv

f = csv.writer(open("places.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["place", "description", "address", "website", "reviews"])

for entry in results["places"]:
    f.writerow([
        entry['place'], 
        entry['description'], 
        entry['address_string'],
        entry['website']["link"] if 'website' in entry else None,
        entry['reviews']["link"],
    ])