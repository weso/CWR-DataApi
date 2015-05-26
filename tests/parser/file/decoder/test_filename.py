# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.file import default_filename_decoder

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
        self._parser = default_filename_decoder()

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
        self._parser = default_filename_decoder()

    def test_invalid(self):
        result = self._parser.decode('CW130001059_201_.txt')

        self.assertEqual(0, result.year)
        self.assertEqual(0, result.sequence_n)
        self.assertEqual('', result.sender)
        self.assertEqual('', result.receiver)
        self.assertEqual('', result.version)
