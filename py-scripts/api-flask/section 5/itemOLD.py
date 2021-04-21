import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Este item debe tener un precio")

    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item is not None else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "Un item con el nombre '{}' ya existe".format(name)}, 400
        request_data = Item.parser.parse_args()
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'message': 'Item deleted'}

    def put(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        request_data = Item.parser.parse_args()
        if item is None:
            item = {'name': name, 'price': request_data}
            items.append(item)
        else:
            item.update(request_data)
        return item, 200


class ItemList(Resource):
    def get(self):
        return {'items': items}
