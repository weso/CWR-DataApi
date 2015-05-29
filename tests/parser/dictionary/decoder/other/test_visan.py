# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import VISANDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestVISANDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = VISANDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['version'] = 1
        data['isan'] = 2
        data['episode'] = 3
        data['check_digit'] = 4

        record = self._decoder.decode(data)

        self.assertEqual(1, record.version)
        self.assertEqual(2, record.isan)
        self.assertEqual(3, record.episode)
        self.assertEqual(4, record.check_digit)
