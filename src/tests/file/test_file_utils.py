# -*- encoding: utf-8 -*-
import unittest

from commonworks.utils import cwr_file
from commonworks.file import FileIdentifier


"""
Unit tests to check if the CWR file utils work correctly.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestDecodeFileName(unittest.TestCase):
    """
    Tests the CWR file name decoding.

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
        data = cwr_file.decode_filename_updated(self.fn_s2_r2)

        self.assertEqual(2012, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        data = cwr_file.decode_filename_updated(self.fn_s3_r2)

        self.assertEqual(2013, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        data = cwr_file.decode_filename_updated(self.fn_s2_r3)

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        data = cwr_file.decode_filename_updated(self.fn_s3_r3)

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestDecodeFileNameOld(unittest.TestCase):
    """
    Tests the CWR file name decoding.

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
        data = cwr_file.decode_filename(self.fn_s2_r2)

        self.assertEqual(2012, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        data = cwr_file.decode_filename(self.fn_s3_r2)

        self.assertEqual(2013, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        data = cwr_file.decode_filename(self.fn_s2_r3)

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        data = cwr_file.decode_filename(self.fn_s3_r3)

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestEncodeFileName(unittest.TestCase):
    """
    Tests the CWR file name encoding.

    These files follow the CWyynnnnsss_rrr.Vxx pattern.
    """

    def setUp(self):
        # Sender with 2 digits and receiver with 2 digits
        self.fn_s2_r2 = FileIdentifier(2012, 123, '11', '22', 2.1)
        # Sender with 3 digits and receiver with 2 digits
        self.fn_s3_r2 = FileIdentifier(2013, 123, 'ABC', '23', 2.2)
        # Sender with 2 digits and receiver with 3 digits
        self.fn_s2_r3 = FileIdentifier(2099, 0, '22', 'DEC', 0)
        # Sender with 3 digits and receiver with 3 digits
        self.fn_s3_r3 = FileIdentifier(2000, 12, 'AB2', '234', 0.2)

    def test_s2_r2(self):
        data = cwr_file.encode_filename_updated(self.fn_s2_r2)

        self.assertEqual("CW12012311_22.V21", data)

    def test_s3_r2(self):
        data = cwr_file.encode_filename_updated(self.fn_s3_r2)

        self.assertEqual("CW130123ABC_23.V22", data)

    def test_s2_r3(self):
        data = cwr_file.encode_filename_updated(self.fn_s2_r3)

        self.assertEqual("CW99000022_DEC.V00", data)

    def test_s3_r3(self):
        data = cwr_file.encode_filename_updated(self.fn_s3_r3)

        self.assertEqual("CW000012AB2_234.V02", data)


class TestEncodeFileNameOld(unittest.TestCase):
    """
    Tests the CWR file name encoding.

    This tests against the old naming pattern.

    These files follow the CWyynnsss_rrr.Vxx pattern.
    """

    def setUp(self):
        # Sender with 2 digits and receiver with 2 digits
        self.fn_s2_r2 = FileIdentifier(2012, 23, '11', '22', 2.1)
        # Sender with 3 digits and receiver with 2 digits
        self.fn_s3_r2 = FileIdentifier(2013, 1, 'ABC', '23', 2.2)
        # Sender with 2 digits and receiver with 3 digits
        self.fn_s2_r3 = FileIdentifier(2099, 0, '22', 'DEC', 0)
        # Sender with 3 digits and receiver with 3 digits
        self.fn_s3_r3 = FileIdentifier(2000, 12, 'AB2', '234', 0.2)

    def test_s2_r2(self):
        data = cwr_file.encode_filename(self.fn_s2_r2)

        self.assertEqual("CW122311_22.V21", data)

    def test_s3_r2(self):
        data = cwr_file.encode_filename(self.fn_s3_r2)

        self.assertEqual("CW1301ABC_23.V22", data)

    def test_s2_r3(self):
        data = cwr_file.encode_filename(self.fn_s2_r3)

        self.assertEqual("CW990022_DEC.V00", data)

    def test_s3_r3(self):
        data = cwr_file.encode_filename(self.fn_s3_r3)

        self.assertEqual("CW0012AB2_234.V02", data)