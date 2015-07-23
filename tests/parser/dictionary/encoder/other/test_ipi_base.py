# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import IPIBaseDictionaryEncoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestIPIBaseEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = IPIBaseDictionaryEncoder()

    def test_encoded(self):
        encoded = self._encoder.encode('T-123456789-1')

        self.assertEqual('T-123456789-1', encoded)
