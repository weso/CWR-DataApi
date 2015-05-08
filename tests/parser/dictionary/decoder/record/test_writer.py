# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import WriterRecordDictionaryDecoder


"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWriterRecordDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WriterRecordDictionaryDecoder()

    def test_encoded(self):
        dict = {}

        dict['ip_n'] = 'ABC15'
        dict['personal_number'] = 'ABC1234'
        dict['ipi_name_n'] = 14107338
        dict['ipi_base_n'] = 'I-000000229-7'
        dict['writer_first_name'] = 'NAME'
        dict['writer_last_name'] = 'LAST NAME'
        dict['tax_id'] = 923703412

        dict['record_type'] = 'SWR'
        dict['transaction_sequence_n'] = 3
        dict['record_sequence_n'] = 15
        dict['writer_designation'] = 'AD'
        dict['work_for_hire'] = True
        dict['writer_unknown'] = 'T'
        dict['reversionary'] = 'T'
        dict['first_recording_refusal'] = 'T'
        dict['usa_license'] = 'B'
        dict['pr_society'] = 13
        dict['pr_ownership_share'] = 50.5
        dict['mr_society'] = 14
        dict['mr_ownership_share'] = 60.5
        dict['sr_society'] = 15
        dict['sr_ownership_share'] = 70.5

        record = self._decoder.decode(dict)

        self.assertEqual('ABC15', record.writer.ip_n)
        self.assertEqual('ABC1234', record.writer.personal_number)
        self.assertEqual(14107338, record.writer.ipi_name_n)
        self.assertEqual('I-000000229-7', record.writer.ipi_base_n)
        self.assertEqual('NAME', record.writer.writer_first_name)
        self.assertEqual('LAST NAME', record.writer.writer_last_name)
        self.assertEqual(923703412, record.writer.tax_id)

        self.assertEqual('SWR', record.record_type)
        self.assertEqual(3, record.transaction_sequence_n)
        self.assertEqual(15, record.record_sequence_n)
        self.assertEqual('AD', record.writer_designation)
        self.assertEqual(True, record.work_for_hire)
        self.assertEqual('T', record.writer_unknown)
        self.assertEqual('T', record.reversionary)
        self.assertEqual('T', record.first_recording_refusal)
        self.assertEqual('B', record.usa_license)
        self.assertEqual(13, record.pr_society)
        self.assertEqual(50.5, record.pr_ownership_share)
        self.assertEqual(14, record.mr_society)
        self.assertEqual(60.5, record.mr_ownership_share)
        self.assertEqual(15, record.sr_society)
        self.assertEqual(70.5, record.sr_ownership_share)