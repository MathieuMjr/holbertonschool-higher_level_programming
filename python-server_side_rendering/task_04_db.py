#!/usr/bin/env python3
import json
from flask import Flask, render_template, request
import csv
import sqlite3

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
    if not content:
        datas = []
    else:
        datas = content['items']
    return render_template('items.html', datas=datas)
# Il faut nommer la variable qu'on envoit dans le html pour la réutiliser sous
# le même nom
# dans le html via jinja. Ici on envoi datas sous le nom datas.
# Mais on aurait pu faire
# variable = datas pour récupérer "variable" via jinja


@app.route('/products')
def products():
    datas = request.args
    source = ""
    id = ""
    if 'source' in datas:
        source = datas['source']
    if 'id' in datas:
        id = datas['id']
    if source == 'csv':
        with open("products.csv", 'r') as file:
            content = list(csv.DictReader(file))
    elif source == 'json':
        with open('products.json', 'r') as file:
            content = json.load(file)
    elif source == 'db':
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        content = []
        for tuple in rows:
            content.append({
                "id": tuple[0],
                "name": tuple[1],
                "category": tuple[2],
                "price": tuple[3]
            })
    else:
        return render_template('product_display.html', error="Wrong source")
    if id:
        id_data = []
        for element in content:
            if element['id'] == int(id) or element['id'] == id:
                id_data.append(element)
                return render_template('product_display.html', datas=id_data)
        if not id_data:
            return render_template('product_display.html', error="Product not found")
    else:
        return render_template('product_display.html', datas=content)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
