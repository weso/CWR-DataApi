# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.encoder.cwrjson import JSONEncoder
from cwr.group import GroupTrailer


"""
Group Trailer to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestGroupTrailerDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = GroupTrailer(record_type='GRT',
                            group_id=3,
                            transaction_count=15,
                            record_count=20)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('GRT', encoded['record_type'])
        self.assertEqual(3, encoded['group_id'])
        self.assertEqual(15, encoded['transaction_count'])
        self.assertEqual(20, encoded['record_count'])