import requests

endpoint1 = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint1)

print(get_response.json())