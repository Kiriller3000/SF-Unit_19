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
        print('Не допустимый метод')
    return print('\n Статус код: ', response.status_code,'\n',f'Ответ на {method} запрос: ', response.json())

