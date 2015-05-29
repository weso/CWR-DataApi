# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import AgreementDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAgreementRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AgreementDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'ACK'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['submitter_agreement_n'] = 'AB12'
        data['agreement_type'] = 'OS'
        data['agreement_start_date'] = datetime.datetime.strptime('20030215',
                                                                  '%Y%m%d').date()
        data['number_of_works'] = 12
        data['prior_royalty_status'] = 'D'
        data['post_term_collection_status'] = 'D'
        data['international_standard_code'] = 'DFG135'
        data['society_assigned_agreement_n'] = 'DF35'
        data['sales_manufacture_clause'] = 'M'
        data['agreement_end_date'] = datetime.datetime.strptime('20030216',
                                                                '%Y%m%d').date()
        data['date_of_signature'] = datetime.datetime.strptime('20030217',
                                                               '%Y%m%d').date()
        data['retention_end_date'] = datetime.datetime.strptime('20030218',
                                                                '%Y%m%d').date()
        data['prior_royalty_start_date'] = datetime.datetime.strptime(
            '20030219', '%Y%m%d').date()
        data['post_term_collection_end_date'] = datetime.datetime.strptime(
            '20030220', '%Y%m%d').date()
        data['shares_change'] = True
        data['advance_given'] = True

        record = self._decoder.decode(data)

        self.assertEqual('ACK', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('AB12', record.submitter_agreement_n)
        self.assertEqual('OS', record.agreement_type)
        self.assertEqual(
            datetime.datetime.strptime('20030215', '%Y%m%d').date(),
            record.agreement_start_date)
        self.assertEqual(12, record.number_of_works)
        self.assertEqual('D', record.prior_royalty_status)
        self.assertEqual('D', record.post_term_collection_status)
        self.assertEqual('DFG135', record.international_standard_code)
        self.assertEqual('DF35', record.society_assigned_agreement_n)
        self.assertEqual('M', record.sales_manufacture_clause)
        self.assertEqual(
            datetime.datetime.strptime('20030216', '%Y%m%d').date(),
            record.agreement_end_date)
        self.assertEqual(
            datetime.datetime.strptime('20030217', '%Y%m%d').date(),
            record.date_of_signature)
        self.assertEqual(
            datetime.datetime.strptime('20030218', '%Y%m%d').date(),
            record.retention_end_date)
        self.assertEqual(
            datetime.datetime.strptime('20030219', '%Y%m%d').date(),
            record.prior_royalty_start_date)
        self.assertEqual(
            datetime.datetime.strptime('20030220', '%Y%m%d').date(),
            record.post_term_collection_end_date)
        self.assertEqual(True, record.shares_change)
        self.assertEqual(True, record.advance_given)
