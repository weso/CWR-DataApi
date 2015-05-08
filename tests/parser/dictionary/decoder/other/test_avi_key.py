# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AVIKeyDecoder


"""
Acknowledgement to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAVIKeyDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AVIKeyDecoder()

    def test_encoded(self):
        dict = {}

        dict['society_code'] = 1
        dict['av_number'] = 2

        record = self._decoder.decode(dict)

        self.assertEqual(1, record.society_code)
        self.assertEqual(2, record.av_number)