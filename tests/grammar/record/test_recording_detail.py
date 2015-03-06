# -*- encoding: utf-8 -*-
import unittest

from cwr.grammar.record import work_detail


"""
CWR Work Detail grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkDetalGrammar(unittest.TestCase):
    def setUp(self):
        self.grammar = work_detail.recording

    def test_common(self):
        record = 'REC000001990000071019980101                                                            000300     A COMPILATION                                               A B C  _SYMBOLS_                                            33221                                       U   '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('REC', result.record_type)
        self.assertEqual(199, result.transaction_sequence_n)
        self.assertEqual(710, result.record_sequence_n)
        self.assertEqual(1998, result.first_release_date.year)
        self.assertEqual(1, result.first_release_date.month)
        self.assertEqual(1, result.first_release_date.day)
        self.assertEqual(0, result.first_release_duration.hour)
        self.assertEqual(3, result.first_release_duration.minute)
        self.assertEqual(0, result.first_release_duration.second)
        self.assertEqual('A COMPILATION', result.first_album_title)
        self.assertEqual('A B C  _SYMBOLS_', result.first_album_label)
        self.assertEqual('33221', result.first_release_catalog_id)
        self.assertEqual(None, result.ean)
        self.assertEqual('', result.isrc)
        self.assertEqual(None, result.recording_format)
        self.assertEqual('U', result.recording_technique)
        self.assertEqual(None, result.media_type)

    def test_valid_full(self):
        record = 'REC000012340000002320120113                                                            102030     ALBUM TITLE                                                 ALBUM LABEL                                                 CATALOG ID        1234567890123ESA2B1212345ADCD '

        result = self.grammar.parseString(record)[0]

        self.assertEqual('REC', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual(2012, result.first_release_date.year)
        self.assertEqual(1, result.first_release_date.month)
        self.assertEqual(13, result.first_release_date.day)
        self.assertEqual(10, result.first_release_duration.hour)
        self.assertEqual(20, result.first_release_duration.minute)
        self.assertEqual(30, result.first_release_duration.second)
        self.assertEqual('ALBUM TITLE', result.first_album_title)
        self.assertEqual('ALBUM LABEL', result.first_album_label)
        self.assertEqual('CATALOG ID', result.first_release_catalog_id)
        self.assertEqual(1234567890123, result.ean)
        self.assertEqual('ESA2B1212345', result.isrc)
        self.assertEqual('A', result.recording_format)
        self.assertEqual('D', result.recording_technique)
        self.assertEqual('CD', result.media_type)
