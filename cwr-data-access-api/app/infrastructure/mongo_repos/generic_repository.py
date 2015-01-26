from app.infrastructure.mongo_repos.config import host, port, db_name
from app.infrastructure.mongo_repos.mongo_connection import connect_to_db

__author__ = 'borja'


class GenericRepository(object):
    ELEMENTS_PER_PAGE = 15

    def __init__(self, url_root, collection):
        self._db = connect_to_db(host=host, port=port, db_name=db_name)
        self._url_root = url_root
        self._collection = collection

    @property
    def collection(self):
        return self._collection

    def find_all(self, page_number):
        return list(self._db[self.collection].find().skip(int(page_number) * self.ELEMENTS_PER_PAGE).limit(
            self.ELEMENTS_PER_PAGE))

    def find_by_id(self, item_id):
        item = self._db[self.collection].find_one({'_id': item_id})

        if item is None:
            return "The item with id {} was not found in collection {}".format(item_id, self.collection)

        return item

    def insert_items(self, items):
        for item in items:
            self.insert_item(item)

    def insert_item(self, item):
        self._db[self.collection].insert(item.to_mongo_dict())

    def drop_collection(self):
        self._db[self.collection].drop()