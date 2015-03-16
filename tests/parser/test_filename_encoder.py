# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder import CWRFileNameEncoder, CWRFileNameEncoderOld
from cwr.file import FileTag


"""
CWR file name encoder tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


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

