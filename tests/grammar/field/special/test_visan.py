# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.field import special


"""
Tests for V-ISAN field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
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

        self.assertEqual(1234567, result.version)
        self.assertEqual(12345678912, result.isan)
        self.assertEqual(123, result.episode)
        self.assertEqual(1, result.check_digit)


class TestVISANResultName(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ean = special.visan()

    def test_common(self):
        code = '0123456701234567891201231'

        result = self.ean.parseString(code)

        self.assertEqual(1234567, result.visan.version)
        self.assertEqual(12345678912, result.visan.isan)
        self.assertEqual(123, result.visan.episode)
        self.assertEqual(1, result.visan.check_digit)