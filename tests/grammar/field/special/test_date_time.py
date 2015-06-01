# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.field import special

"""
Tests for the Date and Time field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestDateTimeValid(unittest.TestCase):
    def setUp(self):
        self.ean = special.date_time()

    def test_common(self):
        """
        Tests an average code.
        """
        date = '20120115123000'

        result = self.ean.parseString(date)[0]

        self.assertEqual(2012, result.year)
        self.assertEqual(1, result.month)
        self.assertEqual(15, result.day)
        self.assertEqual(12, result.hour)
        self.assertEqual(30, result.minute)
        self.assertEqual(0, result.second)
