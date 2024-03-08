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
def covid():
    try:
        headers = {
            'AccessKey': {'YourKeyValueHere'}  # Defina o cabeçalho User-Agent de acordo com sua aplicação
        }
        response = requests.get('https://services.apistore.dev/apistore/countries/v1', headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
            return render_template('index.html', data=data)
        else:
            print('data')
            return jsonify({'error': 'Failed to fetch data'}), 500
    except:
        return jsonify({'error': 'Failed to connect to API'}), 500