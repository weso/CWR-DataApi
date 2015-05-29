# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import InterestedPartyForAgreementDictionaryDecoder
from cwr.other import IPIBaseNumber

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestInterestedPartyForAgreementDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = InterestedPartyForAgreementDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'IPA'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['ip_n'] = 'IP123'
        data['ip_last_name'] = 'LAST NAME'
        data['agreement_role_code'] = 'AS'
        data['ip_writer_first_name'] = 'FIRST NAME'
        data['ipi_name_n'] = 250165006
        data['ipi_base_n'] = IPIBaseNumber('I', 229, 7)
        data['pr_society'] = 1
        data['pr_share'] = 50.1
        data['mr_society'] = 2
        data['mr_share'] = 50.2
        data['sr_society'] = 3
        data['sr_share'] = 50.3

        record = self._decoder.decode(data)

        self.assertEqual('IPA', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('LAST NAME', record.ip_last_name)
        self.assertEqual('AS', record.agreement_role_code)
        self.assertEqual('FIRST NAME', record.ip_writer_first_name)
        self.assertEqual(250165006, record.ipi_name_n)
        self.assertEqual('I', record.ipi_base_n.header)
        self.assertEqual(229, record.ipi_base_n.id_code)
        self.assertEqual(7, record.ipi_base_n.check_digit)
        self.assertEqual(1, record.pr_society)
        self.assertEqual(50.1, record.pr_share)
        self.assertEqual(2, record.mr_society)
        self.assertEqual(50.2, record.mr_share)
        self.assertEqual(3, record.sr_society)
        self.assertEqual(50.3, record.sr_share)
