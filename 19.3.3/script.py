from extentions import got_response, data

# GET RESPONSE
get_headers = {'accept': 'application/json'}
params = {'status': 'sold'}
url = 'https://petstore.swagger.io/v2/pet/findByStatus?status=sold'

got_response(url, 'get', headers=get_headers, params=params)


# POST RESPONSE
url = 'https://petstore.swagger.io/v2/user/createWithList'
post_headers = {'accept': 'application/json', 'Content-Type': 'application/json'}

got_response(url, 'post', headers=post_headers, json=data)


# ANOTHER GET RESPONSE
username = data[0]['username']
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
