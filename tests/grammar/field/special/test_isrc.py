# -*- coding: utf-8 -*-
import unittest

from pyparsing import ParseException

from cwr.grammar.field import special

"""
Tests for ISRC fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestISRCShort(unittest.TestCase):
    def setUp(self):
        self.isrc = special.isrc()

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'ES-A2B-12-12'

        result = self.isrc.parseString(code)[0]

        self.assertEqual('ES-A2B-12-12', result)

    def test_zeros(self):
        code = 'ES-A2B-00-00'

        result = self.isrc.parseString(code)

        self.assertEqual('ES-A2B-00-00', result.isrc)


class TestISRCLong(unittest.TestCase):
    def setUp(self):
        self.isrc = special.isrc()

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'ESABC9100055'

        result = self.isrc.parseString(code)[0]

        self.assertEqual('ESABC9100055', result)


class TestISRCExceptionShort(unittest.TestCase):
    def setUp(self):
        self.isrc = special.isrc()

    def test_invalid_country(self):
        """
        Tests an average code.
        """
        code = 'AA-A2B-12-12'

        self.assertRaises(ParseException, self.isrc.parseString, code)

    def test_only_text(self):
        """
        Tests an average code.
        """
        code = 'AABABBCCCDDD'

        self.assertRaises(ParseException, self.isrc.parseString, code)


class TestISRCExceptionLong(unittest.TestCase):
    def setUp(self):
        self.isrc = special.isrc()

    def test_invalid_country(self):
        """
        Tests an average code.
        """
        code = 'AAABC9100055'

        self.assertRaises(ParseException, self.isrc.parseString, code)
