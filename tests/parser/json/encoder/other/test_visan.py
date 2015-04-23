# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.other import VISAN


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPIBaseEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = VISAN(1, 2, 3, 4)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual(1, encoded['version'])
        self.assertEqual(2, encoded['isan'])
        self.assertEqual(3, encoded['episode'])
        self.assertEqual(4, encoded['check_digit'])