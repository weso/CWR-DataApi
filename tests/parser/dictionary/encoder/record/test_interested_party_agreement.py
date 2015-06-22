# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import \
    InterestedPartyForAgreementDictionaryEncoder
from cwr.agreement import InterestedPartyForAgreementRecord
from cwr.other import IPIBaseNumber

"""
InterestedPartyForAgreementRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAgreementInterestedPartyRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = InterestedPartyForAgreementDictionaryEncoder()

    def test_encoded(self):
        ipi_base = IPIBaseNumber('I', 229, 7)

        data = InterestedPartyForAgreementRecord(record_type='ACK',
                                                 transaction_sequence_n=3,
                                                 record_sequence_n=15,
                                                 ip_n='AB12',
                                                 ip_last_name='LAST NAME',
                                                 agreement_role_code='AS',
                                                 ip_writer_first_name='FIRST NAME',
                                                 ipi_name_n='00014107338',
                                                 ipi_base_n=ipi_base,
                                                 pr_society=12,
                                                 pr_share=50.5,
                                                 mr_society=13,
                                                 mr_share=60.5,
                                                 sr_society=14,
                                                 sr_share=70.5)

        encoded = self._encoder.encode(data)

        self.assertEqual('ACK', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('AB12', encoded['ip_n'])
        self.assertEqual('LAST NAME', encoded['ip_last_name'])
        self.assertEqual('AS', encoded['agreement_role_code'])
        self.assertEqual('FIRST NAME', encoded['ip_writer_first_name'])
        self.assertEqual('00014107338', encoded['ipi_name_n'])
        self.assertEqual(12, encoded['pr_society'])
        self.assertEqual(50.5, encoded['pr_share'])
        self.assertEqual(13, encoded['mr_society'])
        self.assertEqual(60.5, encoded['mr_share'])
        self.assertEqual(14, encoded['sr_society'])
        self.assertEqual(70.5, encoded['sr_share'])

        self.assertEqual('I', encoded['ipi_base_n']['header'])
        self.assertEqual(229, encoded['ipi_base_n']['id_code'])
        self.assertEqual(7, encoded['ipi_base_n']['check_digit'])
