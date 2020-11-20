import requests


def client():
    # credentials = {'username':'nill', 'password':'nill1234'}
    token_h = 'Token 60456575f811ce24ebd48322f44766d11ca8a456'
    headers = {'Authorization':token_h}

    response = requests.get('http://127.0.0.1:8000/api/profile/', headers = headers)

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client()