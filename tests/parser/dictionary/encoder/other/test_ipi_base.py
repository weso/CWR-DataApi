# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import CWRDictionaryEncoder
from cwr.other import IPIBaseNumber


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
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = IPIBaseNumber('T', 123456789,
                             1)

        encoded = self._encoder.encode(data)

        self.assertEqual('T', encoded['header'])
        self.assertEqual(123456789, encoded['id_code'])
        self.assertEqual(1, encoded['check_digit'])