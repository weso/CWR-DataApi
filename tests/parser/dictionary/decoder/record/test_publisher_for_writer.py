# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import PublisherForWriterDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPublisherForWriterDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = PublisherForWriterDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'SPU'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['publisher_ip_n'] = '111'
        data['writer_ip_n'] = '222'
        data['submitter_agreement_n'] = '333'
        data['society_assigned_agreement_n'] = '444'

        record = self._decoder.decode(data)

        self.assertEqual('SPU', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('111', record.publisher_ip_n)
        self.assertEqual('222', record.writer_ip_n)
        self.assertEqual('333', record.submitter_agreement_n)
        self.assertEqual('444', record.society_assigned_agreement_n)
