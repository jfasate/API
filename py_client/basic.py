import requests


#endpoint = "https://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

#get_response = requests.get(endpoint)
get_response = requests.post(endpoint, json={"title": "Hello World!", "price": "99.99"})
print(get_response.json())