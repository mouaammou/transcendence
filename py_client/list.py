import requests
# from getpass import getpass

token_endpoint = "http://127.0.0.1:8000/api/auth/"

data = {
	"username":"mouaammo",
	"password":"mouad"
}

get_response = requests.post(token_endpoint, json=data)

if get_response.status_code == 200:
	token = get_response.json()['token']

	endpnt = "http://127.0.0.1:8000/api/products"
	print(token)
	headers = {
		"Authorization" : f"Token {token}"
	}

	res = requests.get(endpnt, headers=headers)
	print(res.json())