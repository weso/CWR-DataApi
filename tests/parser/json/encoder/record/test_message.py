# -*- coding: utf-8 -*-

import unittest
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.acknowledgement import MessageRecord


"""
Message to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestMessageRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = MessageRecord(record_type='MSG',
                             transaction_sequence_n=3,
                             record_sequence_n=15,
                             message_level='F',
                             validation_n='AB3',
                             message_type='G',
                             message_text='THE MESSAGE',
                             original_record_sequence_n=124,
                             message_record_type='AGR')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('MSG', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('F', encoded['message_level'])
        self.assertEqual('AB3', encoded['validation_n'])
        self.assertEqual('G', encoded['message_type'])
        self.assertEqual('THE MESSAGE', encoded['message_text'])
        self.assertEqual(124, encoded['original_record_sequence_n'])
        self.assertEqual('AGR', encoded['message_record_type'])