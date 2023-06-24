from extentions import got_response, data

GET_HEADERS = {'accept': 'application/json'}
POST_HEADERS = {'accept': 'application/json', 'Content-Type': 'application/json'}

# GET RESPONSE
params = {'status': 'sold'}
url = 'https://petstore.swagger.io/v2/pet/findByStatus'

got_response(url, 'get', headers=GET_HEADERS, params=params)


# POST RESPONSE
url = 'https://petstore.swagger.io/v2/user/createWithList'

got_response(url, 'post', headers=POST_HEADERS, json=data)


# ANOTHER GET RESPONSE
username = data[0]['username']
got_response(f'https://petstore.swagger.io/v2/user/{username}','get', headers=GET_HEADERS)


# PUT RESPONSE
url = f'https://petstore.swagger.io/v2/user/{username}'
data = data[0]
data['phone'] = '+7(985)116-79-61656'

got_response(url, 'put', headers=POST_HEADERS, json=data)


# AGAIN GET RESPONSE
got_response(f'https://petstore.swagger.io/v2/user/{username}','get', headers=GET_HEADERS)


# DELETE RESPONSE
url = f'https://petstore.swagger.io/v2/user/{username}'

got_response(url, 'delete', headers=GET_HEADERS)
