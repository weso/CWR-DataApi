# -*- encoding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.record import acknowledgement

"""
CWR acknowledgement grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAcknowledgementAgreementValid(unittest.TestCase):
    def setUp(self):
        self.grammar = acknowledgement.acknowledgement

    def test_valid_full(self):
        """
        Tests that the Acknowledgement grammar parses correctly formatted strings.

        This test contains all the optional fields.
        """
        record = 'ACK0000123400000023201201021020300123401234567AGRTHE CREATION TITLE                                          ABCD1234512345123456ABCD123451234512345720130203AS'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ACK', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(2012, result.creation_date_time.year)
        self.assertEqual(1, result.creation_date_time.month)
        self.assertEqual(2, result.creation_date_time.day)
        self.assertEqual(10, result.creation_date_time.hour)
        self.assertEqual(20, result.creation_date_time.minute)
        self.assertEqual(30, result.creation_date_time.second)
        self.assertEqual(1234, result.group_id)
        self.assertEqual(1234567, result.transaction_n)
        self.assertEqual('AGR', result.transaction_type)
        self.assertEqual('THE CREATION TITLE', result.title)
        self.assertEqual('ABCD1234512345123456', result.submitter_id)
        self.assertEqual('ABCD1234512345123457', result.recipient_id)
        self.assertEqual(2013, result.processing_date.year)
        self.assertEqual(2, result.processing_date.month)
        self.assertEqual(3, result.processing_date.day)
        self.assertEqual('AS', result.transaction_status)

    def test_valid_min(self):
        """
        Tests that the Acknowledgement grammar parses correctly formatted strings.

        This test contains none of the optional fields.
        """
        record = 'ACK0000123400000023201201021020300123401234567AGR                                                                                                    20130203AS'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('ACK', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(2012, result.creation_date_time.year)
        self.assertEqual(1, result.creation_date_time.month)
        self.assertEqual(2, result.creation_date_time.day)
        self.assertEqual(10, result.creation_date_time.hour)
        self.assertEqual(20, result.creation_date_time.minute)
        self.assertEqual(30, result.creation_date_time.second)
        self.assertEqual(1234, result.group_id)
        self.assertEqual(1234567, result.transaction_n)
        self.assertEqual('AGR', result.transaction_type)
        self.assertEqual('', result.title)
        self.assertEqual('', result.submitter_id)
        self.assertEqual('', result.recipient_id)
        self.assertEqual(2013, result.processing_date.year)
        self.assertEqual(2, result.processing_date.month)
        self.assertEqual(3, result.processing_date.day)
        self.assertEqual('AS', result.transaction_status)


class TestAcknowledgementAgreementException(unittest.TestCase):
    def setUp(self):
        self.grammar = acknowledgement.acknowledgement

    def test_nwr_missing_title(self):
        """
        Tests that a exception is thrown when the Original Transaction Type is NWR and not Creation Title is set.
        """
        record = 'ACK0000123400000023201201021020300123401234567NWR                                                            ABCD1234512345123456ABCD123451234512345720130203AS'

        self.assertRaises(ParseException, self.grammar.parseString, record)

    def test_rev_missing_title(self):
        """
        Tests that a exception is thrown when the Original Transaction Type is NWR and not Creation Title is set.
        """
        record = 'ACK0000123400000023201201021020300123401234567REV                                                            ABCD1234512345123456ABCD123451234512345720130203AS'

        self.assertRaises(ParseException, self.grammar.parseString, record)