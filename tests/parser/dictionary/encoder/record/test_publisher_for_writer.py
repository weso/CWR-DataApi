# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import PublisherForWriterDictionaryEncoder
from cwr.interested_party import PublisherForWriterRecord


"""
Publisher for Writer record to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPublisherForWriterRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = PublisherForWriterDictionaryEncoder()

    def test_encoded(self):
        data = PublisherForWriterRecord(record_type='SPU',
                                        transaction_sequence_n=3,
                                        record_sequence_n=15,
                                        publisher_ip_n='111',
                                        writer_ip_n='222',
                                        submitter_agreement_n='333',
                                        society_assigned_agreement_n='444')

        encoded = self._encoder.encode(data)

        self.assertEqual('SPU', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('111', encoded['publisher_ip_n'])
        self.assertEqual('222', encoded['writer_ip_n'])
        self.assertEqual('333', encoded['submitter_agreement_n'])
        self.assertEqual('444', encoded['society_assigned_agreement_n'])