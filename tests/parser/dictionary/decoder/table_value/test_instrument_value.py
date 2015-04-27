# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import InstrumentValueDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestInstrumentValueDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = InstrumentValueDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['code'] = 'BBF'
        dict['name'] = 'Bamboo Flute'
        dict['family'] = 'National/Folk'
        dict['description'] = 'same as Dizi or D\'Tzu'

        record = self._decoder.decode(dict)

        self.assertEqual('BBF', record.code)
        self.assertEqual('Bamboo Flute', record.name)
        self.assertEqual('National/Folk', record.family)
        self.assertEqual('same as Dizi or D\'Tzu', record.description)