# -*- coding: utf-8 -*-

from cwr.acknowledgement import AcknowledgementRecord, MessageRecord

from cwr.parser.common import Encoder


"""
Offers classes to parse CWR objects from and into dictionaries.

This helps for example to create JSON or Mongo objects.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRDictionaryEncoder(Encoder):
    """
    Encodes CWR model classes into dictionaries.
    """

    def __init__(self):
        super(CWRDictionaryEncoder, self).__init__()

    def encode(self, object):
        if isinstance(object, AcknowledgementRecord):
            encoded = self.__encode_acknowledgement_record(object)
        elif isinstance(object, MessageRecord):
            encoded = self.__encode_message_record(object)
        else:
            encoded = None

        return encoded

    def __encode_transaction_record_head(self, record):
        """
        Creates the head of a transaction record.

        :param record: the record with the head to transform into a dictionary
        :return: a dictionary created from the record head
        """
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['transaction_sequence_n'] = record.transaction_sequence_n
        encoded['record_sequence_n'] = record.record_sequence_n

        return encoded

    def __encode_acknowledgement_record(self, record):
        """
        Creates a dictionary from an AcknowledgementRecord.

        :param record: the AcknowledgementRecord to transform into a dictionary
        :return: a dictionary created from the AcknowledgementRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['creation_date_time'] = record.creation_date_time
        encoded['creation_title'] = record.creation_title
        encoded['original_group_id'] = record.original_group_id
        encoded['original_transaction_sequence_n'] = record.original_transaction_sequence_n
        encoded['original_transaction_type'] = record.original_transaction_type
        encoded['processing_date'] = record.processing_date
        encoded['recipient_creation_n'] = record.recipient_creation_n
        encoded['submitter_creation_n'] = record.submitter_creation_n
        encoded['transaction_status'] = record.transaction_status

        return encoded

    def __encode_message_record(self, record):
        """
        Creates a dictionary from a MessageRecord.

        :param record: the MessageRecord to transform into a dictionary
        :return: a dictionary created from the MessageRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['message_level'] = record.message_level
        encoded['message_record_type'] = record.message_record_type
        encoded['message_text'] = record.message_text
        encoded['message_type'] = record.message_type
        encoded['original_record_sequence_n'] = record.original_record_sequence_n
        encoded['validation_n'] = record.validation_n

        return encoded