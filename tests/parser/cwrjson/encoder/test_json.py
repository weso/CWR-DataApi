# -*- coding: utf-8 -*-

import unittest
import datetime
import json

from cwr.parser.encoder.cwrjson import JSONEncoder
from cwr.file import FileTag, CWRFile
from cwr.group import GroupHeader, GroupTrailer, Group
from cwr.work import WorkRecord
from cwr.agreement import AgreementRecord
from cwr.transmission import TransmissionTrailer, TransmissionHeader, Transmission


"""
Group from dictionary encoding tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestFileJSONEncoding(unittest.TestCase):
    def setUp(self):
        self._encoder = JSONEncoder()

    def test_file_agreement(self):
        tag = self._get_file_tag()
        transmission = self._get_transmission_agreement()

        data = CWRFile(tag, transmission)

        encoded = self._encoder.encode(data)

        expected = json.loads(
            '{"transmission": {"header": {"creation_date_time": "2003-02-16", "sender_name": "SENDER", "sender_id": "ABC334", "sender_type": "SO", "record_type": "HDR", "edi_standard": "01.10", "transmission_date": "2003-02-17", "character_set": "ASCII"}, "groups": [{"group_trailer": {"record_count": 20, "record_type": "GRT", "group_id": 3, "transaction_count": 15}, "transactions": [[{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}], [{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}]], "group_header": {"record_type": "GRH", "version_number": "02.10", "group_id": 3, "batch_request_id": 15, "transaction_type": "AGR"}}, {"group_trailer": {"record_count": 20, "record_type": "GRT", "group_id": 3, "transaction_count": 15}, "transactions": [[{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}], [{"sales_manufacture_clause": "M", "date_of_signature": "2003-02-17", "prior_royalty_start_date": "2003-02-19", "advance_given": true, "retention_end_date": "2003-02-18", "international_standard_code": "DFG135", "prior_royalty_status": "D", "agreement_end_date": "2003-02-16", "record_type": "AGR", "shares_change": true, "post_term_collection_status": "D", "agreement_type": "OS", "submitter_agreement_n": "AB12", "society_assigned_agreement_n": "DF35", "record_sequence_n": 15, "agreement_start_date": "2003-02-15", "transaction_sequence_n": 3, "post_term_collection_end_date": "2003-02-20", "number_of_works": 12}]], "group_header": {"record_type": "GRH", "version_number": "02.10", "group_id": 3, "batch_request_id": 15, "transaction_type": "AGR"}}], "trailer": {"record_type": "TRL", "group_count": 155, "record_count": 568, "transaction_count": 245}}, "tag": {"sequence_n": 123, "receiver": "RCV", "sender": "SND", "version": 2.1, "year": 2015}}')

        self.assertEqual(expected, json.loads(encoded))

    def test_file_work_with_nones(self):
        tag = self._get_file_tag()
        transmission = self._get_transmission_work()

        data = CWRFile(tag, transmission)

        encoded = self._encoder.encode(data)

        expected = json.loads(
            '{"transmission": {"header": {"creation_date_time": "2003-02-16", "sender_name": "SENDER", "sender_id": "ABC334", "sender_type": "SO", "record_type": "HDR", "edi_standard": "01.10", "transmission_date": "2003-02-17", "character_set": "ASCII"}, "groups": [{"group_trailer": {"record_count": 20, "record_type": "GRT", "group_id": 3, "transaction_count": 15}, "transactions": [[{"opus_number": "OP35", "recorded_indicator": "Y", "contact_id": "123CONTACT", "record_sequence_n": 15, "music_arrangement": "ORI", "language_code": "ES", "duration": "01:12:00", "contact_name": "THE CONTACT", "composite_type": "MED", "lyric_adaptation": "MOD", "title": "TITLE", "transaction_sequence_n": 3, "excerpt_type": "MOV", "submitter_work_n": "ABC123", "priority_flag": "Y", "copyright_number": "ABDF146", "text_music_relationship": "MTX", "work_type": "BL", "grand_rights_indicator": true, "date_publication_printed_edition": "2003-02-16", "musical_work_distribution_category": "SER", "catalogue_number": "GGH97", "composite_component_count": 5, "exceptional_clause": "Y", "record_type": "NWR", "iswc": null, "version_type": "ORI", "copyright_date": "2003-02-17"}]], "group_header": {"record_type": "GRH", "version_number": "02.10", "group_id": 3, "batch_request_id": 15, "transaction_type": "NWR"}}], "trailer": {"record_type": "TRL", "group_count": 155, "record_count": 568, "transaction_count": 245}}, "tag": {"sequence_n": 123, "receiver": "RCV", "sender": "SND", "version": 2.1, "year": 2015}}')

        self.assertEqual(expected, json.loads(encoded))


    def _get_file_tag(self):
        return FileTag(year=2015,
                       sequence_n=123,
                       sender='SND',
                       receiver='RCV',
                       version=2.1)

    def _get_transmission_agreement(self):
        header = TransmissionHeader(record_type='HDR',
                                    sender_id='ABC334',
                                    sender_name='SENDER',
                                    sender_type='SO',
                                    creation_date_time=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                                    transmission_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                                    edi_standard='01.10',
                                    character_set='ASCII')
        trailer = TransmissionTrailer(record_type='TRL',
                                      group_count=155,
                                      transaction_count=245,
                                      record_count=568)
        groups = [self._get_group_agreement(), self._get_group_agreement()]

        return Transmission(header, trailer, groups)

    def _get_transmission_work(self):
        header = TransmissionHeader(record_type='HDR',
                                    sender_id='ABC334',
                                    sender_name='SENDER',
                                    sender_type='SO',
                                    creation_date_time=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                                    transmission_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                                    edi_standard='01.10',
                                    character_set='ASCII')
        trailer = TransmissionTrailer(record_type='TRL',
                                      group_count=155,
                                      transaction_count=245,
                                      record_count=568)
        groups = [self._get_group_work()]

        return Transmission(header, trailer, groups)

    def _get_group_agreement(self):
        header = GroupHeader(record_type='GRH',
                             group_id=3,
                             transaction_type='AGR',
                             version_number='02.10',
                             batch_request_id=15)
        trailer = GroupTrailer(record_type='GRT',
                               group_id=3,
                               transaction_count=15,
                               record_count=20)
        transactions = [self._get_transaction_agreement(), self._get_transaction_agreement()]

        return Group(header, trailer, transactions)

    def _get_group_work(self):
        header = GroupHeader(record_type='GRH',
                             group_id=3,
                             transaction_type='NWR',
                             version_number='02.10',
                             batch_request_id=15)
        trailer = GroupTrailer(record_type='GRT',
                               group_id=3,
                               transaction_count=15,
                               record_count=20)
        transactions = [self._get_transaction_work()]

        return Group(header, trailer, transactions)

    def _get_transaction_agreement(self):
        return [self._get_agreement()]

    def _get_transaction_work(self):
        return [self._get_work()]

    def _get_agreement(self):
        return AgreementRecord(record_type='AGR',
                               transaction_sequence_n=3,
                               record_sequence_n=15,
                               submitter_agreement_n='AB12',
                               agreement_type='OS',
                               agreement_start_date=datetime.datetime.strptime('20030215', '%Y%m%d').date(),
                               number_of_works=12,
                               prior_royalty_status='D',
                               post_term_collection_status='D',
                               international_standard_code='DFG135',
                               society_assigned_agreement_n='DF35',
                               sales_manufacture_clause='M',
                               agreement_end_date=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                               date_of_signature=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                               retention_end_date=datetime.datetime.strptime('20030218', '%Y%m%d').date(),
                               prior_royalty_start_date=datetime.datetime.strptime('20030219', '%Y%m%d').date(),
                               post_term_collection_end_date=datetime.datetime.strptime('20030220', '%Y%m%d').date(),
                               shares_change=True,
                               advance_given=True)

    def _get_work(self):
        return WorkRecord(record_type='NWR',
                          transaction_sequence_n=3,
                          record_sequence_n=15,
                          submitter_work_n='ABC123',
                          title='TITLE',
                          version_type='ORI',
                          musical_work_distribution_category='SER',
                          date_publication_printed_edition=datetime.datetime.strptime('20030216', '%Y%m%d').date(),
                          text_music_relationship='MTX',
                          language_code='ES',
                          copyright_number='ABDF146',
                          copyright_date=datetime.datetime.strptime('20030217', '%Y%m%d').date(),
                          music_arrangement='ORI',
                          lyric_adaptation='MOD',
                          excerpt_type='MOV',
                          composite_type='MED',
                          composite_component_count=5,
                          iswc=None,
                          work_type='BL',
                          duration=datetime.datetime.strptime('011200', '%H%M%S').time(),
                          catalogue_number='GGH97',
                          opus_number='OP35',
                          contact_id='123CONTACT',
                          contact_name='THE CONTACT',
                          recorded_indicator='Y',
                          priority_flag='Y',
                          exceptional_clause='Y',
                          grand_rights_indicator=True)