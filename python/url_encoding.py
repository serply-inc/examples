import requests
from urllib.parse import urlencode, quote

# set the api key in headers
headers = {"apikey": "YOUR_API_KEY"}


def main():
    data = {
        "q": "site:linkedin.com/in john doe",
        "num": 10,
        "start": 20,
        "safe": "active",
    }
    query = urlencode(data)
    url = f"https://api.serply.io/v1/search/{query}"
    resp = requests.get(url, headers=headers)
    result = resp.json()
    print(result)


if __name__ == "__main__":
    main()
