import requests


endpoint = "http://localhost:8000/products/create/"

#get_response = requests.get(endpoint)
'''
RetrieveAPIView
get_response = requests.get(endpoint)
print(get_response.json())
'''

'''CreateAPIView
get_response = requests.post(endpoint, json={"title": "CreateAPIView", "price": 123.00})
print(get_response.json())
'''

'''ListAPIView
get_response = requests.get(endpoint)
print(get_response.json())
'''

'''ListCreateAPIView'''
get_response = requests.post(endpoint, json={"title": "ListCreateAPIView", "price": 72.00})
print(get_response.json())