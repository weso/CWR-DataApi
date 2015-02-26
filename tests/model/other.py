# -*- encoding: utf-8 -*-

import unittest

from cwr.other import ISWCCode


"""
Tests for miscellany model classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestISWCCode(unittest.TestCase):
    """
    Tests the ISWCCode class.
    """

    def test_printable_text(self):
        iswc = ISWCCode(123, 1)

        self.assertEqual('ISWC T-000000123-1', str(iswc))