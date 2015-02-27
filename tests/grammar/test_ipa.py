# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import ipa


"""
CWR Interested Party in Agreement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseIPA(unittest.TestCase):
    """
    Tests that the IPA grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = ipa.ipa

    def test_valid_full(self):
        """
        Tests that IPA grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'IPA0000123400000023ACI-000000229-701234567890A12345678LAST NAME                                    FIRST NAME                    009020500100300001102312'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('IPA', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('AC', result.agreement_role_code)
        self.assertEqual(1234567890, result.ipi)
        self.assertEqual('I', result.ipi_name.header)
        self.assertEqual(229, result.ipi_name.id_code)
        self.assertEqual(7, result.ipi_name.check_digit)
        self.assertEqual('A12345678', result.ip_id)
        self.assertEqual('LAST NAME', result.last_name)
        self.assertEqual('FIRST NAME', result.writer_name)
        self.assertEqual(9, result.pr_society)
        self.assertEqual(20.5, result.pr_share)
        self.assertEqual(10, result.mr_society)
        self.assertEqual(30, result.mr_share)
        self.assertEqual(11, result.sr_society)
        self.assertEqual(023.12, result.sr_share)
