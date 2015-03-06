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
        code = 'ESA2B1212345'

        result = self.isrc.parseString(code)[0]

        self.assertEqual('ESA2B1212345', result)