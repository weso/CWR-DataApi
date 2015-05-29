# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import TransmissionHeaderDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestTransmissionHeaderDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = TransmissionHeaderDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'HDR'
        data['sender_id'] = 'SND123'
        data['sender_name'] = 'THE SENDER'
        data['sender_type'] = 'SO'
        data['creation_date_time'] = datetime.datetime.strptime('20030216', '%Y%m%d').date()
        data['transmission_date'] = datetime.datetime.strptime('20030217', '%Y%m%d').date()
        data['edi_standard'] = '01.10'
        data['character_set'] = 'ASCII'

        record = self._decoder.decode(data)

        self.assertEqual('HDR', record.record_type)
        self.assertEqual('SND123', record.sender_id)
        self.assertEqual('THE SENDER', record.sender_name)
        self.assertEqual('SO', record.sender_type)
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(), record.creation_date_time)
        self.assertEqual(datetime.datetime.strptime('20030217', '%Y%m%d').date(), record.transmission_date)
        self.assertEqual('01.10', record.edi_standard)
        self.assertEqual('ASCII', record.character_set)
