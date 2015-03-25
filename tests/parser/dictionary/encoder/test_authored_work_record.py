# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.work import AuthoredWorkRecord
from cwr.other import ISWCCode


"""
AuthoredWorkRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAuthoredWorkRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        iswc = ISWCCode(12345678, 9)

        data = AuthoredWorkRecord(record_type='SWR',
                                  transaction_sequence_n=3,
                                  record_sequence_n=15,
                                  title='TITLE',
                                  submitter_work_n='ABC135',
                                  writer_1_first_name='FIRST NAME 1',
                                  writer_1_last_name='LAST NAME 1',
                                  writer_2_first_name='FIRST NAME 2',
                                  writer_2_last_name='LAST NAME 2',
                                  writer_1_ipi_base_n='I-000000229-7',
                                  writer_1_ipi_name_n=14107338,
                                  writer_2_ipi_base_n='I-000000300-7',
                                  writer_2_ipi_name_n=14107448,
                                  source='SOURCE',
                                  language_code='ES',
                                  iswc=iswc)

        encoded = self._encoder.encode(data)

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('TITLE', encoded['title'])
        self.assertEqual('ABC135', encoded['submitter_work_n'])
        self.assertEqual('FIRST NAME 1', encoded['writer_1_first_name'])
        self.assertEqual('LAST NAME 1', encoded['writer_1_last_name'])
        self.assertEqual('FIRST NAME 2', encoded['writer_2_first_name'])
        self.assertEqual('LAST NAME 2', encoded['writer_2_last_name'])
        self.assertEqual('I-000000229-7', encoded['writer_1_ipi_base_n'])
        self.assertEqual(14107338, encoded['writer_1_ipi_name_n'])
        self.assertEqual('I-000000300-7', encoded['writer_2_ipi_base_n'])
        self.assertEqual(14107448, encoded['writer_2_ipi_name_n'])
        self.assertEqual('SOURCE', encoded['source'])
        self.assertEqual('ES', encoded['language_code'])
        self.assertEqual(12345678, encoded['iswc'].id_code)
        self.assertEqual(9, encoded['iswc'].check_digit)