# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables

from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Non-Roman Alphabet Other Writer Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNOWGrammar(unittest.TestCase):
    """
    Tests that the NPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('nra_other_writer')

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NOW0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      ES1'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NOW', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME', result.writer_name)
        self.assertEqual('FIRST NAME', result.writer_first_name)
        self.assertEqual('ES', result.language_code)
        self.assertEqual(1, result.position)