# -*- coding: utf-8 -*-

import unittest
import datetime

from cwr.parser.decoder.dictionary import GroupDictionaryDecoder

"""
Group from dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TestGroupDictionaryEncoding(unittest.TestCase):
    def setUp(self):
        self._decoder = GroupDictionaryDecoder()

    def test_encoded(self):
        trailer = {}
        trailer['record_count'] = 20
        trailer['record_type'] = 'GRT'
        trailer['group_id'] = 3
        trailer['transaction_count'] = 15

        header = {}
        header['record_type'] = 'GRH'
        header['version_number'] = '02.10'
        header['group_id'] = 3
        header['batch_request_id'] = 15
        header['transaction_type'] = 'AGR'

        transactions = [[{'original_group_id': 4, 'creation_date_time': datetime.date(2003, 2, 15),
                          'original_transaction_type': 'AGR', 'record_sequence_n': 15, 'record_type': 'ACK',
                          'creation_title': 'TITLE', 'original_transaction_sequence_n': 5, 'transaction_status': 'AS',
                          'recipient_creation_n': 'B124', 'submitter_creation_n': 'A123', 'transaction_sequence_n': 3,
                          'processing_date': datetime.date(2003, 2, 16)},
                         {'original_record_sequence_n': 124, 'validation_n': 'AB3', 'message_record_type': 'AGR',
                          'message_text': 'THE MESSAGE', 'record_sequence_n': 15, 'record_type': 'MSG',
                          'message_level': 'F', 'message_type': 'G', 'transaction_sequence_n': 3},
                         {'original_record_sequence_n': 124, 'validation_n': 'AB3', 'message_record_type': 'AGR',
                          'message_text': 'THE MESSAGE', 'record_sequence_n': 15, 'record_type': 'MSG',
                          'message_level': 'F', 'message_type': 'G', 'transaction_sequence_n': 3},
                         {'sales_manufacture_clause': 'M', 'date_of_signature': datetime.date(2003, 2, 17),
                          'prior_royalty_start_date': datetime.date(2003, 2, 19), 'advance_given': True,
                          'retention_end_date': datetime.date(2003, 2, 18), 'international_standard_code': 'DFG135',
                          'prior_royalty_status': 'D', 'agreement_end_date': datetime.date(2003, 2, 16),
                          'record_type': 'AGR', 'shares_change': True, 'post_term_collection_status': 'D',
                          'agreement_type': 'OS', 'submitter_agreement_n': 'AB12',
                          'society_assigned_agreement_n': 'DF35', 'record_sequence_n': 15,
                          'agreement_start_date': datetime.date(2003, 2, 15), 'transaction_sequence_n': 3,
                          'post_term_collection_end_date': datetime.date(2003, 2, 20), 'number_of_works': 12}]]

        dict = {'group_trailer': trailer, 'transactions': transactions, 'group_header': header}

        record = self._decoder.decode(dict)

        self.assertEqual('GRH', record.group_header.record_type)
        self.assertEqual('GRT', record.group_trailer.record_type)

        self.assertEqual('ACK', record.transactions[0][0].record_type)
