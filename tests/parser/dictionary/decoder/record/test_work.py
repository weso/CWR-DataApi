# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import WorkDictionaryDecoder
from cwr.other import ISWCCode

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWorkDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WorkDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'NWR'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['submitter_work_n'] = 'ABC123'
        dict['title'] = 'TITLE'
        dict['version_type'] = 'ORI'
        dict['musical_work_distribution_category'] = 'SER'
        dict['date_publication_printed_edition'] = datetime.datetime.strptime('20030216', '%Y%m%d').date()
        dict['text_music_relationship'] = 'MTX'
        dict['language_code'] = 'ES'
        dict['copyright_number'] = 'ABDF146'
        dict['copyright_date'] = datetime.datetime.strptime('20030217', '%Y%m%d').date()
        dict['music_arrangement'] = 'ORI'
        dict['lyric_adaptation'] = 'MOD'
        dict['excerpt_type'] = 'MOV'
        dict['composite_type'] = 'MED'
        dict['composite_component_count'] = 5
        dict['iswc'] = ISWCCode(12345678, 9)
        dict['work_type'] = 'BL'
        dict['duration'] = datetime.datetime.strptime('011200', '%H%M%S').time()
        dict['catalogue_number'] = 'GGH97'
        dict['opus_number'] = 'OP35'
        dict['contact_id'] = '123CONTACT'
        dict['contact_name'] = 'THE CONTACT'
        dict['recorded_indicator'] = 'Y'
        dict['priority_flag'] = 'Y'
        dict['exceptional_clause'] = 'Y'
        dict['grand_rights_indicator'] = True

        record = self._decoder.decode(dict)

        self.assertEqual('NWR', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('ABC123', record.submitter_work_n)
        self.assertEqual('TITLE', record.title)
        self.assertEqual('ORI', record.version_type)
        self.assertEqual('SER', record.musical_work_distribution_category)
        self.assertEqual(datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                         record.date_publication_printed_edition)
        self.assertEqual('MTX', record.text_music_relationship)
        self.assertEqual('ES', record.language_code)
        self.assertEqual('ABDF146', record.copyright_number)
        self.assertEqual(datetime.datetime.strptime('20030217', '%Y%m%d').date(), record.copyright_date)
        self.assertEqual('ORI', record.music_arrangement)
        self.assertEqual('MOD', record.lyric_adaptation)
        self.assertEqual('MOV', record.excerpt_type)
        self.assertEqual('MED', record.composite_type)
        self.assertEqual(5, record.composite_component_count)
        self.assertEqual(12345678, record.iswc.id_code)
        self.assertEqual(9, record.iswc.check_digit)
        self.assertEqual('BL', record.work_type)
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(), record.duration)
        self.assertEqual('GGH97', record.catalogue_number)
        self.assertEqual('OP35', record.opus_number)
        self.assertEqual('123CONTACT', record.contact_id)
        self.assertEqual('THE CONTACT', record.contact_name)
        self.assertEqual('Y', record.recorded_indicator)
        self.assertEqual('Y', record.priority_flag)
        self.assertEqual('Y', record.exceptional_clause)
        self.assertEqual(True, record.grand_rights_indicator)
