# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AuthoredWorkDictionaryDecoder
from cwr.other import IPIBaseNumber, ISWCCode

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestAuthoredWorkDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AuthoredWorkDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['record_type'] = 'EWT'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['title'] = 'TITLE'
        dict['submitter_work_n'] = 'WRK123'
        dict['writer_1_first_name'] = 'FIRST NAME 1'
        dict['writer_1_last_name'] = 'LAST NAME 1'
        dict['writer_2_first_name'] = 'FIRST NAME 2'
        dict['writer_2_last_name'] = 'LAST NAME 2'
        dict['writer_1_ipi_name_n'] = 250165006
        dict['writer_1_ipi_base_n'] = IPIBaseNumber('I', 229, 7)
        dict['writer_2_ipi_name_n'] = 350165006
        dict['writer_2_ipi_base_n'] = IPIBaseNumber('I', 230, 8)
        dict['source'] = 'SOURCE'
        dict['language_code'] = 'ES'
        dict['iswc'] = ISWCCode(12345678, 9)

        record = self._decoder.decode(dict)

        self.assertEqual('EWT', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('TITLE', record.title)
        self.assertEqual('WRK123', record.submitter_work_n)
        self.assertEqual('FIRST NAME 1', record.writer_1_first_name)
        self.assertEqual('LAST NAME 1', record.writer_1_last_name)
        self.assertEqual('FIRST NAME 2', record.writer_2_first_name)
        self.assertEqual('LAST NAME 2', record.writer_2_last_name)
        self.assertEqual(250165006, record.writer_1_ipi_name_n)
        self.assertEqual('I', record.writer_1_ipi_base_n.header)
        self.assertEqual(229, record.writer_1_ipi_base_n.id_code)
        self.assertEqual(7, record.writer_1_ipi_base_n.check_digit)
        self.assertEqual(350165006, record.writer_2_ipi_name_n)
        self.assertEqual('I', record.writer_2_ipi_base_n.header)
        self.assertEqual(230, record.writer_2_ipi_base_n.id_code)
        self.assertEqual(8, record.writer_2_ipi_base_n.check_digit)
        self.assertEqual('SOURCE', record.source)
        self.assertEqual('ES', record.language_code)
        self.assertEqual(12345678, record.iswc.id_code)
        self.assertEqual(9, record.iswc.check_digit)
