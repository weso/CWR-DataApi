# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import IPIBaseDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestIPIBaseDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = IPIBaseDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['header'] = 'T'
        dict['id_code'] = 123456789
        dict['check_digit'] = 1

        record = self._decoder.decode(dict)

        self.assertEqual('T', record.header)
        self.assertEqual(123456789, record.id_code)
        self.assertEqual(1, record.check_digit)
