from flask import Flask, Blueprint, jsonify, render_template
import requests
service = Blueprint('service', __name__)

@service.route('/repositories')
def repositories():
    try:

        token = 123
        response = requests.get('https://api.github.com/user/repos', headers={'Authorization': f'token {token}'})
        
        print(response)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return render_template('repositories.html', datas=data)
        else:
            print('data')
            return jsonify({'error': 'Failed to fetch data'}), 500
    except requests.exceptions.RequestException as e:
        print(e)
        return jsonify({'error': 'Failed to connect to API'}), 500