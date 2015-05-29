# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.encoder.dictionary import GroupDictionaryEncoder
from cwr.group import GroupHeader, GroupTrailer, Group
from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.agreement import AgreementRecord

"""
Group Header to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestGroupDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = GroupDictionaryEncoder()

    def test_encoded(self):
        header = GroupHeader(record_type='GRH',
                             group_id=3,
                             transaction_type='AGR',
                             version_number='02.10',
                             batch_request_id=15)
        trailer = GroupTrailer(record_type='GRT',
                               group_id=3,
                               transaction_count=15,
                               record_count=20)
        transactions = [self._get_transaction()]

        data = Group(header, trailer, transactions)

        encoded = self._encoder.encode(data)

        self.assertEqual('GRH', encoded['group_header']['record_type'])
        self.assertEqual('GRT', encoded['group_trailer']['record_type'])
        self.assertEqual(1, len(encoded['transactions']))
        self.assertEqual(4, len(encoded['transactions'][0]))
        self.assertEqual('ACK', encoded['transactions'][0][0]['record_type'])

    def _get_transaction(self):
        acknowledgement = self._get_ack()

        message1 = self._get_message()
        message2 = self._get_message()

        agreement = self._get_agreement()

        return [acknowledgement, message1, message2, agreement]

    def _get_ack(self):
        return AcknowledgementRecord(record_type='ACK',
                                     transaction_sequence_n=3,
                                     record_sequence_n=15,
                                     original_group_id=4,
                                     original_transaction_sequence_n=5,
                                     original_transaction_type='AGR',
                                     transaction_status='AS',
                                     creation_date_time=datetime.datetime.strptime(
                                         '20030215', '%Y%m%d').date(),
                                     processing_date=datetime.datetime.strptime(
                                         '20030216', '%Y%m%d').date(),
                                     creation_title='TITLE',
                                     submitter_creation_n='A123',
                                     recipient_creation_n='B124')

    def _get_message(self):
        return MessageRecord(record_type='MSG',
                             transaction_sequence_n=3,
                             record_sequence_n=15,
                             message_level='F',
                             validation_n='AB3',
                             message_type='G',
                             message_text='THE MESSAGE',
                             original_record_sequence_n=124,
                             message_record_type='AGR')

    def _get_agreement(self):
        return AgreementRecord(record_type='AGR',
                               transaction_sequence_n=3,
                               record_sequence_n=15,
                               submitter_agreement_n='AB12',
                               agreement_type='OS',
                               agreement_start_date=datetime.datetime.strptime(
                                   '20030215', '%Y%m%d').date(),
                               number_of_works=12,
                               prior_royalty_status='D',
                               post_term_collection_status='D',
                               international_standard_code='DFG135',
                               society_assigned_agreement_n='DF35',
                               sales_manufacture_clause='M',
                               agreement_end_date=datetime.datetime.strptime(
                                   '20030216', '%Y%m%d').date(),
                               date_of_signature=datetime.datetime.strptime(
                                   '20030217', '%Y%m%d').date(),
                               retention_end_date=datetime.datetime.strptime(
                                   '20030218', '%Y%m%d').date(),
                               prior_royalty_start_date=datetime.datetime.strptime(
                                   '20030219', '%Y%m%d').date(),
                               post_term_collection_end_date=datetime.datetime.strptime(
                                   '20030220', '%Y%m%d').date(),
                               shares_change=True,
                               advance_given=True)
