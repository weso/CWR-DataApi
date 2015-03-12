# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.field import special


"""
Tests for EAN 13 fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestEAN13Valid(unittest.TestCase):
    def setUp(self):
        self.ean = special.ean_13()

    def test_common(self):
        """
        Tests an average code.
        """
        code = '1234567890123'

        result = self.ean.parseString(code)[0]

        self.assertEqual(1234567890123, result)


class TestEAN13ResultName(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ean = special.ean_13()

    def test_common(self):
        code = '1234567890123'

        result = self.ean.parseString(code)

        self.assertEqual(1234567890123, result.ean_13)