# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.field import special

"""
Tests for V-ISAN field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestVISANValid(unittest.TestCase):
    def setUp(self):
        self.ean = special.visan()

    def test_common(self):
        """
        Tests an average code.
        """
        code = '0123456701234567891201231'

        result = self.ean.parseString(code)[0]

        self.assertEqual('0123456701234567891201231', result)


class TestVISANResultName(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ean = special.visan()

    def test_common(self):
        code = '0123456701234567891201231'

        result = self.ean.parseString(code)

        self.assertEqual('0123456701234567891201231', result.visan)
