# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.field import table

"""
CWR file Special Agreement parsing tests.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestSpecialAgreementValid(unittest.TestCase):
    def setUp(self):
        self.grammar = table.special_agreement()

    def test_valid(self):
        value = 'B'

        result = self.grammar.parseString(value)[0]

        self.assertEqual('B', result)

    def test_empty(self):
        value = ' '

        result = self.grammar.parseString(value)[0]

        self.assertEqual(None, result)
