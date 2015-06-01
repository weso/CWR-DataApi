# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import InstrumentValueDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestInstrumentValueDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = InstrumentValueDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['code'] = 'BBF'
        data['name'] = 'Bamboo Flute'
        data['family'] = 'National/Folk'
        data['description'] = 'same as Dizi or D\'Tzu'

        record = self._decoder.decode(data)

        self.assertEqual('BBF', record.code)
        self.assertEqual('Bamboo Flute', record.name)
        self.assertEqual('National/Folk', record.family)
        self.assertEqual('same as Dizi or D\'Tzu', record.description)
