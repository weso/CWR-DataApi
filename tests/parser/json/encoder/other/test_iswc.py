# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.other import ISWCCode


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestISWCodeEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = ISWCCode(123456789,
                        1)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual(123456789, encoded['id_code'])
        self.assertEqual(1, encoded['check_digit'])