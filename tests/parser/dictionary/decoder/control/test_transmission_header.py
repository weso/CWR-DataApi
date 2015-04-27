# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.dictionary import TransmissionHeaderDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionHeaderDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = TransmissionHeaderDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'HDR'
        dict['sender_id'] = 'SND123'
        dict['sender_name'] = 'THE SENDER'
        dict['sender_type'] = 'SO'
        dict['creation_date_time'] = datetime.datetime.strptime('20030216', '%Y%m%d').date()
        dict['transmission_date'] = datetime.datetime.strptime('20030217', '%Y%m%d').date()
        dict['edi_standard'] = '01.10'
        dict['character_set'] = 'ASCII'

        record = self._decoder.decode(dict)

        self.assertEqual('HDR', record.record_type)
        self.assertEqual('SND123', record.sender_id)
        self.assertEqual('THE SENDER', record.sender_name)
        self.assertEqual('SO', record.sender_type)
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(), record.creation_date_time)
        self.assertEqual(datetime.datetime.strptime('20030217', '%Y%m%d').date(), record.transmission_date)
        self.assertEqual('01.10', record.edi_standard)
        self.assertEqual('ASCII', record.character_set)