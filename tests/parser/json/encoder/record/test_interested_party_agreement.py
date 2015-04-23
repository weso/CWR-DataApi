# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.agreement import InterestedPartyForAgreementRecord


"""
InterestedPartyForAgreementRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementInterestedPartyRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = InterestedPartyForAgreementRecord(record_type='ACK',
                                                 transaction_sequence_n=3,
                                                 record_sequence_n=15,
                                                 ip_n='AB12',
                                                 ip_last_name='LAST NAME',
                                                 agreement_role_code='AS',
                                                 ip_writer_first_name='FIRST NAME',
                                                 ipi_name_n='00014107338',
                                                 ipi_base_n='I-000000229-7',
                                                 pr_society=12,
                                                 pr_share=50.5,
                                                 mr_society=13,
                                                 mr_share=60.5,
                                                 sr_society=14,
                                                 sr_share=70.5)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('ACK', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('AB12', encoded['ip_n'])
        self.assertEqual('LAST NAME', encoded['ip_last_name'])
        self.assertEqual('AS', encoded['agreement_role_code'])
        self.assertEqual('FIRST NAME', encoded['ip_writer_first_name'])
        self.assertEqual('00014107338', encoded['ipi_name_n'])
        self.assertEqual('I-000000229-7', encoded['ipi_base_n'])
        self.assertEqual(12, encoded['pr_society'])
        self.assertEqual(50.5, encoded['pr_share'])
        self.assertEqual(13, encoded['mr_society'])
        self.assertEqual(60.5, encoded['mr_share'])
        self.assertEqual(14, encoded['sr_society'])
        self.assertEqual(70.5, encoded['sr_share'])