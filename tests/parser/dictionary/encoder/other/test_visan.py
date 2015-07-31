# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import VISANDictionaryEncoder
from cwr.other import VISAN

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestVISANEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = VISANDictionaryEncoder()

    def test_encoded(self):
        encoded = self._encoder.encode(1234)

        self.assertEqual(1234, encoded)
