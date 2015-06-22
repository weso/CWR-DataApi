# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.encoder.dictionary import ComponentDictionaryEncoder
from cwr.work import ComponentRecord
from cwr.other import ISWCCode, IPIBaseNumber

"""
ComponentRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestComponentRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = ComponentDictionaryEncoder()

    def test_encoded(self):
        iswc = ISWCCode(12345678, 9)
        ipi_base_1 = IPIBaseNumber('I', 229, 7)
        ipi_base_2 = IPIBaseNumber('I', 339, 7)

        data = ComponentRecord(record_type='COM',
                               transaction_sequence_n=3,
                               record_sequence_n=15,
                               title='TITLE',
                               writer_1_last_name='LAST NAME 1',
                               submitter_work_n='ABCD123',
                               writer_1_first_name='FIRST NAME 1',
                               writer_2_first_name='FIRST NAME 2',
                               writer_2_last_name='LAST NAME 2',
                               writer_1_ipi_base_n=ipi_base_1,
                               writer_1_ipi_name_n=14107338,
                               writer_2_ipi_base_n=ipi_base_2,
                               writer_2_ipi_name_n=14107400,
                               iswc=iswc,
                               duration=datetime.datetime.strptime('011200',
                                                                   '%H%M%S').time())

        encoded = self._encoder.encode(data)

        self.assertEqual('COM', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('TITLE', encoded['title'])
        self.assertEqual('LAST NAME 1', encoded['writer_1_last_name'])
        self.assertEqual('ABCD123', encoded['submitter_work_n'])
        self.assertEqual('FIRST NAME 1', encoded['writer_1_first_name'])
        self.assertEqual('FIRST NAME 2', encoded['writer_2_first_name'])
        self.assertEqual('LAST NAME 2', encoded['writer_2_last_name'])
        self.assertEqual('LAST NAME 2', encoded['writer_2_last_name'])
        self.assertEqual(14107338, encoded['writer_1_ipi_name_n'])
        self.assertEqual(14107400, encoded['writer_2_ipi_name_n'])
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(),
                         encoded['duration'])

        self.assertEqual('I', encoded['writer_1_ipi_base_n']['header'])
        self.assertEqual(229, encoded['writer_1_ipi_base_n']['id_code'])
        self.assertEqual(7, encoded['writer_1_ipi_base_n']['check_digit'])

        self.assertEqual('I', encoded['writer_2_ipi_base_n']['header'])
        self.assertEqual(339, encoded['writer_2_ipi_base_n']['id_code'])
        self.assertEqual(7, encoded['writer_2_ipi_base_n']['check_digit'])

        self.assertEqual(12345678, encoded['iswc']['id_code'])
        self.assertEqual(9, encoded['iswc']['check_digit'])
