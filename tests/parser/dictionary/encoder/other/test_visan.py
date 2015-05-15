# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import VISANEncoder
from cwr.other import VISAN


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestVISANEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = VISANEncoder()

    def test_encoded(self):
        data = VISAN(1, 2, 3, 4)

        encoded = self._encoder.encode(data)

        self.assertEqual(1, encoded['version'])
        self.assertEqual(2, encoded['isan'])
        self.assertEqual(3, encoded['episode'])
        self.assertEqual(4, encoded['check_digit'])