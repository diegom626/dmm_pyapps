from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()

        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "The store with name {} already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "Something went wrong, couldn't save store"}, 500

        return store.json()

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': "Item: {} deleted".format(name)}, 200


class StoreList(Resource):
    def get(self):
        # return list(map(lambda x: x.json(), ItemModel.query.all()))
        return {'Stores': [store.json() for store in StoreModel.query.all()]}  # Lista de comprension
