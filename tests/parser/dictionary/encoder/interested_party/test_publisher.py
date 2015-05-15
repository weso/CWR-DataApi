# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import PublisherEncoder
from cwr.interested_party import Publisher


"""
Publisher to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestPublisherDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = PublisherEncoder()

    def test_encoded(self):
        data = Publisher(ip_n='ABC15',
                         publisher_name='NAME',
                         ipi_name_n=14107338,
                         ipi_base_n='I-000000229-7',
                         tax_id=923703412)

        encoded = self._encoder.encode(data)

        self.assertEqual('ABC15', encoded['ip_n'])
        self.assertEqual('NAME', encoded['publisher_name'])
        self.assertEqual(14107338, encoded['ipi_name_n'])
        self.assertEqual('I-000000229-7', encoded['ipi_base_n'])
        self.assertEqual(923703412, encoded['tax_id'])