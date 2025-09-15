import requests


endpoint = "http://localhost:8000/products/list-create/"

#get_response = requests.get(endpoint)

'''RetrieveAPIView
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
get_response = requests.post(endpoint, json={"title": "ListCreateAPIView", "price": 72.00, "sale_price": 65.00})
print(get_response.json())


'''UpdateAPIView
data = {"title": "UpdateAPIView",}
get_response = requests.put(endpoint, json=data)
print(get_response.json())
'''

'''DestroyAPIView
product_id = int(input("Enter product id to delete: "))

if not product_id:
    print("Please provide a valid product id")
    exit()
else:
    endpoint = f"http://localhost:8000/products/{product_id}/delete/"
    get_response = requests.delete(endpoint)
    print(get_response.status_code)
'''
