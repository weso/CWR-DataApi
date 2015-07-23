# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import IPIBaseDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestIPIBaseDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = IPIBaseDictionaryDecoder()

    def test_encoded(self):
        record = self._decoder.decode('I-000000229-7')

        self.assertEqual('I-000000229-7', record)
