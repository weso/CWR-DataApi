# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import PublisherRecordEncoder
from cwr.interested_party import PublisherRecord, Publisher


"""
Publisher to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPublisherDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = PublisherRecordEncoder()

    def test_encoded(self):
        publisher = Publisher(ip_n='ABC15',
                              publisher_name='NAME',
                              ipi_name_n=14107338,
                              ipi_base_n='I-000000229-7',
                              tax_id=923703412)

        data = PublisherRecord(record_type='SPU',
                               transaction_sequence_n=3,
                               record_sequence_n=15,
                               publisher=publisher,
                               publisher_sequence_n=12,
                               submitter_agreement_n='ABC13',
                               publisher_type='PA',
                               publisher_unknown='U',
                               agreement_type='PG',
                               international_standard_code='14AEI',
                               society_assigned_agreement_n='GH34',
                               pr_society=13,
                               pr_ownership_share=50.5,
                               mr_society=14,
                               mr_ownership_share=60.5,
                               sr_society=15,
                               sr_ownership_share=70.5,
                               first_recording_refusal='N',
                               usa_license='B')

        encoded = self._encoder.encode(data)
        publisher = encoded['publisher']

        self.assertEqual('ABC15', publisher['ip_n'])
        self.assertEqual('NAME', publisher['publisher_name'])
        self.assertEqual(14107338, publisher['ipi_name_n'])
        self.assertEqual('I-000000229-7', publisher['ipi_base_n'])
        self.assertEqual(923703412, publisher['tax_id'])

        self.assertEqual('SPU', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(12, encoded['publisher_sequence_n'])
        self.assertEqual('ABC13', encoded['submitter_agreement_n'])
        self.assertEqual('PA', encoded['publisher_type'])
        self.assertEqual('U', encoded['publisher_unknown'])
        self.assertEqual('PG', encoded['agreement_type'])
        self.assertEqual('14AEI', encoded['international_standard_code'])
        self.assertEqual('GH34', encoded['society_assigned_agreement_n'])
        self.assertEqual(13, encoded['pr_society'])
        self.assertEqual(50.5, encoded['pr_ownership_share'])
        self.assertEqual(14, encoded['mr_society'])
        self.assertEqual(60.5, encoded['mr_ownership_share'])
        self.assertEqual(15, encoded['sr_society'])
        self.assertEqual(70.5, encoded['sr_ownership_share'])
        self.assertEqual('N', encoded['first_recording_refusal'])
        self.assertEqual('B', encoded['usa_license'])