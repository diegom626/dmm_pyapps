#!/usr/bin/env python


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    @classmethod
    def franchise(cls, store):
        new_store = cls(store.name + " - franchise")
        return new_store

    @staticmethod
    def store_details(store):
        return "{}, Total stock price: {}".format(store.name, int(store.stock_price()))
