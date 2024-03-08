from flask import Flask, Blueprint, jsonify, render_template
import requests
service = Blueprint('service', __name__)

@service.route('/hello')
def hello():
    return jsonify({'message': 'Hello from the blueprint!'})

@service.route('/goodbye')
def goodbye():
    return jsonify({'message': 'Goodbye from the blueprint!'})

@service.route('/aaa')
def index():
    # Faz uma requisição GET para uma API externa (por exemplo, a API de dados do COVID-19)
    response = requests.get('https://api.covid19api.com/summary')

    # Verifica se a requisição foi bem sucedida (código de status 200)
    if response.status_code == 200:
        # Converte a resposta para um objeto JSON
        data = response.json()
        # Passa os dados para o template e renderiza o template
        print(data)
        return render_template('index.html', data=data)
    else:
        # Retorna uma mensagem de erro caso a requisição não tenha sido bem sucedida
        return jsonify({'error': 'Failed to fetch data'}), 500
