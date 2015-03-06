# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.field import table

"""
CWR file Record parsing tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestSocietyCodeValid(unittest.TestCase):
    def setUp(self):
        self.grammar = table.society()

    def test_full(self):
        value = '001'

        result = self.grammar.parseString(value)[0]

        self.assertEqual(1, result)

    def test_short_left(self):
        value = '1  '

        result = self.grammar.parseString(value)[0]

        self.assertEqual(1, result)

    def test_short_right(self):
        value = '  1'

        # TODO: Make this work
        # result = self.grammar.parseString(value)[0]

        # self.assertEqual(1, result)

    def test_empty(self):
        value = '   '

        result = self.grammar.parseString(value)[0]

        self.assertEqual(None, result)