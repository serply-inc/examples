import os
import urllib
import requests

API_KEY = os.environ.get("API_KEY")

# set the api key in headers
headers = {"apikey": API_KEY}

# get back 100 results
# q: the search term
# hl: return results in English
# num: how many results to return (default 10, max 100)
query = {
    "q": "smart phone", 
    "hl": "en", 
    "num": 100
}

# build to url to make request
url = f"https://api.serply.io/v1/search/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(f"First 100 results: {results}")


# getting results 200-300 results
# q: the search term
# hl: return results in English
# num: how many results to return (default 10, max 100)
# start: which 
query = {
    "q": "smart phone", 
    "hl": "en", 
    "num": 100,
    "start": 200
}

# build to url to make request
url = f"https://api.serply.io/v1/search/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(f"Next 100 results: {results}")



# Getting local results from France
# q: the search term
# hl: return results in French
# lr: what language to return results
# cr: country 

# check out https://webapps.stackexchange.com/questions/16047/how-to-restrict-a-google-search-to-results-of-a-specific-language for language settings
query = {
    "q": "smart phone",
    "hl": "fr",
    "lr": "lang_fr",
    "cr": "countryFR"
}

# build to url to make request
url = f"https://api.serply.io/v1/search/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(f"Next 100 results: {results}")

# use the proxy location
headers["X-Proxy-Location"] = "FR"

# build to url to make request
url = f"https://api.serply.io/v1/search/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(f"Next 100 results: {results}")

import csv

f = csv.writer(open("locals.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["title", "description", "link"])

for result in results["results"]:
    f.writerow([
        result['title'], 
        result['description'], 
        result['link']
    ])