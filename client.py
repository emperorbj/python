import requests

url = "http://127.0.0.1:8000/customers"

response = requests.get(url)
data = response.json()
print(data)