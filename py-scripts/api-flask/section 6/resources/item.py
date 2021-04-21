import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This item must have a price")

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name {} already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])

        try:
            item.insert()
        except:
            return {"message": "An error ocurred inserting the item."}, 500  # Internal server error

        return item.json(), 201

    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items where name=?"
        result = cursor.execute(query, (name,))
        row = result.rowcount
        connection.commit()
        connection.close()

        if row >= 1:
            return {'message': "Item: {} deleted".format(name)}, 200

        return {'message': "Item {} doesn't exists, nothing to do".format(name)}, 204

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        updated_item = ItemModel(name, data['price'])

        if item is None:
            try:
                updated_item.insert()
            except:
                return {"message": "An error ocurred inserting the item."}, 500
        else:
            try:
                updated_item.update()
            except:
                return {"message": "An error ocurred updating the item."}, 500

        return updated_item.json(), 201


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()

        return {'items': items}, 200
