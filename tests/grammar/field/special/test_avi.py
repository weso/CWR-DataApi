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


class TestAVIValid(unittest.TestCase):
    def setUp(self):
        self.ean = special.avi()

    def test_common(self):
        """
        Tests an average code.
        """
        code = '012012345678901234'

        result = self.ean.parseString(code)[0]

        self.assertEqual(12, result.society_code)
        self.assertEqual('012345678901234', result.av_number)


class TestAVIResultName(unittest.TestCase):
    """
    Tests that the IPI Base Number accepts and parses valid values.
    """

    def setUp(self):
        self.ean = special.avi()

    def test_common(self):
        code = '012012345678901234'

        result = self.ean.parseString(code)

        self.assertEqual(12, result.avi.society_code)
        self.assertEqual('012345678901234', result.avi.av_number)