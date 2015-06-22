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
        ipi_base = {}

        ipi_base['header'] = 'I'
        ipi_base['id_code'] = 229
        ipi_base['check_digit'] = 7

        data = {}

        data['ip_n'] = 'IP123'
        data['publisher_name'] = 'NAME'
        data['ipi_name_n'] = 250165006
        data['ipi_base_n'] = ipi_base
        data['tax_id'] = 923703412

        record = self._decoder.decode(data)

        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('NAME', record.publisher_name)
        self.assertEqual(250165006, record.ipi_name_n)
        self.assertEqual(923703412, record.tax_id)

        self.assertEqual('I', record.ipi_base_n.header)
        self.assertEqual(229, record.ipi_base_n.id_code)
        self.assertEqual(7, record.ipi_base_n.check_digit)
