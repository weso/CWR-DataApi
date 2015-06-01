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
__status__ = 'Development'


class TestRecordingDetailDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = RecordingDetailDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'REC'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['first_release_date'] = datetime.datetime.strptime('20030216',
                                                                '%Y%m%d').date()
        data['first_release_duration'] = datetime.datetime.strptime('011200',
                                                                    '%H%M%S').time()
        data['first_album_title'] = 'FIRST TITLE'
        data['first_album_label'] = 'FIRST LABEL'
        data['first_release_catalog_n'] = 'ABF35'
        data['ean'] = 1234567890123
        data['isrc'] = 'ES-A2B-12-12'
        data['recording_format'] = 'V'
        data['recording_technique'] = 'D'
        data['media_type'] = 'CES'

        record = self._decoder.decode(data)

        self.assertEqual('REC', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual(
            datetime.datetime.strptime('20030216', '%Y%m%d').date(),
            record.first_release_date)
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(),
                         record.first_release_duration)
        self.assertEqual('FIRST TITLE', record.first_album_title)
        self.assertEqual('FIRST LABEL', record.first_album_label)
        self.assertEqual('ABF35', record.first_release_catalog_n)
        self.assertEqual(1234567890123, record.ean)
        self.assertEqual('ES-A2B-12-12', record.isrc)
        self.assertEqual('V', record.recording_format)
        self.assertEqual('D', record.recording_technique)
        self.assertEqual('CES', record.media_type)
