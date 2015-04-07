# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import WorkOriginDictionaryDecoder
from cwr.other import VISAN


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkOriginDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WorkOriginDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'ORN'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['intended_purpose'] = 'PURPOSE'
        dict['production_title'] = 'TITLE'
        dict['cd_identifier'] = 'ID134'
        dict['cut_number'] = 5
        dict['library'] = 'LIB467'
        dict['bltvr'] = 'BLTVR'
        dict['visan'] = VISAN(1234567, 12345678912, 123, 1)
        dict['production_n'] = 'PROD145'
        dict['episode_title'] = 'EPISODE'
        dict['episode_n'] = 'EP145'
        dict['year_production'] = 1994
        dict['audio_visual_key'] = 'KEY'

        record = self._decoder.decode(dict)

        self.assertEqual('ORN', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('PURPOSE', record.intended_purpose)
        self.assertEqual('TITLE', record.production_title)
        self.assertEqual('ID134', record.cd_identifier)
        self.assertEqual(5, record.cut_number)
        self.assertEqual('LIB467', record.library)
        self.assertEqual('BLTVR', record.bltvr)
        self.assertEqual(1, record.visan.check_digit)
        self.assertEqual(123, record.visan.episode)
        self.assertEqual(12345678912, record.visan.isan)
        self.assertEqual(1234567, record.visan.version)
        self.assertEqual('PROD145', record.production_n)
        self.assertEqual('EPISODE', record.episode_title)
        self.assertEqual('EP145', record.episode_n)
        self.assertEqual(1994, record.year_production)
        self.assertEqual('KEY', record.audio_visual_key)