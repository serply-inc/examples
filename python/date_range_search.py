import urllib
import requests

# set the api key in headers
headers = {
    "apikey": "YOUR_API_KEY"
}

# format the query
# q: the search term
# hl: return results in English
# tbs: parameter to specify time ( https://illusioncity.net/pcweb-google-operators/ )
query = {
    "q": "elon musk",
    "hl": "en",
    "tbs": "cdr:1,cd_min:01/01/2013,cd_max:12/31/2013"
}

# build to url to make request
url = f"https://api.goog.io/v1/search/" + urllib.parse.urlencode(query)
print(url)

resp = requests.get(url, headers=headers)
results = resp.json()
print(results)
