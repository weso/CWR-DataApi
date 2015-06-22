# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import WriterDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWorkDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WriterDictionaryDecoder()

    def test_encoded(self):
        ipi_base = {}

        ipi_base['header'] = 'I'
        ipi_base['id_code'] = 229
        ipi_base['check_digit'] = 7

        data = {}

        data['ip_n'] = 'ABC15'
        data['personal_number'] = 'ABC1234'
        data['ipi_name_n'] = 14107338
        data['ipi_base_n'] = ipi_base
        data['writer_first_name'] = 'NAME'
        data['writer_last_name'] = 'LAST NAME'
        data['tax_id'] = 923703412

        record = self._decoder.decode(data)

        self.assertEqual('ABC15', record.ip_n)
        self.assertEqual('ABC1234', record.personal_number)
        self.assertEqual(14107338, record.ipi_name_n)
        self.assertEqual('NAME', record.writer_first_name)
        self.assertEqual('LAST NAME', record.writer_last_name)
        self.assertEqual(923703412, record.tax_id)

        self.assertEqual('I', record.ipi_base_n.header)
        self.assertEqual(229, record.ipi_base_n.id_code)
        self.assertEqual(7, record.ipi_base_n.check_digit)
