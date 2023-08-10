import requests
import json

api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=API_KEY&base="

exchange_type = input("Exchange Type: ")
currency_received = input("Currency Received: ")
amount = int(input(f"How much money {exchange_type}: "))

result = requests.get(api_url + exchange_type)
result = json.loads(result.text)

print(f"1 {exchange_type} = {result['rates'][currency_received]} {currency_received}")
print(f"{amount} {exchange_type} = {amount * result['rates'][currency_received]} {currency_received}")