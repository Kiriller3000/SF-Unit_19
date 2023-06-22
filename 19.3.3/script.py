from extentions import got_response

# GET RESPONSE
get_headers = {'accept': 'application/json'}
params = {'status': 'sold'}
url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'

got_response(url, 'get', headers=get_headers, params=params)


# POST RESPONSE
url = 'https://petstore.swagger.io/v2/user/createWithList'
post_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
username = 'name'
data = [
  {
    "id": 0,
    "username": f"{username}",
    "firstName": "FName",
    "lastName": "LName",
    "email": "wefw@sdvs.tk",
    "password": "passw0rd",
    "phone": "+1(156)651-651-651",
    "userStatus": 0
  }
]
got_response(url, 'post', headers=post_headers, json=data)


# ANOTHER GET RESPONSE
got_response(f'https://petstore.swagger.io/v2/user/{username}','get', headers=get_headers)


# PUT RESPONSE
url = f'https://petstore.swagger.io/v2/user/{username}'
data = data[0]
data['phone'] = '+7(985)116-79-61656'

got_response(url, 'put', headers=post_headers, json=data)


# AGAIN GET RESPONSE
got_response(f'https://petstore.swagger.io/v2/user/{username}','get', headers=get_headers)


# DELETE RESPONSE
url = f'https://petstore.swagger.io/v2/user/{username}'

got_response(url, 'delete', headers=get_headers)
