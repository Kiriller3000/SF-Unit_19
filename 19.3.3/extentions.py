import requests

def got_response(url: str, method: str, **kwargs):
    if method == 'get':
        response = requests.get(url, **kwargs)
    elif method =='post':
        response = requests.post(url, **kwargs)
    elif method == 'put':
        response = requests.put(url, **kwargs)
    elif method == 'delete':
        response = requests.delete(url, **kwargs)
    else:
        exit('Не допустимый метод')
    return print('\n Статус код: ', response.status_code,'\n',f'Ответ на {method} запрос: ', response.json())

data = [
  {
    "id": 0,
    "username": "Name}",
    "firstName": "FName",
    "lastName": "LName",
    "email": "wefw@sdvs.tk",
    "password": "passw0rd",
    "phone": "+1(156)651-651-651",
    "userStatus": 0
  }
]
