import requests
from requests.models import Response

def retorna_cep():
    response = requests.get('https://viacep.com.br/ws/01001000/json/')
    print(response.text)
    print(type(response))
    print(type(response.json())),
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def retorna_pokemon():
    response = requests.get('')
