# -*- coding: utf-8 -*-

import unittest

from cwr.parser.decoder.cwrjson import JSONDecoder

"""
Group from dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileJSONDecoding(unittest.TestCase):
    def setUp(self):
        self._decoder = JSONDecoder()

    def test_file(self):
        value = '{"transmission": {"header": {"creation_date_time": "2003-02-16", "sender_name": "SENDER", "sender_id": "ABC334", "sender_type": "SO", "record_type": "HDR", "edi_standard": "01.10", "transmission_date": "2003-02-17", "character_set": "ASCII"}, "groups": [{"group_trailer": {"record_count": 20, "record_type": "GRT", "group_id": 3, "transaction_count": 15}, "transactions": [[{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}], [{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}]], "group_header": {"record_type": "GRH", "version_number": "02.10", "group_id": 3, "batch_request_id": 15, "transaction_type": "AGR"}}, {"group_trailer": {"record_count": 20, "record_type": "GRT", "group_id": 3, "transaction_count": 15}, "transactions": [[{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}], [{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}]], "group_header": {"record_type": "GRH", "version_number": "02.10", "group_id": 3, "batch_request_id": 15, "transaction_type": "AGR"}}], "trailer": {"record_type": "TRL", "group_count": 155, "record_count": 568, "transaction_count": 245}}, "tag": {"sequence_n": 123, "receiver": "RCV", "sender": "SND", "version": 2.1, "year": 2015}}'

        result = self._decoder.decode(value)

        tag = result.tag

        self.assertEqual('SND', tag.sender)

        transmission = result.transmission

        self.assertEqual('HDR', transmission.header.record_type)
        self.assertEqual('TRL', transmission.trailer.record_type)

        groups = transmission.groups

        self.assertEqual(2, len(groups))

        group = groups[0]

        self.assertEqual('GRH', group.group_header.record_type)
        self.assertEqual('GRT', group.group_trailer.record_type)

        self.assertEqual('AGR', group.group_header.transaction_type)

        transactions = group.transactions

        self.assertEqual(2, len(transactions))

        self.assertEqual('AGR', transactions[0][0].record_type)
