import requests

endpoint1 = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint1, json={
			'title': 'None',
			'price':"samir"
			})

print(get_response.json())