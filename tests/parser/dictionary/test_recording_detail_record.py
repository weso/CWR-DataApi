# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.work import RecordingDetailRecord


"""
RecordingDetailRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestRecordingDetailRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = RecordingDetailRecord(record_type='SWR',
                                     transaction_sequence_n=3,
                                     record_sequence_n=15,
                                     first_release_date=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                                     first_release_duration=datetime.datetime.strptime('011200', '%H%M%S').time(),
                                     first_album_title='FIRST TITLE',
                                     first_album_label='FIRST LABEL',
                                     first_release_catalog_n='ABF35',
                                     ean=1234567890123,
                                     isrc='ES-A2B-12-12',
                                     recording_format='V',
                                     recording_technique='D',
                                     media_type='CES')

        encoded = self._encoder.encode(data)

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(), encoded['first_release_date'])
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(), encoded['first_release_duration'])
        self.assertEqual('FIRST TITLE', encoded['first_album_title'])
        self.assertEqual('FIRST LABEL', encoded['first_album_label'])
        self.assertEqual('ABF35', encoded['first_release_catalog_n'])
        self.assertEqual(1234567890123, encoded['ean'])
        self.assertEqual('ES-A2B-12-12', encoded['isrc'])
        self.assertEqual('V', encoded['recording_format'])
        self.assertEqual('D', encoded['recording_technique'])
        self.assertEqual('CES', encoded['media_type'])