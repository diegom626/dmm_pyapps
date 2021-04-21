#!/usr/bin/env python
import pymongo
from database import Database
from menu import Menu

Database.initialize()

if __name__ == '__main__':
    menu = Menu()
    menu.run_menu()
