import os
import urllib
import requests

API_KEY = os.environ.get("API_KEY")
# set the api key in headers
headers = {"apikey": API_KEY}

# format the query
# q: the search term
# hl: return results in English
query = {"q": "best bike trail"}

# build to url to make request
url = f"https://api.serply.io/v1/image/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()

import csv

f = csv.writer(open("images.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["src", "title", "href"])

for result in results["image_results"]:
    f.writerow([
        result['image']['src'], 
        result['link']['title'], 
        result['link']['href']
    ])