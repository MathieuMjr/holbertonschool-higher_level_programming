#!/usr/bin/env python3
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as file:
        content = json.load(file)
    if content == "":
        datas = []
    else:
        datas = content['items']
    return render_template('items.html', datas=datas)
# Il faut nommer la variable qu'on envoit dans le html pour la réutiliser sous
# le même nom
# dans le html via jinja. Ici on envoi datas sous le nom datas.
# Mais on aurait pu faire
# variable = datas pour récupérer "variable" via jinja


if __name__ == '__main__':
    app.run(debug=True, port=5000)
