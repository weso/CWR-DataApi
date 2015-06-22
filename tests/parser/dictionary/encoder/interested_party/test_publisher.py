# -*- coding: utf-8 -*-

import unittest

from cwr.parser.encoder.dictionary import PublisherDictionaryEncoder
from cwr.interested_party import Publisher
from cwr.other import IPIBaseNumber

"""
Publisher to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestPublisherDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = PublisherDictionaryEncoder()

    def test_encoded(self):
        ipi_base = IPIBaseNumber('I', 229, 7)

        data = Publisher(ip_n='ABC15',
                         publisher_name='NAME',
                         ipi_name_n=14107338,
                         ipi_base_n=ipi_base,
                         tax_id=923703412)

        encoded = self._encoder.encode(data)

        self.assertEqual('ABC15', encoded['ip_n'])
        self.assertEqual('NAME', encoded['publisher_name'])
        self.assertEqual(14107338, encoded['ipi_name_n'])
        self.assertEqual(923703412, encoded['tax_id'])

        self.assertEqual('I', encoded['ipi_base_n']['header'])
        self.assertEqual(229, encoded['ipi_base_n']['id_code'])
        self.assertEqual(7, encoded['ipi_base_n']['check_digit'])
