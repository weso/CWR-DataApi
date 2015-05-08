# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import WriterDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWorkDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WriterDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['ip_n'] = 'ABC15'
        dict['personal_number'] = 'ABC1234'
        dict['ipi_name_n'] = 14107338
        dict['ipi_base_n'] = 'I-000000229-7'
        dict['writer_first_name'] = 'NAME'
        dict['writer_last_name'] = 'LAST NAME'
        dict['tax_id'] = 923703412

        record = self._decoder.decode(dict)

        self.assertEqual('ABC15', record.ip_n)
        self.assertEqual('ABC1234', record.personal_number)
        self.assertEqual(14107338, record.ipi_name_n)
        self.assertEqual('I-000000229-7', record.ipi_base_n)
        self.assertEqual('NAME', record.writer_first_name)
        self.assertEqual('LAST NAME', record.writer_last_name)
        self.assertEqual(923703412, record.tax_id)