# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import MediaTypeValueDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestMediaTypeValueDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = MediaTypeValueDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['code'] = 'EP'
        data['name'] = '45 rpm 17 cm EP'
        data['media_type'] = 'VINYL'
        data['duration_max'] = 16
        data['works_max'] = 4
        data['fragments_max'] = 12

        record = self._decoder.decode(data)

        self.assertEqual('EP', record.code)
        self.assertEqual('45 rpm 17 cm EP', record.name)
        self.assertEqual('VINYL', record.media_type)
        self.assertEqual(16, record.duration_max)
        self.assertEqual(4, record.works_max)
        self.assertEqual(12, record.fragments_max)
