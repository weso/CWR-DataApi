# -*- coding: utf-8 -*-

import unittest

from cwr.parser.file import CWRFileNameEncoder, CWRFileNameEncoderOld, CWRFileNameDecoder
from cwr.file import FileTag


"""
CWR file name encoder tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileNameCWRDecodeValid(unittest.TestCase):
    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_old(self):
        result = self._parser.decode('CW122311_22.V21')

        self.assertEqual(2012, result.year)
        self.assertEqual(23, result.sequence_n)
        self.assertEqual('11', result.sender)
        self.assertEqual('22', result.receiver)
        self.assertEqual(2.1, result.version)

    def test_new(self):
        result = self._parser.decode('CW12012311_22.V21')

        self.assertEqual(2012, result.year)
        self.assertEqual(123, result.sequence_n)
        self.assertEqual('11', result.sender)
        self.assertEqual('22', result.receiver)
        self.assertEqual(2.1, result.version)


class TestFileNameCWRDecodeInvalid(unittest.TestCase):
    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_invalid(self):
        result = self._parser.decode('CW130001059_201_.txt')

        self.assertEqual(0, result.year)
        self.assertEqual(0, result.sequence_n)
        self.assertEqual('', result.sender)
        self.assertEqual('', result.receiver)
        self.assertEqual('', result.version)


class TestFileNameCWREncodeValid(unittest.TestCase):
    """
    Tests that CWRFileNameEncoder encodes valid FileTags (using the new format)
    """

    def setUp(self):
        self._parser = CWRFileNameEncoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.encode(FileTag(2012, 123, '11', '22', 2.1))

        self.assertEqual("CW12012311_22.V21", data)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.encode(FileTag(2013, 123, 'ABC', '23', 2.2))

        self.assertEqual("CW130123ABC_23.V22", data)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(2099, 0, '22', 'DEC', 0))

        self.assertEqual("CW99000022_DEC.V00", data)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(2000, 12, 'AB2', '234', 0.2))

        self.assertEqual("CW000012AB2_234.V02", data)

    def test_s3_r3_old_year(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(1960, 12, 'AB2', '234', 0.2))

        self.assertEqual("CW600012AB2_234.V02", data)

    def test_s3_r3_short_year(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(60, 12, 'AB2', '234', 0.2))

        self.assertEqual("CW600012AB2_234.V02", data)


class TestFileNameCWREncodeValidOld(unittest.TestCase):
    """
    Tests that CWRFileNameEncoder encodes valid FileTags (using the old format)
    """

    def setUp(self):
        self._parser = CWRFileNameEncoderOld()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.encode(FileTag(2012, 23, '11', '22', 2.1))

        self.assertEqual("CW122311_22.V21", data)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.encode(FileTag(2013, 1, 'ABC', '23', 2.2))

        self.assertEqual("CW1301ABC_23.V22", data)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(2099, 0, '22', 'DEC', 0))

        self.assertEqual("CW990022_DEC.V00", data)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.encode(FileTag(2000, 12, 'AB2', '234', 0.2))

        self.assertEqual("CW0012AB2_234.V02", data)

