import requests

def shorten_link(full_link, link_name):
    API_KEY = '5e8080ab9cda701555f252900bf2fa907d2c4'
    BASE_URL = 'https://cutt.ly/api/api.ph'

    paylaod = {'key': API_KEY, 'short' : full_link, 'name' : link_name}
    request = requests.get(BASE_URL, params=paylaod)
    data = request.json()

    print(data)

#shorten_link('paste_link', 'name_the_link')