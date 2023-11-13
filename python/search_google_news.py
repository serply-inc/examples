import os
import urllib
import requests

API_KEY = os.environ.get("API_KEY")
# set the api key in headers
headers = {"apikey": API_KEY}

# format the query
# q: the search term
# hl: return results in English
query = {"q": "global markets"}

# build to url to make request
url = f"https://api.serply.io/v1/news/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()

print(results)