import requests


def client():
    data = {
        'username':'hbe',
        'email':'hbe@gmail.com', 
        'password1':'nill1234',
        'password2':'nill1234',
        }
    # token_h = 'Token 60456575f811ce24ebd48322f44766d11ca8a456'
    # headers = {'Authorization':token_h}

    response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data = data)

    response_data = response.json()
    print(response_data)


if __name__ == '__main__':
    client() 