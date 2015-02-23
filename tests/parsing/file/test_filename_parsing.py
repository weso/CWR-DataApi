# -*- encoding: utf-8 -*-
import unittest

from cwr.parsing.file import CWRFileNameDecoder, CWRFileNameEncoder
from cwr.file import FileTag
from pyparsing import ParseException

"""
CWR file name parsing tests.

The following cases are tested:
- CWRFileNameDecoder decodes correctly formatted CWR file names (using both the old and new format)
- CWRFileNameDecoder decodes correctly formatted zip file file names (using both the old and new format)
- CWRFileNameEncoder encodes valid FileTags (using both the old and new format)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileNameCWRDecodeValid(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted CWR file names (using the new format).
    """

    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.decode('CW12012311_22.V21')

        self.assertEqual(2012, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.decode('CW130123ABC_23.V22')

        self.assertEqual(2013, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.decode('CW99000022_DEC.V00')

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.decode('CW000012AB2_234.V02')

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestFileNameCWRDecodeValidOld(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted CWR file names (using the old format).
    """

    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.decode_old('CW122311_22.V21')

        self.assertEqual(2012, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.decode_old('CW1301ABC_23.V22')

        self.assertEqual(2013, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.2, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.decode_old('CW990022_DEC.V00')

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(0, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.decode_old('CW0012AB2_234.V02')

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(0.2, data.version)


class TestFileNameZIPDecodeValid(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted zip file file names (using the new format).
    """

    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.decode('CW12012311_22.zip')

        self.assertEqual(2012, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.decode('CW130123ABC_23.zip')

        self.assertEqual(2013, data.year)
        self.assertEqual(123, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.decode('CW99000022_DEC.zip')

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.decode('CW000012AB2_234.zip')

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2.1, data.version)


class TestFileNameZIPDecodeValidOld(unittest.TestCase):
    """
    Tests that CWRFileNameDecoder decodes correctly formatted zip file names (using the old format).
    """

    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.decode_old('CW122311_22.zip')

        self.assertEqual(2012, data.year)
        self.assertEqual(23, data.sequence_n)
        self.assertEqual('11', data.sender)
        self.assertEqual('22', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.decode_old('CW1301ABC_23.zip')

        self.assertEqual(2013, data.year)
        self.assertEqual(1, data.sequence_n)
        self.assertEqual('ABC', data.sender)
        self.assertEqual('23', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.decode_old('CW990022_DEC.zip')

        self.assertEqual(2099, data.year)
        self.assertEqual(0, data.sequence_n)
        self.assertEqual('22', data.sender)
        self.assertEqual('DEC', data.receiver)
        self.assertEqual(2.1, data.version)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.decode_old('CW0012AB2_234.zip')

        self.assertEqual(2000, data.year)
        self.assertEqual(12, data.sequence_n)
        self.assertEqual('AB2', data.sender)
        self.assertEqual('234', data.receiver)
        self.assertEqual(2.1, data.version)


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
        self._parser = CWRFileNameEncoder()

    def test_s2_r2(self):
        # Sender with 2 digits and receiver with 2 digits
        data = self._parser.encode_old(FileTag(2012, 23, '11', '22', 2.1))

        self.assertEqual("CW122311_22.V21", data)

    def test_s3_r2(self):
        # Sender with 3 digits and receiver with 2 digits
        data = self._parser.encode_old(FileTag(2013, 1, 'ABC', '23', 2.2))

        self.assertEqual("CW1301ABC_23.V22", data)

    def test_s2_r3(self):
        # Sender with 2 digits and receiver with 3 digits
        data = self._parser.encode_old(FileTag(2099, 0, '22', 'DEC', 0))

        self.assertEqual("CW990022_DEC.V00", data)

    def test_s3_r3(self):
        # Sender with 3 digits and receiver with 3 digits
        data = self._parser.encode_old(FileTag(2000, 12, 'AB2', '234', 0.2))

        self.assertEqual("CW0012AB2_234.V02", data)

class TestFileNameCWRDecodeException(unittest.TestCase):

    def setUp(self):
        self._parser = CWRFileNameDecoder()

    def test_empty(self):
        self.assertRaises(ParseException, self._parser.decode, '')

    def test_empty_old(self):
        self.assertRaises(ParseException, self._parser.decode_old, '')

    def test_sequence_too_long(self):
        self.assertRaises(ParseException, self._parser.decode, 'CW0000012AB2_234.V21')

    def test_sequence_too_short(self):
        self.assertRaises(ParseException, self._parser.decode, 'CW000012AB2_234.V21')

    def test_sender_spaces(self):
        self.assertRaises(ParseException, self._parser.decode, 'CW000012A 2_234.V21')

    def test_receiver_spaces(self):
        self.assertRaises(ParseException, self._parser.decode, 'CW000012AB2_2 4.V21')
