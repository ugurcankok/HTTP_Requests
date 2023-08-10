import requests

headlines_url = "https://newsapi.org/v2/top-headlines"
everything_url = "https://newsapi.org/v2/everything"

api_key = "<api_key>"

# response = requests.get(headlines_url, params={
#     "apiKey": api_key,
#     "country": "tr"
# })

response = requests.get(everything_url, params={
    "apiKey": api_key,
    "q": "futbol",
    "language": "tr",
    "sortBy": "publishedAt"
})

news = response.json()["articles"]

for new in news:
    print(new["source"]["name"])
    print(new["title"])
    print(new["url"])