import requests

id = input()

endpoint2 = "http://localhost:8000/api/products/"+id+"/detail"

# get_response = requests.post(endpoint1, json={
# 			'title': 'None',
# 			'price':"samir"
# 			})

data = {
	'title':'casc bleuthouth',
	'content':None
}

get_response = requests.get(endpoint2)

print(get_response.json())