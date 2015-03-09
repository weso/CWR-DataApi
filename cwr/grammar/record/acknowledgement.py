# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import acknowledgement as field_ack
from cwr.grammar.field import message as field_message
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.acknowledgement import AcknowledgementRecord, MessageRecord


"""
CWR Acknowledgement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Rules.
"""

# Acknowledgment Pattern
acknowledgement = field_special.lineStart + field_record.record_prefix(_config.record_type('acknowledgement'),
                                                                       compulsory=True) + \
                  field_ack.creation_date_time + \
                  field_ack.original_group_id + field_ack.original_transaction_n + field_table.original_transaction_type(
    True) + field_ack.creation_title + \
                  field_ack.submitter_creation_n + field_ack.recipient_creation_n + field_ack.processing_date + field_table.transaction_status(
    True) + \
                  field_special.lineEnd

message = field_special.lineStart + field_record.record_prefix(_config.record_type('message'),
                                                               compulsory=True) + field_table.message_types() + \
          field_message.sequence_n + field_message.record_message + field_table.message_levels() + field_message.validation + field_message.message_text + \
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
    return AcknowledgementRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                 parsed.group_id, parsed.transaction_n, parsed.transaction_type,
                                 parsed.transaction_status, parsed.creation_date_time, parsed.processing_date,
                                 parsed.title, parsed.submitter_id, parsed.recipient_id)


def _to_message_record(parsed):
    """
    Transforms the final parsing result into a MessageRecord instance.

    :param parsed: result of parsing a Message record
    :return: a MessageRecord created from the parsed record
    """
    return MessageRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                         parsed.message_type,
                         parsed.text, parsed.sequence_n, parsed.message_record_type, parsed.message_level,
                         parsed.validation)