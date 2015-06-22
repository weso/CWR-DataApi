# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.dictionary import WriterRecordDictionaryDecoder

"""
Dictionary to Message decoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestWriterRecordDictionaryDecoder(unittest.TestCase):
    def setUp(self):
        self._decoder = WriterRecordDictionaryDecoder()

    def test_encoded(self):
        ipi_base = {}

        ipi_base['header'] = 'I'
        ipi_base['id_code'] = 229
        ipi_base['check_digit'] = 7

        writer = {}

        writer['ip_n'] = 'ABC15'
        writer['personal_number'] = 'ABC1234'
        writer['ipi_name_n'] = 14107338
        writer['ipi_base_n'] = ipi_base
        writer['writer_first_name'] = 'NAME'
        writer['writer_last_name'] = 'LAST NAME'
        writer['tax_id'] = 923703412

        data = {}

        data['writer'] = writer

        data['record_type'] = 'SWR'
        data['transaction_sequence_n'] = 3
        data['record_sequence_n'] = 15
        data['writer_designation'] = 'AD'
        data['work_for_hire'] = True
        data['writer_unknown'] = 'T'
        data['reversionary'] = 'T'
        data['first_recording_refusal'] = 'T'
        data['usa_license'] = 'B'
        data['pr_society'] = 13
        data['pr_ownership_share'] = 50.5
        data['mr_society'] = 14
        data['mr_ownership_share'] = 60.5
        data['sr_society'] = 15
        data['sr_ownership_share'] = 70.5

        record = self._decoder.decode(data)

        self.assertEqual('ABC15', record.writer.ip_n)
        self.assertEqual('ABC1234', record.writer.personal_number)
        self.assertEqual(14107338, record.writer.ipi_name_n)
        self.assertEqual('NAME', record.writer.writer_first_name)
        self.assertEqual('LAST NAME', record.writer.writer_last_name)
        self.assertEqual(923703412, record.writer.tax_id)

        self.assertEqual('I', record.writer.ipi_base_n.header)
        self.assertEqual(229, record.writer.ipi_base_n.id_code)
        self.assertEqual(7, record.writer.ipi_base_n.check_digit)

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
