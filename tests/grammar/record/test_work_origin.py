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


class TestWorkOriginGrammar(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('work_origin')

    def test_valid_full(self):
        record = 'ORN0000123400000023LIBPRODUCTION TITLE                                            IDENTIFIER     1234THE LIBRARY                                                 B1234567812345678901212341ABDFE       EPISODE TITLE                                               ABD12345            2012123ABDEFG                   '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ORN', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('LIB', result.intended_purpose)
        self.assertEqual('PRODUCTION TITLE', result.production_title)
        self.assertEqual('IDENTIFIER', result.cd_identifier)
        self.assertEqual(1234, result.cut_number)
        self.assertEqual('THE LIBRARY', result.library)
        self.assertEqual('B', result.bltvr)
        self.assertEqual(12345678, result.visan.version)
        self.assertEqual(123456789012, result.visan.isan)
        self.assertEqual(1234, result.visan.episode)
        self.assertEqual(1, result.visan.check_digit)
        self.assertEqual('ABDFE', result.production_n)
        self.assertEqual('EPISODE TITLE', result.episode_title)
        self.assertEqual('ABD12345', result.episode_n)
        self.assertEqual(2012, result.year_production)
        self.assertEqual(123, result.audio_visual_key.society_code)
        self.assertEqual('ABDEFG', result.audio_visual_key.av_number)