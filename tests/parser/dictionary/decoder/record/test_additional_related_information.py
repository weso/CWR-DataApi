# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import AdditionalRelatedInformationDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAdditionalRelatedInformationRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = AdditionalRelatedInformationDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'ARI'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['society_n'] = 1
        dict['type_of_right'] = 'PER'
        dict['work_n'] = 'WORK123'
        dict['subject_code'] = 'SUB123'
        dict['note'] = 'A NOTE'

        record = self._decoder.decode(dict)

        self.assertEqual('ARI', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(1, record.society_n)
        self.assertEqual('PER', record.type_of_right)
        self.assertEqual('WORK123', record.work_n)
        self.assertEqual('SUB123', record.subject_code)
        self.assertEqual('A NOTE', record.note)