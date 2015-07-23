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
        record = self._decoder.decode('T0123456789')

        self.assertEqual('T0123456789', record)
