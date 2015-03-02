# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar import publisher

"""
CWR file Publisher parsing tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPublisherRecordValid(unittest.TestCase):
    """
    Tests that the Publisher Record grammar decodes correctly formatted strings
    """

    def setUp(self):
        self.grammar = publisher.publisher

    def test_valid_full(self):
        """
        Tests that Publisher Record grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        prefix = 'SPU000012340000002319A12345678PUBLISHER NAME                               NE 92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        result = self.grammar.parseString(prefix)[0]

        self.assertEqual('SPU', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(19, result.sequence_n)
        self.assertEqual('A12345678', result.publisher.ip_id)
        self.assertEqual('PUBLISHER NAME', result.publisher.name)
        self.assertEqual('N', result.publisher_unknown)
        self.assertEqual('E', result.publisher_type)
        self.assertEqual('923703412', result.publisher.tax_id)
        self.assertEqual(14107338, result.publisher.ipi_name)
        self.assertEqual('A0123456789123', result.agreement_id)
        self.assertEqual(9, result.pr_society)
        self.assertEqual(20.5, result.pr_owner_share)
        self.assertEqual(10, result.mr_society)
        self.assertEqual(30, result.mr_owner_share)
        self.assertEqual(11, result.sr_society)
        self.assertEqual(23.12, result.sr_owner_share)
        self.assertEqual('B', result.special_agreements)
        self.assertEqual('Y', result.first_record_refusal)
        self.assertEqual('I', result.publisher.ipi_base_id.header)
        self.assertEqual(229, result.publisher.ipi_base_id.id_code)
        self.assertEqual(7, result.publisher.ipi_base_id.check_digit)
        self.assertEqual('A0123456789124', result.isac)
        self.assertEqual('A0123456789125', result.society_agreement_id)
        self.assertEqual('OS', result.agreement_type)
        self.assertEqual('B', result.usa_license)