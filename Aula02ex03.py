#API
import requests

resposta = request.get('https://parallelum.com.br/fipe/api/v1/carros/marcas')

print(f'Status da Requisição: {resposta.status_code}')

print(f'Resposta da API: {resposta.json()}')