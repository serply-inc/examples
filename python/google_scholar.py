import os

import requests
from bs4 import BeautifulSoup

API_KEY = os.environ.get("API_KEY")

url = "https://api.serply.io/v1/scholar/q=machine+learning+research"

headers = {
    "User-Agent": "insomnia/8.4.0",
    "apikey": API_KEY
}

response = requests.get(url, headers=headers)

html = response.json()['html']

soup = BeautifulSoup(html, "html.parser")

cite_results = []

for result in soup.find_all("div", {"class": "gs_ri"}):
    header = result.find("h3")
    link = header.find("a").get("href")
    citation = result.find("div", {"class": "gs_a"}).find("a").get("href")
    cite_results.append({
        "title": header.text,
        "link": link,
        "citation": citation
    })

print(cite_results)