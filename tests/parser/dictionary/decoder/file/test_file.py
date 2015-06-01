# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import FileDictionaryDecoder

"""
Group Header to dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestFileDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = FileDictionaryDecoder()

    def test_encoded(self):
        tag = {}
        tag['year'] = 2015
        tag['sequence_n'] = 123
        tag['sender'] = 'SND'
        tag['receiver'] = 'RCV'
        tag['version'] = 2.1

        transmission = _get_transmission()

        file_data = {}
        file_data['tag'] = tag
        file_data['transmission'] = transmission

        data = self._decoder.decode(file_data)

        tag = data.tag

        self.assertEqual(2015, tag.year)
        self.assertEqual(123, tag.sequence_n)
        self.assertEqual('SND', tag.sender)
        self.assertEqual('RCV', tag.receiver)
        self.assertEqual(2.1, tag.version)

        record = data.transmission

        self.assertEqual('HDR', record.header.record_type)
        self.assertEqual('TRL', record.trailer.record_type)

        self.assertEqual(1, len(record.groups))

        group = record.groups[0]

        self.assertEqual('GRH', group.group_header.record_type)
        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('ACK', group.transactions[0][0].record_type)


def _get_transmission():
    header = {}
    header['record_type'] = 'HDR'
    header['sender_id'] = 'SND123'
    header['sender_name'] = 'THE SENDER'
    header['sender_type'] = 'SO'
    header['creation_date_time'] = datetime.datetime.strptime('20030216',
                                                              '%Y%m%d').date()
    header['transmission_date'] = datetime.datetime.strptime('20030217',
                                                             '%Y%m%d').date()
    header['edi_standard'] = '01.10'
    header['character_set'] = 'ASCII'

    trailer = {}
    trailer['record_type'] = 'TRL'
    trailer['group_count'] = 11
    trailer['transaction_count'] = 22
    trailer['record_count'] = 33

    trailer_group = {}
    trailer_group['record_count'] = 20
    trailer_group['record_type'] = 'GRT'
    trailer_group['group_id'] = 3
    trailer_group['transaction_count'] = 15

    header_group = {}
    header_group['record_type'] = 'GRH'
    header_group['version_number'] = '02.10'
    header_group['group_id'] = 3
    header_group['batch_request_id'] = 15
    header_group['transaction_type'] = 'AGR'

    transactions = [[{'original_group_id': 4,
                      'creation_date_time': datetime.date(2003, 2, 15),
                      'original_transaction_type': 'AGR',
                      'record_sequence_n': 15, 'record_type': 'ACK',
                      'creation_title': 'TITLE',
                      'original_transaction_sequence_n': 5,
                      'transaction_status': 'AS',
                      'recipient_creation_n': 'B124',
                      'submitter_creation_n': 'A123',
                      'transaction_sequence_n': 3,
                      'processing_date': datetime.date(2003, 2, 16)},
                     {'original_record_sequence_n': 124, 'validation_n': 'AB3',
                      'message_record_type': 'AGR',
                      'message_text': 'THE MESSAGE', 'record_sequence_n': 15,
                      'record_type': 'MSG',
                      'message_level': 'F', 'message_type': 'G',
                      'transaction_sequence_n': 3},
                     {'original_record_sequence_n': 124, 'validation_n': 'AB3',
                      'message_record_type': 'AGR',
                      'message_text': 'THE MESSAGE', 'record_sequence_n': 15,
                      'record_type': 'MSG',
                      'message_level': 'F', 'message_type': 'G',
                      'transaction_sequence_n': 3},
                     {'sales_manufacture_clause': 'M',
                      'date_of_signature': datetime.date(2003, 2, 17),
                      'prior_royalty_start_date': datetime.date(2003, 2, 19),
                      'advance_given': True,
                      'retention_end_date': datetime.date(2003, 2, 18),
                      'international_standard_code': 'DFG135',
                      'prior_royalty_status': 'D',
                      'agreement_end_date': datetime.date(2003, 2, 16),
                      'record_type': 'AGR', 'shares_change': True,
                      'post_term_collection_status': 'D',
                      'agreement_type': 'OS', 'submitter_agreement_n': 'AB12',
                      'society_assigned_agreement_n': 'DF35',
                      'record_sequence_n': 15,
                      'agreement_start_date': datetime.date(2003, 2, 15),
                      'transaction_sequence_n': 3,
                      'post_term_collection_end_date': datetime.date(2003, 2,
                                                                     20),
                      'number_of_works': 12}]]

    groups = [{'group_header': header_group, 'transactions': transactions,
               'group_trailer': trailer_group}]

    transmission = {'header': header, 'groups': groups, 'trailer': trailer}

    return transmission
