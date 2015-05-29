# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AdditionalRelatedInformationDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAdditionalRelatedInformationRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AdditionalRelatedInformationDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'ARI'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['society_n'] = 1
        data['type_of_right'] = 'PER'
        data['work_n'] = 'WORK123'
        data['subject_code'] = 'SUB123'
        data['note'] = 'A NOTE'

        record = self._decoder.decode(data)

        self.assertEqual('ARI', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(1, record.society_n)
        self.assertEqual('PER', record.type_of_right)
        self.assertEqual('WORK123', record.work_n)
        self.assertEqual('SUB123', record.subject_code)
        self.assertEqual('A NOTE', record.note)
