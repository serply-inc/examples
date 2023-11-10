import requests

url = "https://api.serply.io/v1/scholar/q=machine+learning+research"

payload = ""
headers = {
    "User-Agent": "insomnia/8.4.0",
    "apikey": "YOU_API_KEY"
}

response = requests.request("GET", url, data=payload, headers=headers)

print(response.json()['html'])