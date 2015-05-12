# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import FileTagDictionaryDecoder


"""
Group Header to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileTagDictionaryDecoding(unittest.TestCase):
    def setUp(self):
        self._decoder = FileTagDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['year'] = 2015
        data['sequence_n'] = 123
        data['sender'] = 'SND'
        data['receiver'] = 'RCV'
        data['version'] = 2.1

        tag = self._decoder.decode(data)

        self.assertEqual(2015, tag.year)
        self.assertEqual(123, tag.sequence_n)
        self.assertEqual('SND', tag.sender)
        self.assertEqual('RCV', tag.receiver)
        self.assertEqual(2.1, tag.version)