# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.file import FileTag


"""
Group Header to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        data = FileTag(year=2015,
                       sequence_n=123,
                       sender='SND',
                       receiver='RCV',
                       version=2.1)

        encoded = self._encoder.encode(data)

        self.assertEqual(2015, encoded['year'])
        self.assertEqual(123, encoded['sequence_n'])
        self.assertEqual('SND', encoded['sender'])
        self.assertEqual('RCV', encoded['receiver'])
        self.assertEqual(2.1, encoded['version'])