# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import ComponentDictionaryDecoder
from cwr.other import ISWCCode

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestComponentDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = ComponentDictionaryDecoder()

    def test_encoded(self):
        ipi_base_1 = {}

        ipi_base_1['header'] = 'I'
        ipi_base_1['id_code'] = 229
        ipi_base_1['check_digit'] = 7

        ipi_base_2 = {}

        ipi_base_2['header'] = 'I'
        ipi_base_2['id_code'] = 339
        ipi_base_2['check_digit'] = 7

        data = {}

        data['record_type'] = 'COM'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['title'] = 'TITLE'
        data['submitter_work_n'] = 'ABCD123'
        data['writer_1_last_name'] = 'LAST NAME 1'
        data['writer_1_first_name'] = 'FIRST NAME 1'
        data['writer_2_last_name'] = 'LAST NAME 2'
        data['writer_2_first_name'] = 'FIRST NAME 2'
        data['writer_1_ipi_name_n'] = 14107338
        data['writer_1_ipi_base_n'] = ipi_base_1
        data['writer_2_ipi_name_n'] = 14107400
        data['writer_2_ipi_base_n'] = ipi_base_2
        data['iswc'] = ISWCCode(12345678, 9)
        data['duration'] = datetime.datetime.strptime('011200', '%H%M%S').time()

        record = self._decoder.decode(data)

        self.assertEqual('COM', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('TITLE', record.title)
        self.assertEqual('LAST NAME 1', record.writer_1_last_name)
        self.assertEqual('ABCD123', record.submitter_work_n)
        self.assertEqual('FIRST NAME 1', record.writer_1_first_name)
        self.assertEqual('FIRST NAME 2', record.writer_2_first_name)
        self.assertEqual('LAST NAME 2', record.writer_2_last_name)
        self.assertEqual('LAST NAME 2', record.writer_2_last_name)
        self.assertEqual(14107338, record.writer_1_ipi_name_n)
        self.assertEqual(14107400, record.writer_2_ipi_name_n)
        self.assertEqual(12345678, record.iswc.id_code)
        self.assertEqual(9, record.iswc.check_digit)
        self.assertEqual(datetime.datetime.strptime('011200', '%H%M%S').time(),
                         record.duration)

        self.assertEqual('I', record.writer_1_ipi_base_n.header)
        self.assertEqual(229, record.writer_1_ipi_base_n.id_code)
        self.assertEqual(7, record.writer_1_ipi_base_n.check_digit)

        self.assertEqual('I', record.writer_2_ipi_base_n.header)
        self.assertEqual(339, record.writer_2_ipi_base_n.id_code)
        self.assertEqual(7, record.writer_2_ipi_base_n.check_digit)
