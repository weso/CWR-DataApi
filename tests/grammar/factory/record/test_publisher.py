# -*- coding: utf-8 -*-
import unittest

from tests.utils.grammar import getCommonGrammar

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
        self.grammar = getCommonGrammar('publisher')

    def test_common(self):
        record = 'SPU00000179000005380166       THE MUSIC SOCIETY                             E          002501650060399357851805061 0025061 0050061 00500   0000000000000                            OS '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPU', result.record_type)
        self.assertEqual(179, result.transaction_sequence_n)
        self.assertEqual(538, result.record_sequence_n)
        self.assertEqual(1, result.publisher_sequence_n)
        self.assertEqual('66', result.publisher.ip_n)
        self.assertEqual('THE MUSIC SOCIETY', result.publisher.publisher_name)
        self.assertEqual(None, result.publisher_unknown)
        self.assertEqual('E', result.publisher_type)
        self.assertEqual(None, result.publisher.tax_id)
        self.assertEqual(250165006, result.publisher.ipi_name_n)
        self.assertEqual('03993578518050', result.submitter_agreement_n)
        self.assertEqual(61, result.pr_society)
        self.assertEqual(2.5, result.pr_ownership_share)
        self.assertEqual(61, result.mr_society)
        self.assertEqual(5, result.mr_ownership_share)
        self.assertEqual(61, result.sr_society)
        self.assertEqual(5, result.sr_ownership_share)
        self.assertEqual(None, result.special_agreements)
        self.assertEqual(None, result.first_recording_refusal)
        self.assertEqual(0, result.publisher.ipi_base_n)
        self.assertEqual(None, result.international_standard_code)
        self.assertEqual(None, result.society_assigned_agreement_n)
        self.assertEqual('OS', result.agreement_type)
        self.assertEqual(None, result.usa_license)

    def test_valid_full(self):
        """
        Tests that Publisher Record grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPU', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(19, result.publisher_sequence_n)
        self.assertEqual('A12345678', result.publisher.ip_n)
        self.assertEqual('PUBLISHER NAME', result.publisher.publisher_name)
        self.assertEqual(None, result.publisher_unknown)
        self.assertEqual('AQ', result.publisher_type)
        self.assertEqual(923703412, result.publisher.tax_id)
        self.assertEqual(14107338, result.publisher.ipi_name_n)
        self.assertEqual('A0123456789123', result.submitter_agreement_n)
        self.assertEqual(9, result.pr_society)
        self.assertEqual(20.5, result.pr_ownership_share)
        self.assertEqual(10, result.mr_society)
        self.assertEqual(30, result.mr_ownership_share)
        self.assertEqual(11, result.sr_society)
        self.assertEqual(23.12, result.sr_ownership_share)
        self.assertEqual('B', result.special_agreements)
        self.assertEqual('Y', result.first_recording_refusal)
        self.assertEqual('I', result.publisher.ipi_base_n.header)
        self.assertEqual(229, result.publisher.ipi_base_n.id_code)
        self.assertEqual(7, result.publisher.ipi_base_n.check_digit)
        self.assertEqual('A0123456789124', result.international_standard_code)
        self.assertEqual('A0123456789125', result.society_assigned_agreement_n)
        self.assertEqual('OS', result.agreement_type)
        self.assertEqual('B', result.usa_license)

    def test_valid_min(self):
        """
        Tests that Publisher Record grammar decodes correctly formatted record prefixes.

        This test contains none of the optional fields.
        """
        record = 'OPU000012340000002319                                                      Y  00000000000000000000                 00000   00000   00000                                               '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('OPU', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(19, result.publisher_sequence_n)
        self.assertEqual(None, result.publisher.ip_n)
        self.assertEqual(None, result.publisher.publisher_name)
        self.assertEqual('Y', result.publisher_unknown)
        self.assertEqual(None, result.publisher_type)
        self.assertEqual(0, result.publisher.tax_id)
        self.assertEqual(0, result.publisher.ipi_name_n)
        self.assertEqual(None, result.submitter_agreement_n)
        self.assertEqual(None, result.pr_society)
        self.assertEqual(0, result.pr_ownership_share)
        self.assertEqual(None, result.mr_society)
        self.assertEqual(0, result.mr_ownership_share)
        self.assertEqual(None, result.sr_society)
        self.assertEqual(0, result.sr_ownership_share)
        self.assertEqual(None, result.special_agreements)
        self.assertEqual(None, result.first_recording_refusal)
        self.assertEqual(None, result.publisher.ipi_base_n)
        self.assertEqual(None, result.international_standard_code)
        self.assertEqual(None, result.society_assigned_agreement_n)
        self.assertEqual(None, result.agreement_type)
        self.assertEqual(None, result.usa_license)


class TestPublisherRecordException(unittest.TestCase):
    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = DefaultPrefixBuilder(_config.record_types(), _factory_field)
        _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_record('publisher')

    def test_no_acquiror_performing_shares(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                PA92370341200014107338A0123456789123009020500100000001100000BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_no_acquiror_mechanization_shares(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                PA92370341200014107338A0123456789123009000000100100001100000BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_no_acquiror_synchronization_shares(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                PA92370341200014107338A0123456789123009000000100000001100100BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_sequence_number_0(self):
        record = 'SPU000012340000002300A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_acquiror_missing_shares(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009000000100000001100000BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_controlled_has_no_name(self):
        record = 'SPU000012340000002319A12345678                                              AQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_known_has_no_name(self):
        record = 'OPU000012340000002319A12345678                                             NAQ92370341200014107338A0123456789123009020500100300001102312LY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_controlled_has_no_type(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                               N  92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_controlled_unknown(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                               NAQ92370341200014107338A0123456789123009020500100300001102312LY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_not_controlled_unknown_blank(self):
        record = 'OPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009020500100300001102312LY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_not_controlled_unknown_has_name(self):
        record = 'OPU000012340000002319A12345678PUBLISHER NAME                               YAQ92370341200014107338A0123456789123009020500100300001102312LY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_pr_share_above_50(self):
        record = 'SPU000012340000002319A12345678PUBLISHER NAME                                AQ92370341200014107338A0123456789123009051000100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_opu_bad_special_indicator(self):
        record = 'OPU000012340000002319A12345678PUBLISHER NAME                               NAQ92370341200014107338A0123456789123009020500100300001102312BY I-000000229-7A0123456789124A0123456789125OSB'

        # self.assertRaises(ParseException, self.grammar.parseString, record)