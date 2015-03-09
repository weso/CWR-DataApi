# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.field import special


"""
Tests for ISRC fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestISRCValid(unittest.TestCase):
    def setUp(self):
        self.isrc = special.isrc()

    def test_common(self):
        """
        Tests an average code.
        """
        code = 'ES-A2B-12-12'

        result = self.isrc.parseString(code)[0]

        self.assertEqual('ES-A2B-12-12', result)

    def test_white(self):
        """
        Tests an average code.
        """
        code = '            '

        result = self.isrc.parseString(code)[0]

        self.assertEqual('', result)