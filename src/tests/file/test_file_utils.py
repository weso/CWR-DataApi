# -*- encoding: utf-8 -*-
import unittest

from commonworks.utils import cwr_file


"""
Unit tests to check if the CWR file utils work correctly.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestParseFileName(unittest.TestCase):
    """
    Tests the CWR file name parsing.

    These files follow the CWyynnnnsss_rrr.Vxx pattern.
    """

    def setUp(self):
        # Sender with 2 digits and receiver with 2 digits
        self.fn_s2_r2 = "CW12012311_22.V21"
        # Sender with 3 digits and receiver with 2 digits
        self.fn_s3_r2 = "CW130123ABC_23.V22"
        # Sender with 2 digits and receiver with 3 digits
        self.fn_s2_r3 = "CW99000022_DEC.V00"
        # Sender with 3 digits and receiver with 3 digits
        self.fn_s3_r3 = "CW000012AB2_234.V02"

    def test_s2_r2(self):
        data = cwr_file.parse_filename(self.fn_s2_r2)

        self.assertEqual(12, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(21, data.version)

    def test_s3_r2(self):
        data = cwr_file.parse_filename(self.fn_s3_r2)

        self.assertEqual(13, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(22, data.version)

    def test_s2_r3(self):
        data = cwr_file.parse_filename(self.fn_s2_r3)

        self.assertEqual(99, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(00, data.version)

    def test_s3_r3(self):
        data = cwr_file.parse_filename(self.fn_s3_r3)

        self.assertEqual(00, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2, data.version)


class TestParseFileNameOld(unittest.TestCase):
    """
    Tests the CWR file name parsing.

    This tests against the old naming pattern.

    These files follow the CWyynnsss_rrr.Vxx pattern.
    """

    def setUp(self):
        # Sender with 2 digits and receiver with 2 digits
        self.fn_s2_r2 = "CW122311_22.V21"
        # Sender with 3 digits and receiver with 2 digits
        self.fn_s3_r2 = "CW1301ABC_23.V22"
        # Sender with 2 digits and receiver with 3 digits
        self.fn_s2_r3 = "CW990022_DEC.V00"
        # Sender with 3 digits and receiver with 3 digits
        self.fn_s3_r3 = "CW0012AB2_234.V02"

    def test_s2_r2(self):
        data = cwr_file.parse_filename_old(self.fn_s2_r2)

        self.assertEqual(12, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(21, data.version)

    def test_s3_r2(self):
        data = cwr_file.parse_filename_old(self.fn_s3_r2)

        self.assertEqual(13, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(22, data.version)

    def test_s2_r3(self):
        data = cwr_file.parse_filename_old(self.fn_s2_r3)

        self.assertEqual(99, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(00, data.version)

    def test_s3_r3(self):
        data = cwr_file.parse_filename_old(self.fn_s3_r3)

        self.assertEqual(00, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2, data.version)