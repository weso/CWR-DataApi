# -*- encoding: utf-8 -*-

import unittest
import re

from tests.mongo.mongo_test_conf import host, port, db_name, MongoGenericRepository
from commonworks.table_value import TableValue


"""
Unit tests to check if the Repository API can be made to work correctly with Mongo.

Requires a Mongo database running, and set up as mongo_test_conf indicates.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestQuery(unittest.TestCase):
    """
    Tests querying the Mongo repository.
    """

    def setUp(self):
        self.repo = MongoGenericRepository(host, port, db_name, 'queries')

        entity = TableValue('id', 'name', 'descriptor')
        self.repo.add(entity)

        entity = TableValue('10', 'entity_1', 'descriptor')
        self.repo.add(entity)
        entity = TableValue('11', 'entity_2', 'descriptor')
        self.repo.add(entity)
        entity = TableValue('12', 'entity_3', 'descriptor')
        self.repo.add(entity)

        entity = TableValue('AS', 'Assignor',
                            'The entitled party who is assigning the rights to a musical work within an agreement')
        self.repo.add(entity)

        entity = TableValue('POP', 'Popular',
                            'The musical mainstream, usually song-based and melody-orientated, created for mass '
                            'consumption')
        self.repo.add(entity)

    def tearDown(self):
        self.repo.clear()

    def test_all(self):
        entities = self.repo.get(lambda e: True)
        self.assertEqual(len(entities), 6)

    def test_name_regex(self):
        expression = re.compile('entity_\d*')
        entities = self.repo.get(lambda e: expression.match(e['name']))
        self.assertEqual(len(entities), 3)

    def test_name_exact(self):
        entities = self.repo.get(lambda e: e['name'] == 'Popular')
        self.assertEqual(len(entities), 1)


if __name__ == '__main__':
    unittest.main()