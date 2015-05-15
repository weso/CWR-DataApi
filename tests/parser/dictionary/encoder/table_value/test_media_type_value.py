# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import MediaTypeDictionaryEncoder
from cwr.table_value import MediaTypeValue


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestMediaTypeValueEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = MediaTypeDictionaryEncoder()

    def test_encoded(self):
        data = MediaTypeValue('EP', '45 rpm 17 cm EP', 'VINYL', 16, 4, 12)

        encoded = self._encoder.encode(data)

        self.assertEqual('EP', encoded['code'])
        self.assertEqual('45 rpm 17 cm EP', encoded['name'])
        self.assertEqual('VINYL', encoded['media_type'])
        self.assertEqual(16, encoded['duration_max'])
        self.assertEqual(4, encoded['works_max'])
        self.assertEqual(12, encoded['fragments_max'])