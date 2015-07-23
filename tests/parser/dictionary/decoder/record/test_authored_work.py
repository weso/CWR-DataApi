# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import AuthoredWorkDictionaryDecoder
from cwr.other import ISWCCode

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestAuthoredWorkDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = AuthoredWorkDictionaryDecoder()

    def test_encoded(self):
        data = {}

        data['record_type'] = 'EWT'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['title'] = 'TITLE'
        data['submitter_work_n'] = 'WRK123'
        data['writer_1_first_name'] = 'FIRST NAME 1'
        data['writer_1_last_name'] = 'LAST NAME 1'
        data['writer_2_first_name'] = 'FIRST NAME 2'
        data['writer_2_last_name'] = 'LAST NAME 2'
        data['writer_1_ipi_name_n'] = 250165006
        data['writer_1_ipi_base_n'] = 'I-000000229-7'
        data['writer_2_ipi_name_n'] = 350165006
        data['writer_2_ipi_base_n'] = 'I-000000339-7'
        data['source'] = 'SOURCE'
        data['language_code'] = 'ES'
        data['iswc'] = ISWCCode(12345678, 9)

        record = self._decoder.decode(data)

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
        self.assertEqual(350165006, record.writer_2_ipi_name_n)
        self.assertEqual('SOURCE', record.source)
        self.assertEqual('ES', record.language_code)
        self.assertEqual(12345678, record.iswc.id_code)
        self.assertEqual(9, record.iswc.check_digit)

        self.assertEqual('I-000000229-7', record.writer_1_ipi_base_n)

        self.assertEqual('I-000000339-7', record.writer_2_ipi_base_n)
