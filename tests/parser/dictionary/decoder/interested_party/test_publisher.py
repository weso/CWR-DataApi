# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import PublisherDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPublisherDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = PublisherDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['ip_n'] = 'IP123'
        data['publisher_name'] = 'NAME'
        data['ipi_name_n'] = 250165006
        data['ipi_base_n'] = 'I-000000229-7'
        data['tax_id'] = 923703412

        record = self._decoder.decode(data)

        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('NAME', record.publisher_name)
        self.assertEqual(250165006, record.ipi_name_n)
        self.assertEqual(923703412, record.tax_id)

        self.assertEqual('I-000000229-7', record.ipi_base_n)
