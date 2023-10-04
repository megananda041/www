from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_data', methods=['POST'])
def load_data():
    url = request.form['url']
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return display_data(data, url)
    else:
        return 'Failed to retrieve data'

def display_data(data, url):
    table = '<table border="1">'
    table += '<tr>'
    headers = data[0].keys()
    for header in headers:
        table += f'<th>{header}</th>'
    table += '</tr>'

    for item in data:
        table += '<tr>'
        for header in headers:
            table += f'<td>{item[header]}</td>'
        table += '</tr>'

    table += '</table>'
    table += f'<div>Data loaded from: {url}</div>'
    return table

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
