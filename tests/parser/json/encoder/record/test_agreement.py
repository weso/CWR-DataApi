# -*- coding: utf-8 -*-

import unittest
import datetime
import json

from cwr.agreement import AgreementRecord
from cwr.parser.cwrjson import JSONEncoder


"""
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAgreementRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = AgreementRecord(record_type='ACK',
                               transaction_sequence_n=3,
                               record_sequence_n=15,
                               submitter_agreement_n='AB12',
                               agreement_type='OS',
                               agreement_start_date=datetime.datetime.strptime('20030215', '%Y%m%d').date(),
                               number_of_works=12,
                               prior_royalty_status='D',
                               post_term_collection_status='D',
                               international_standard_code='DFG135',
                               society_assigned_agreement_n='DF35',
                               sales_manufacture_clause='M',
                               agreement_end_date=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                               date_of_signature=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                               retention_end_date=datetime.datetime.strptime('20030218', '%Y%m%d').date(),
                               prior_royalty_start_date=datetime.datetime.strptime('20030219', '%Y%m%d').date(),
                               post_term_collection_end_date=datetime.datetime.strptime('20030220', '%Y%m%d').date(),
                               shares_change=True,
                               advance_given=True)

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('ACK', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('AB12', encoded['submitter_agreement_n'])
        self.assertEqual('OS', encoded['agreement_type'])
        self.assertEqual('2003-02-15', encoded['agreement_start_date'])
        self.assertEqual(12, encoded['number_of_works'])
        self.assertEqual('D', encoded['prior_royalty_status'])
        self.assertEqual('D', encoded['post_term_collection_status'])
        self.assertEqual('DFG135', encoded['international_standard_code'])
        self.assertEqual('DF35', encoded['society_assigned_agreement_n'])
        self.assertEqual('M', encoded['sales_manufacture_clause'])
        self.assertEqual('2003-02-16', encoded['agreement_end_date'])
        self.assertEqual('2003-02-17', encoded['date_of_signature'])
        self.assertEqual('2003-02-18', encoded['retention_end_date'])
        self.assertEqual('2003-02-19', encoded['prior_royalty_start_date'])
        self.assertEqual('2003-02-20',
                         encoded['post_term_collection_end_date'])
        self.assertEqual(True, encoded['shares_change'])
        self.assertEqual(True, encoded['advance_given'])