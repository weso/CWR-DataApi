# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import AcknowledgementDictionaryDecoder

"""
Dictionary to Acknowledgement decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAcknowledgementRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AcknowledgementDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'ACK'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['original_group_id'] = 4
        data['original_transaction_sequence_n'] = 5
        data['original_transaction_type'] = 'AGR'
        data['transaction_status'] = 'AS'
        data['creation_date_time'] = datetime.datetime.strptime('20030215',
                                                                '%Y%m%d').date()
        data['processing_date'] = datetime.datetime.strptime('20030216',
                                                             '%Y%m%d').date()
        data['creation_title'] = 'TITLE'
        data['submitter_creation_n'] = 'A123'
        data['recipient_creation_n'] = 'B124'

        record = self._decoder.decode(data)

        self.assertEqual('ACK', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(4, record.original_group_id)
        self.assertEqual(5, record.original_transaction_sequence_n)
        self.assertEqual('AGR', record.original_transaction_type)
        self.assertEqual('AS', record.transaction_status)
        self.assertEqual(
            datetime.datetime.strptime('20030215', '%Y%m%d').date(),
            record.creation_date_time)
        self.assertEqual(
            datetime.datetime.strptime('20030216', '%Y%m%d').date(),
            record.processing_date)
        self.assertEqual('TITLE', record.creation_title)
        self.assertEqual('A123', record.submitter_creation_n)
        self.assertEqual('B124', record.recipient_creation_n)
