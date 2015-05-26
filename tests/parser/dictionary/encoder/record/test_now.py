# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import NonRomanAlphabetOtherWriterDictionaryEncoder
from cwr.non_roman_alphabet import NonRomanAlphabetOtherWriterRecord

"""
NOWRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNOWRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = NonRomanAlphabetOtherWriterDictionaryEncoder()

    def test_encoded(self):
        data = NonRomanAlphabetOtherWriterRecord(record_type='NOW',
                                                 transaction_sequence_n=3,
                                                 record_sequence_n=15,
                                                 writer_first_name='FIRST NAME',
                                                 writer_name='NAME',
                                                 position=5,
                                                 language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('NOW', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('FIRST NAME', encoded['writer_first_name'])
        self.assertEqual('NAME', encoded['writer_name'])
        self.assertEqual(5, encoded['position'])
        self.assertEqual('ES', encoded['language_code'])
