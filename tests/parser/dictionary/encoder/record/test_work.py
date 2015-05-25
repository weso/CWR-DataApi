# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.encoder.dictionary import WorkDictionaryEncoder
from cwr.work import WorkRecord
from cwr.other import ISWCCode

"""
WorkRecord to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = WorkDictionaryEncoder()

    def test_encoded(self):
        iswc = ISWCCode(12345678, 9)

        data = WorkRecord(record_type='NWR',
                          transaction_sequence_n=3,
                          record_sequence_n=15,
                          submitter_work_n='ABC123',
                          title='TITLE',
                          version_type='ORI',
                          musical_work_distribution_category='SER',
                          date_publication_printed_edition=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                          text_music_relationship='MTX',
                          language_code='ES',
                          copyright_number='ABDF146',
                          copyright_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                          music_arrangement='ORI',
                          lyric_adaptation='MOD',
                          excerpt_type='MOV',
                          composite_type='MED',
                          composite_component_count=5,
                          iswc=iswc,
                          work_type='BL',
                          duration=datetime.datetime.strptime('011200', '%H%M%S').time(),
                          catalogue_number='GGH97',
                          opus_number='OP35',
                          contact_id='123CONTACT',
                          contact_name='THE CONTACT',
                          recorded_indicator='Y',
                          priority_flag='Y',
                          exceptional_clause='Y',
                          grand_rights_indicator=True)

        encoded = self._encoder.encode(data)

        self.assertEqual('NWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('ABC123', encoded['submitter_work_n'])
        self.assertEqual('TITLE', encoded['title'])
        self.assertEqual('ORI', encoded['version_type'])
        self.assertEqual('SER', encoded['musical_work_distribution_category'])
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                         encoded['date_publication_printed_edition'])
        self.assertEqual('MTX', encoded['text_music_relationship'])
        self.assertEqual('ES', encoded['language_code'])
        self.assertEqual('ABDF146', encoded['copyright_number'])
        self.assertEqual(datetime.datetime.strptime('20030217', '%Y%m%d').date(), encoded['copyright_date'])
        self.assertEqual('ORI', encoded['music_arrangement'])
        self.assertEqual('MOD', encoded['lyric_adaptation'])
        self.assertEqual('MOV', encoded['excerpt_type'])
        self.assertEqual('MED', encoded['composite_type'])
        self.assertEqual(5, encoded['composite_component_count'])
        self.assertEqual('BL', encoded['work_type'])
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(), encoded['duration'])
        self.assertEqual('GGH97', encoded['catalogue_number'])
        self.assertEqual('OP35', encoded['opus_number'])
        self.assertEqual('123CONTACT', encoded['contact_id'])
        self.assertEqual('THE CONTACT', encoded['contact_name'])
        self.assertEqual('Y', encoded['recorded_indicator'])
        self.assertEqual('Y', encoded['priority_flag'])
        self.assertEqual('Y', encoded['exceptional_clause'])
        self.assertEqual(True, encoded['grand_rights_indicator'])

        self.assertEqual(12345678, encoded['iswc']['id_code'])
        self.assertEqual(9, encoded['iswc']['check_digit'])

    def test_encoded_no_iswc(self):
        iswc = None

        data = WorkRecord(record_type='NWR',
                          transaction_sequence_n=3,
                          record_sequence_n=15,
                          submitter_work_n='ABC123',
                          title='TITLE',
                          version_type='ORI',
                          musical_work_distribution_category='SER',
                          date_publication_printed_edition=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                          text_music_relationship='MTX',
                          language_code='ES',
                          copyright_number='ABDF146',
                          copyright_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                          music_arrangement='ORI',
                          lyric_adaptation='MOD',
                          excerpt_type='MOV',
                          composite_type='MED',
                          composite_component_count=5,
                          iswc=iswc,
                          work_type='BL',
                          duration=datetime.datetime.strptime('011200', '%H%M%S').time(),
                          catalogue_number='GGH97',
                          opus_number='OP35',
                          contact_id='123CONTACT',
                          contact_name='THE CONTACT',
                          recorded_indicator='Y',
                          priority_flag='Y',
                          exceptional_clause='Y',
                          grand_rights_indicator=True)

        encoded = self._encoder.encode(data)

        self.assertEqual('NWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('ABC123', encoded['submitter_work_n'])
        self.assertEqual('TITLE', encoded['title'])
        self.assertEqual('ORI', encoded['version_type'])
        self.assertEqual('SER', encoded['musical_work_distribution_category'])
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                         encoded['date_publication_printed_edition'])
        self.assertEqual('MTX', encoded['text_music_relationship'])
        self.assertEqual('ES', encoded['language_code'])
        self.assertEqual('ABDF146', encoded['copyright_number'])
        self.assertEqual(datetime.datetime.strptime('20030217', '%Y%m%d').date(), encoded['copyright_date'])
        self.assertEqual('ORI', encoded['music_arrangement'])
        self.assertEqual('MOD', encoded['lyric_adaptation'])
        self.assertEqual('MOV', encoded['excerpt_type'])
        self.assertEqual('MED', encoded['composite_type'])
        self.assertEqual(5, encoded['composite_component_count'])
        self.assertEqual('BL', encoded['work_type'])
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(), encoded['duration'])
        self.assertEqual('GGH97', encoded['catalogue_number'])
        self.assertEqual('OP35', encoded['opus_number'])
        self.assertEqual('123CONTACT', encoded['contact_id'])
        self.assertEqual('THE CONTACT', encoded['contact_name'])
        self.assertEqual('Y', encoded['recorded_indicator'])
        self.assertEqual('Y', encoded['priority_flag'])
        self.assertEqual('Y', encoded['exceptional_clause'])
        self.assertEqual(True, encoded['grand_rights_indicator'])

        self.assertEqual(None, encoded['iswc'])
