# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import AdditionalRecordRelatedInfoEncoder
from cwr.info import AdditionalRelatedInfoRecord


"""
Additional Related Info to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAdditionalRelatedInfoRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = AdditionalRecordRelatedInfoEncoder()

    def test_encoded(self):
        data = AdditionalRelatedInfoRecord(record_type='GRH',
                                           transaction_sequence_n=3,
                                           record_sequence_n=15,
                                           society_n=18,
                                           type_of_right='PER',
                                           work_n=12,
                                           subject_code='RQ',
                                           note='NOTE')

        encoded = self._encoder.encode(data)

        self.assertEqual('GRH', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(18, encoded['society_n'])
        self.assertEqual('PER', encoded['type_of_right'])
        self.assertEqual(12, encoded['work_n'])
        self.assertEqual('RQ', encoded['subject_code'])
        self.assertEqual('NOTE', encoded['note'])