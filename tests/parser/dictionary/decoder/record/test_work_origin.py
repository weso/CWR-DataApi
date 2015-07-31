# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import WorkOriginDictionaryDecoder
from cwr.other import VISAN

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWorkOriginDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WorkOriginDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'ORN'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['intended_purpose'] = 'PURPOSE'
        data['production_title'] = 'TITLE'
        data['cd_identifier'] = 'ID134'
        data['cut_number'] = 5
        data['library'] = 'LIB467'
        data['bltvr'] = 'BLTVR'
        data['visan'] = 1234567123456789121231
        data['production_n'] = 'PROD145'
        data['episode_title'] = 'EPISODE'
        data['episode_n'] = 'EP145'
        data['year_production'] = 1994
        data['audio_visual_key'] = 'KEY'

        record = self._decoder.decode(data)

        self.assertEqual('ORN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('PURPOSE', record.intended_purpose)
        self.assertEqual('TITLE', record.production_title)
        self.assertEqual('ID134', record.cd_identifier)
        self.assertEqual(5, record.cut_number)
        self.assertEqual('LIB467', record.library)
        self.assertEqual('BLTVR', record.bltvr)
        self.assertEqual(1234567123456789121231, record.visan)
        self.assertEqual('PROD145', record.production_n)
        self.assertEqual('EPISODE', record.episode_title)
        self.assertEqual('EP145', record.episode_n)
        self.assertEqual(1994, record.year_production)
        self.assertEqual('KEY', record.audio_visual_key)
