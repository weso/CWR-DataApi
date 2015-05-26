# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import VISANDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestVISANDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = VISANDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['version'] = 1
        dict['isan'] = 2
        dict['episode'] = 3
        dict['check_digit'] = 4

        record = self._decoder.decode(dict)

        self.assertEqual(1, record.version)
        self.assertEqual(2, record.isan)
        self.assertEqual(3, record.episode)
        self.assertEqual(4, record.check_digit)
