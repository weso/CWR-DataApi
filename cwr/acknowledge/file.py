# -*- coding: utf-8 -*-

import codecs
from datetime import date
import sys
from config_cwr.accessor import CWRConfiguration
from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.file import CWRFile, FileTag
from cwr.group import Group, GroupHeader, GroupTrailer
from cwr.parser.encoder.file import default_encoder_cwr_file

from cwr.record import TransactionRecord
from cwr.transmission import Transmission, TransmissionTrailer, TransmissionHeader
from cwr.utils.printer import CWRPrinter
from cwr.validation.common import ValidationStatus

"""
Class generate acknowledgement file"
"""

__author__ = 'Yaroslav O. Golub'
__license__ = 'MIT'
__status__ = 'Development'


class SequenceGenerator:
    def __init__(self, start=0):
        self._sequence = self.generator(start)

    @staticmethod
    def generator(start):
        num = start
        while True:
            yield num
            num += 1

    def get(self):
        return self._sequence.__next__()


class AcknowledgeFile(object):
    _acknowledge = None

    config = None

    def __init__(self, config, sequence_n, reciver):
        self.config = config
        tag = FileTag(self._year(), sequence_n, self._sender(), reciver, self._version())
        transmission = AcknowledgeTransmission(self.config['sender_id'],
                                               self.config['sender_name'],
                                               self.config['sender_type'])
        self._acknowledge = CWRFile(tag, transmission)

    @staticmethod
    def _year():
        return date.today().year

    def _sender(self):
        return self.config['sender_name']

    @staticmethod
    def _version():
        return "2.1"

    def validate_transaction(self, transaction):
        return ValidationStatus('AS')

    def acknowledge_cwr_file(self, cwr_file):
        assert isinstance(cwr_file, CWRFile)
        for group in cwr_file.transmission.groups:
            ack_group = AcknowledgeGroup(group)
            for transaction in group.transactions:
                status = self.validate_transaction(transaction)
                ack_transaction = AcknowledgeTransaction(group.group_header.group_id, transaction, status.code, status.message)
                ack_group.append_transaction(ack_transaction)
            self._acknowledge.transmission.append_group(ack_group)

    def print(self, path):
        output = codecs.open(path + '.ack.parsed', 'w', 'latin-1')
        printer = CWRPrinter()
        printer.print_file(self._acknowledge, output)

    def encode(self, path):
        output = codecs.open(path + '.ack', 'w', 'latin-1')
        out_old = sys.stdout
        sys.stdout = output
        file_encoder = default_encoder_cwr_file()
        result = file_encoder.encode(self._acknowledge.transmission)
        sys.stdout = out_old

    #self.acknowledge_transmission(cwr_file.transmission)

    # def acknowledge_transmission(self, transmission):
    #     assert isinstance(transmission, Transmission)
    #     for group in transmission.groups:
    #         ack_group = self.acknowledge_group(group)
    #         self._acknowledge.transmission.groups.append(ack_group)
    #     self._acknowledge.transmission.trailer.group_count = transmission.trailer.group_count
    #
    # def acknowledge_group(self, group):
    #     assert isinstance(group, Group)
    #     ack_header = GroupHeader()
    #     ack_group = Group()
    #     for transaction in group.transactions:
    #         self.acknowledge_transaction(transaction)
    #
    # def acknowledge_transaction(self, transaction):
    #     pass
    #
    # def get(self):
    #     return CWRFile


class AcknowledgeTransmission(Transmission):
    group_sequence = SequenceGenerator(0)

    def __init__(self, sender_id, sender_name, sender_type):
        record_type = 'HDR'
        creation_date_time = date.today()
        transmission_date = date.today()
        header = TransmissionHeader(record_type=record_type,
                                    sender_id=sender_id,
                                    sender_name=sender_name,
                                    sender_type=sender_type,
                                    creation_date_time=creation_date_time,
                                    transmission_date=transmission_date)
        trailer = TransmissionTrailer(record_type='TRL')
        super(AcknowledgeTransmission, self).__init__(header=header, trailer=trailer)

    def append_group(self, group):
        assert isinstance(group, AcknowledgeGroup)
        if self.groups is None:
            self.groups = []
        group.group_header.group_id = self.group_sequence.get()
        group.group_trailer.group_id = self.group_sequence.get()
        self.groups.append(group)
        self.trailer.group_count += 1
        self.trailer.transaction_count += group.group_trailer.transaction_count
        self.trailer.record_count += group.group_trailer.record_count


class AcknowledgeGroup(Group):
    transactions_sequence = SequenceGenerator(0)

    def __init__(self, original_group):
        header = GroupHeader(record_type='GRH',
                             transaction_type='ACK',
                             batch_request_id=original_group.group_header.batch_request_id)
        trailer = GroupTrailer(record_type='GRT')
        super(AcknowledgeGroup, self).__init__(group_header=header, group_trailer=trailer)

    def append_transaction(self, transaction):
        assert isinstance(transaction, AcknowledgeTransaction)
        transaction.transaction_sequence_n = self.transactions_sequence.get()
        self.transactions.append(transaction.records)
        self.group_trailer.transaction_count += 1
        self.group_trailer.record_count += len(transaction.records)


class AcknowledgeTransaction(object):
    record_sequence = SequenceGenerator(0)

    _transaction_sequence_n = 0

    def __init__(self, original_group_id, transaction, status, message=''):
        self._records = []
        original_transaction = transaction[0]
        ack = AcknowledgementRecord(record_type='ACK',
                                    record_sequence_n=self.record_sequence.get(),
                                    original_group_id=original_group_id,
                                    original_transaction_sequence_n=original_transaction.transaction_sequence_n,
                                    original_transaction_type=original_transaction.record_type,
                                    transaction_status=status,
                                    creation_date_time=date.today(),
                                    processing_date=date.today(),
                                    creation_title=original_transaction.title,
                                    submitter_creation_n='',
                                    recipient_creation_n='')
        self._records.append(ack)
        #if message:
        #    records.append(MessageRecord())
        for rec in transaction:
            self._records.append(rec)

    @property
    def transaction_sequence_n(self):
        return self._transaction_sequence_n

    @transaction_sequence_n.setter
    def transaction_sequence_n(self, value):
        for record in self._records:
            record.transaction_sequence_n = value
        self._transaction_sequence_n = value

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        self._records = value


def example_acknowledge_file(sequence_n, reciver):
    config = CWRConfiguration()
    return AcknowledgeFile(config.load_acknowledge_config('example'), sequence_n, reciver)
