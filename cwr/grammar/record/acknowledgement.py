# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Acknowledgement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Rules.
"""

# Acknowledgment Pattern
acknowledgement = _factory_record.get_record('acknowledgement')

message = field_special.lineStart + \
          field_record.record_prefix(_config.record_type('message')) + \
          _factory_field.get_field('message_type') + \
          _factory_field.get_field('original_record_sequence_n') + \
          _factory_field.get_field('message_record_type') + \
          _factory_field.get_field('message_level') + \
          _factory_field.get_field('validation') + \
          _factory_field.get_field('message_text') + \
          field_special.lineEnd

"""
Parsing actions for the patterns.
"""

acknowledgement.setParseAction(lambda a: _to_acknowledgement_record(a))

message.setParseAction(lambda a: _to_message_record(a))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_acknowledgement_record(parsed):
    """
    Transforms the final parsing result into an AcknowledgementRecord instance.

    :param parsed: result of parsing an Acknowledgement record
    :return: a AcknowledgementRecord created from the parsed record
    """
    return AcknowledgementRecord(record_type=parsed.record_type,
                                 transaction_sequence_n=parsed.transaction_sequence_n,
                                 record_sequence_n=parsed.record_sequence_n,
                                 original_group_id=parsed.original_group_id,
                                 original_transaction_sequence_n=parsed.original_transaction_sequence_n,
                                 original_transaction_type=parsed.original_transaction_type,
                                 transaction_status=parsed.transaction_status,
                                 creation_date_time=parsed.creation_date_time,
                                 processing_date=parsed.processing_date,
                                 creation_title=parsed.creation_title,
                                 submitter_creation_n=parsed.submitter_creation_n,
                                 recipient_creation_n=parsed.recipient_creation_n)


def _to_message_record(parsed):
    """
    Transforms the final parsing result into a MessageRecord instance.

    :param parsed: result of parsing a Message record
    :return: a MessageRecord created from the parsed record
    """
    return MessageRecord(record_type=parsed.record_type,
                         transaction_sequence_n=parsed.transaction_sequence_n,
                         record_sequence_n=parsed.record_sequence_n,
                         message_type=parsed.message_type,
                         message_text=parsed.message_text,
                         original_record_sequence_n=parsed.original_record_sequence_n,
                         message_record_type=parsed.message_record_type,
                         message_level=parsed.message_level,
                         validation_n=parsed.validation)