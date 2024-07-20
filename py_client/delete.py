import requests

id = input()

endpoint2 = f"http://localhost:8000/api/products/{id}"

data = {
	'title':'casc bleuthouth',
	'content':None
}

get_response = requests.delete(endpoint2)

print(get_response)