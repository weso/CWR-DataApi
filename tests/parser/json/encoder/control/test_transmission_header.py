# -*- coding: utf-8 -*-

import unittest
import datetime
import json

from cwr.parser.cwrjson import JSONEncoder
from cwr.transmission import TransmissionHeader


"""
TransmissionHeader to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestTransmissionHeaderDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_encoded(self):
        data = TransmissionHeader(record_type='HDR',
                                  sender_id='ABC334',
                                  sender_name='SENDER',
                                  sender_type='SO',
                                  creation_date_time=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                                  transmission_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                                  edi_standard='01.10',
                                  character_set='ASCII')

        encoded = self._encoder.encode(data)

        encoded = json.loads(encoded)

        self.assertEqual('HDR', encoded['record_type'])
        self.assertEqual('ABC334', encoded['sender_id'])
        self.assertEqual('SENDER', encoded['sender_name'])
        self.assertEqual('SO', encoded['sender_type'])
        self.assertEqual('2003-02-16', encoded['creation_date_time'])
        self.assertEqual('2003-02-17', encoded['transmission_date'])
        self.assertEqual('01.10', encoded['edi_standard'])
        self.assertEqual('ASCII', encoded['character_set'])