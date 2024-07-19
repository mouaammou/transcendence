import requests

endpoint1 = "http://127.0.0.1:8000/api/"
endpoint2 = "http://localhost:8000/api/products/"

# get_response = requests.post(endpoint1, json={
# 			'title': 'None',
# 			'price':"samir"
# 			})

data = {
	'title':'casc bleuthouth',
	'content':None
}

get_response = requests.post(endpoint2, json=data)

print(get_response.json())