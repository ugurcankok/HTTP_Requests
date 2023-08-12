import requests

url = "http://api.weatherapi.com/v1/current.json"
access_key = "<api_key>"

city = input("city: ")

response = requests.get(url, params= {
    "key": access_key,
    "q": city,
    "lang": "tr"
})

result = response.json()

city = result["location"]["name"]
weather_condition = result["current"]["temp_c"]
text = result["current"]["condition"]["text"]

print(f"{city}, {weather_condition} centigrade and {text}.")