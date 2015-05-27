# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import PublisherRecordDictionaryDecoder
from cwr.other import IPIBaseNumber

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPublisherRecordDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = PublisherRecordDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['ip_n'] = 'IP123'
        dict['publisher_name'] = 'NAME'
        dict['ipi_name_n'] = 250165006
        dict['ipi_base_n'] = IPIBaseNumber('I', 229, 7)
        dict['tax_id'] = 923703412

        dict['record_type'] = 'SPU'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['publisher_sequence_n'] = 5
        dict['submitter_agreement_n'] = 'AGR123'
        dict['publisher_type'] = 'PA'
        dict['publisher_unknown'] = 'N'
        dict['agreement_type'] = 'PG'
        dict['international_standard_code'] = 'A0123456789124'
        dict['society_assigned_agreement_n'] = 'SAGR123'
        dict['pr_society'] = 1
        dict['pr_ownership_share'] = 50.1
        dict['mr_society'] = 2
        dict['mr_ownership_share'] = 50.2
        dict['sr_society'] = 3
        dict['sr_ownership_share'] = 50.3
        dict['special_agreements'] = 'N'
        dict['first_recording_refusal'] = 'N'
        dict['usa_license'] = 'B'

        record = self._decoder.decode(dict)

        self.assertEqual('IP123', record.publisher.ip_n)
        self.assertEqual('NAME', record.publisher.publisher_name)
        self.assertEqual(250165006, record.publisher.ipi_name_n)
        self.assertEqual('I', record.publisher.ipi_base_n.header)
        self.assertEqual(229, record.publisher.ipi_base_n.id_code)
        self.assertEqual(7, record.publisher.ipi_base_n.check_digit)
        self.assertEqual(923703412, record.publisher.tax_id)

        self.assertEqual('SPU', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(5, record.publisher_sequence_n)
        self.assertEqual('AGR123', record.submitter_agreement_n)
        self.assertEqual('PA', record.publisher_type)
        self.assertEqual('N', record.publisher_unknown)
        self.assertEqual('PG', record.agreement_type)
        self.assertEqual('A0123456789124', record.international_standard_code)
        self.assertEqual('SAGR123', record.society_assigned_agreement_n)
        self.assertEqual(1, record.pr_society)
        self.assertEqual(50.1, record.pr_ownership_share)
        self.assertEqual(2, record.mr_society)
        self.assertEqual(50.2, record.mr_ownership_share)
        self.assertEqual(3, record.sr_society)
        self.assertEqual(50.3, record.sr_ownership_share)
        self.assertEqual('N', record.special_agreements)
        self.assertEqual('N', record.first_recording_refusal)
        self.assertEqual('B', record.usa_license)
