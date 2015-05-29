# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AVIKeyDictionaryDecoder

"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAVIKeyDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AVIKeyDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['society_code'] = 1
        data['av_number'] = 2

        record = self._decoder.decode(data)

        self.assertEqual(1, record.society_code)
        self.assertEqual(2, record.av_number)
