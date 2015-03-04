# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import nra_record


"""
CWR Non-Roman Alphabet Publisher Name grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPRGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = nra_record.npr

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'NPR0000123400000023NAME                                                                                                                                                            FIRST NAME                                                                                                                                                      00014107338I-000000229-7ESENCAN'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('NPR', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('NAME', result.name)
        self.assertEqual('FIRST NAME', result.first_name)
        self.assertEqual(14107338, result.ipi_name)
        self.assertEqual('I', result.ipi_base.header)
        self.assertEqual(229, result.ipi_base.id_code)
        self.assertEqual(7, result.ipi_base.check_digit)
        self.assertEqual('ES', result.language)
        self.assertEqual('EN', result.performance_language)
        self.assertEqual('CAN', result.performance_dialect)