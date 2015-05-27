# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import ISWCDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestISWCDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = ISWCDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['id_code'] = 123456789
        dict['check_digit'] = 1

        record = self._decoder.decode(dict)

        self.assertEqual('T', record.header)
        self.assertEqual(123456789, record.id_code)
        self.assertEqual(1, record.check_digit)
