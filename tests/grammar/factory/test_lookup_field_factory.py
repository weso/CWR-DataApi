# -*- coding: utf-8 -*-
import unittest

from cwr.grammar.factory.field import LookupFieldFactory


"""
Tests for EAN 13 fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestLookupFieldFactoryValid(unittest.TestCase):
    def setUp(self):
        self.factory = LookupFieldFactory()

    def test_creation(self):
        id = 'original_transaction_type'

        result = self.factory.get_field(id)

        self.assertNotEqual(None, result)

    def test_returns_same(self):
        id = 'original_transaction_type'

        result1 = self.factory.get_field(id)
        result2 = self.factory.get_field(id)

        self.assertEqual(result1, result2)

    def test_returns_same_two_instances(self):
        factory2 = LookupFieldFactory()

        id = 'original_transaction_type'

        result1 = self.factory.get_field(id)
        result2 = factory2.get_field(id)

        self.assertEqual(result1, result2)