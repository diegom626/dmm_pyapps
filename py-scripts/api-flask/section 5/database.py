#!/usr/bin/env python
import sqlite3


class Database:
    DB = "test.db"

    def __init__(self):
        self.connect()

    def connect(self):
        self.connection = sqlite3.connect(Database.DB)
        self.cursor = self.connection.cursor()

    def insert_item(self, item, price):
        values = (item, price)
        self.cursor.execute("INSERT INTO items VALUES (?, ?)", values)
        self.close()
        return "ITEM CREATED"

    def find_item(self, item):
        query = "SELECT * FROM items where name=?"
        result = self.cursor.execute(query, (item,))

        row = result.fetchone()

        if row:
            return {'item': {'name': row[0], 'price': row[1]}}
        return "NOT FOUND"

    def close(self):
        self.connection.commit()
        self.connection.close()
