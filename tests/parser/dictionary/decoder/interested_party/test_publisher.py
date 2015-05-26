# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import PublisherDictionaryDecoder
from cwr.other import IPIBaseNumber

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPublisherDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = PublisherDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['ip_n'] = 'IP123'
        dict['publisher_name'] = 'NAME'
        dict['ipi_name_n'] = 250165006
        dict['ipi_base_n'] = IPIBaseNumber('I', 229, 7)
        dict['tax_id'] = 923703412

        record = self._decoder.decode(dict)

        self.assertEqual('IP123', record.ip_n)
        self.assertEqual('NAME', record.publisher_name)
        self.assertEqual(250165006, record.ipi_name_n)
        self.assertEqual('I', record.ipi_base_n.header)
        self.assertEqual(229, record.ipi_base_n.id_code)
        self.assertEqual(7, record.ipi_base_n.check_digit)
        self.assertEqual(923703412, record.tax_id)
