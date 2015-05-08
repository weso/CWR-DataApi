# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import MessageDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestMessageRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = MessageDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'MSG'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['message_level'] = 'F'
        dict['validation_n'] = 'AB3'
        dict['message_type'] = 'G'
        dict['message_text'] = 'THE MESSAGE'
        dict['original_record_sequence_n'] = 124
        dict['message_record_type'] = 'AGR'

        record = self._decoder.decode(dict)

        self.assertEqual('MSG', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('F', record.message_level)
        self.assertEqual('G', record.message_type)
        self.assertEqual('THE MESSAGE', record.message_text)
        self.assertEqual('AGR', record.message_record_type)