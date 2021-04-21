#!/usr/bin/env python
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

tiendas = [
    {'name': "Amazon jijij",
     'items': [
         {
             'name': 'ps4',
             'price': 10.99
         }
     ]

     }
]

@app.route('/')
def home():
    return render_template('index.html')


# POST /store data: {name:}
@app.route('/tienda', methods=['POST'])
def crear_tienda():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    tiendas.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/tienda/<string:name>', methods=['GET'])
def get_store(name):
    for tienda in tiendas:
        if tienda['name'] == name:
            return jsonify(tienda)
    return jsonify({'mensaje:': 'Error, la tienda no se encuentra'})


# GET /store
@app.route('/tienda/', methods=['GET'])
def list_store():
    return jsonify({'stores': tiendas})


# POST /store/<string:name>/item {name:, price}
@app.route('/tienda/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for tienda in tiendas:
        if tienda['name'] == name:
            nuevo_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            tienda['items'].append(nuevo_item)
            return jsonify(tienda['items'])
    return jsonify({'mensaje:': 'Error, la tienda no se encuentra para agregar item correspondiente'})


# GET /store/<string:name>/item
@app.route('/tienda/<string:name>/item')
def get_item_in_store(name):
        for tienda in tiendas:
            if tienda['name'] == name:
                if len(tienda['items']) >= 1:
                    return jsonify({'tienda': name, 'items': tienda['items']})
                else:
                    return jsonify({'message': 'La tienda no tiene items'})
        return jsonify({'mensaje:': 'Error, la tienda no se encuentra'})


app.run(port=5000, debug=True)

