# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import RecordingDetailDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestRecordingDetailDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = RecordingDetailDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'REC'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['first_release_date'] = datetime.datetime.strptime('20030216', '%Y%m%d').date()
        dict['first_release_duration'] = datetime.datetime.strptime('011200', '%H%M%S').time()
        dict['first_album_title'] = 'FIRST TITLE'
        dict['first_album_label'] = 'FIRST LABEL'
        dict['first_release_catalog_n'] = 'ABF35'
        dict['ean'] = 1234567890123
        dict['isrc'] = 'ES-A2B-12-12'
        dict['recording_format'] = 'V'
        dict['recording_technique'] = 'D'
        dict['media_type'] = 'CES'

        record = self._decoder.decode(dict)

        self.assertEqual('REC', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(), record.first_release_date)
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(), record.first_release_duration)
        self.assertEqual('FIRST TITLE', record.first_album_title)
        self.assertEqual('FIRST LABEL', record.first_album_label)
        self.assertEqual('ABF35', record.first_release_catalog_n)
        self.assertEqual(1234567890123, record.ean)
        self.assertEqual('ES-A2B-12-12', record.isrc)
        self.assertEqual('V', record.recording_format)
        self.assertEqual('D', record.recording_technique)
        self.assertEqual('CES', record.media_type)
