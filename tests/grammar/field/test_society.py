# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.field.table import society

"""
CWR file Record parsing tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestSocietyCodeValid(unittest.TestCase):
    def setUp(self):
        self.grammar = society()

    def test_full(self):
        value = '001'

        result = self.grammar.parseString(value)[0]

        self.assertEqual(1, result)

    def test_short(self):
        value = '1  '

        result = self.grammar.parseString(value)[0]

        self.assertEqual(1, result)