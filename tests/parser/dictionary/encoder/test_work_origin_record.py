# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.work import WorkOriginRecord
from cwr.other import VISAN


"""
WorkOriginRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkOriginRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        visan = VISAN(1234567, 12345678912, 123, 1)

        data = WorkOriginRecord(record_type='ORN',
                                transaction_sequence_n=3,
                                record_sequence_n=15,
                                intended_purpose='PURPOSE',
                                production_title='TITLE',
                                cd_identifier='ID134',
                                cut_number=5,
                                library='LIB467',
                                bltvr='BLTVR',
                                visan=visan,
                                production_n='PROD145',
                                episode_title='EPISODE',
                                episode_n='EP145',
                                year_production=1994,
                                audio_visual_key='KEY')

        encoded = self._encoder.encode(data)

        self.assertEqual('ORN', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('PURPOSE', encoded['intended_purpose'])
        self.assertEqual('TITLE', encoded['production_title'])
        self.assertEqual('ID134', encoded['cd_identifier'])
        self.assertEqual(5, encoded['cut_number'])
        self.assertEqual('LIB467', encoded['library'])
        self.assertEqual('BLTVR', encoded['bltvr'])
        self.assertEqual(visan.check_digit, encoded['visan'].check_digit)
        self.assertEqual(visan.episode, encoded['visan'].episode)
        self.assertEqual(visan.isan, encoded['visan'].isan)
        self.assertEqual(visan.version, encoded['visan'].version)
        self.assertEqual('PROD145', encoded['production_n'])
        self.assertEqual('EPISODE', encoded['episode_title'])
        self.assertEqual('EP145', encoded['episode_n'])
        self.assertEqual(1994, encoded['year_production'])
        self.assertEqual('KEY', encoded['audio_visual_key'])