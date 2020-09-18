import urllib
import requests

# set the api key in headers
headers = {
    "apikey": "YOUR_API_KEY"
}

# format the query
# q: the search term
# hl: return results in English
query = {
    "q": "best bike trail",
    "hl": "en"
}

# build to url to make request
url = f"https://api.goog.io/v1/search/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(results)
