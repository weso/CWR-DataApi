# -*- coding: utf-8 -*-

import unittest

from cwr.parser.dictionary import CWRDictionaryEncoder
from cwr.interested_party import Writer, WriterRecord


"""
Writer to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestWriterRecordDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = CWRDictionaryEncoder()

    def test_encoded(self):
        writer = Writer(ip_n='ABC15',
                        personal_number='ABC1234',
                        ipi_name_n=14107338,
                        ipi_base_n='I-000000229-7',
                        writer_first_name='NAME',
                        writer_last_name='LAST NAME',
                        tax_id=923703412)

        data = WriterRecord(record_type='SWR',
                            transaction_sequence_n=3,
                            record_sequence_n=15,
                            writer=writer,
                            writer_designation='AD',
                            work_for_hire=True,
                            writer_unknown='T',
                            reversionary='T',
                            first_recording_refusal='T',
                            usa_license='B',
                            pr_society=13,
                            pr_ownership_share=50.5,
                            mr_society=14,
                            mr_ownership_share=60.5,
                            sr_society=15,
                            sr_ownership_share=70.5)

        encoded = self._encoder.encode(data)

        writer = encoded['writer']

        self.assertEqual('ABC15', writer['ip_n'])
        self.assertEqual('ABC1234', writer['personal_number'])
        self.assertEqual(14107338, writer['ipi_name_n'])
        self.assertEqual('I-000000229-7', writer['ipi_base_n'])
        self.assertEqual('NAME', writer['writer_first_name'])
        self.assertEqual('LAST NAME', writer['writer_last_name'])
        self.assertEqual(923703412, writer['tax_id'])

        self.assertEqual('SWR', encoded['record_type'])
        self.assertEqual(3, encoded['transaction_sequence_n'])
        self.assertEqual(15, encoded['record_sequence_n'])
        self.assertEqual('AD', encoded['writer_designation'])
        self.assertEqual(True, encoded['work_for_hire'])
        self.assertEqual('T', encoded['writer_unknown'])
        self.assertEqual('T', encoded['reversionary'])
        self.assertEqual('T', encoded['first_recording_refusal'])
        self.assertEqual('B', encoded['usa_license'])
        self.assertEqual(13, encoded['pr_society'])
        self.assertEqual(50.5, encoded['pr_ownership_share'])
        self.assertEqual(14, encoded['mr_society'])
        self.assertEqual(60.5, encoded['mr_ownership_share'])
        self.assertEqual(15, encoded['sr_society'])
        self.assertEqual(70.5, encoded['sr_ownership_share'])