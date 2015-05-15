# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import NonRomanAlphabetWorkEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetWorkRecord


"""
NRAWorkRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNRAWorkRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = NonRomanAlphabetWorkEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetWorkRecord(record_type='NET',
                                          transaction_sequence_n=3,
                                          record_sequence_n=15,
                                          title='THE TITLE',
                                          language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('NET', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('THE TITLE', encoded['title'])
        self.assertEqual('ES', encoded['language_code'])