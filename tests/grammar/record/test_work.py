# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Work Origin grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('work')

    def test_valid_common(self):
        record = 'NWR0000019900000000WORK NAME                                                     1450455                  00000000            UNC000000YMTX   ORI   ORIORI                                          N00000000000U                                                  Y'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NWR', result.record_type)
        self.assertEqual(199, result.transaction_sequence_n)
        self.assertEqual(0, result.record_sequence_n)
        self.assertEqual('WORK NAME', result.title)
        self.assertEqual(None, result.language_code)
        self.assertEqual('1450455', result.submitter_work_n)
        self.assertEqual(None, result.iswc)
        self.assertEqual(None, result.copyright_date)
        self.assertEqual(None, result.copyright_number)
        self.assertEqual('UNC', result.musical_work_distribution_category)
        self.assertEqual(0, result.duration.hour)
        self.assertEqual(0, result.duration.minute)
        self.assertEqual(0, result.duration.second)
        self.assertEqual('Y', result.recorded_indicator)
        self.assertEqual('MTX', result.text_music_relationship)
        self.assertEqual(None, result.composite_type)
        self.assertEqual('ORI', result.version_type)
        self.assertEqual(None, result.excerpt_type)
        self.assertEqual('ORI', result.music_arrangement)
        self.assertEqual('ORI', result.lyric_adaptation)
        self.assertEqual(None, result.contact_name)
        self.assertEqual(None, result.contact_id)
        self.assertEqual(None, result.work_type)
        self.assertEqual(False, result.grand_rights_indicator)
        self.assertEqual(0, result.composite_component_count)
        self.assertEqual(None, result.date_publication_printed_edition)
        self.assertEqual('U', result.exceptional_clause)
        self.assertEqual(None, result.opus_number)
        self.assertEqual(None, result.catalogue_number)
        self.assertEqual('Y', result.priority_flag)