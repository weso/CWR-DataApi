__author__ = 'borja'

from pymongo import MongoClient


def connect_to_db(host, port, db_name):
    client = MongoClient(host, port)
    db = client[db_name]

    return db
