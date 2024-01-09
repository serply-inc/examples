import os
import urllib
import requests

# set the api key in headers
headers = {"apikey": os.environ["API_KEY"]}

# format the query
# q: the search term
# hl: return results in English
query = {"q": "best bike trail", "hl": "en"}

# build to url to make request
url = f"https://api.serply.io/v1/crawl/" + urllib.parse.urlencode(query)

resp = requests.get(url, headers=headers)
results = resp.json()
print(results)

with open("crawl.html", "wt") as fp:
    fp.write(results['html'])