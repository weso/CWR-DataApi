# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import AlternateTitleEncoder
from cwr.work import AlternateTitleRecord


"""
AlternateTitleRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAuthoredWorkRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = AlternateTitleEncoder()

    def test_encoded(self):
        data = AlternateTitleRecord(record_type='SWR',
                                    transaction_sequence_n=3,
                                    record_sequence_n=15,
                                    alternate_title='ALTERNATE',
                                    title_type='FT',
                                    language_code='ES')

        encoded = self._encoder.encode(data)

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('ALTERNATE', encoded['alternate_title'])
        self.assertEqual('FT', encoded['title_type'])
        self.assertEqual('ES', encoded['language_code'])