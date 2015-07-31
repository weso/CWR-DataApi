# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import ISWCDictionaryEncoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestISWCodeEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = ISWCDictionaryEncoder()

    def test_encoded(self):
        encoded = self._encoder.encode('T0123456789')

        self.assertEqual('T0123456789', encoded)
