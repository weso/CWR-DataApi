# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import AcknowledgementDictionaryDecoder, MessageDictionaryDecoder


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
acknowledgement = _factory_record.get_transaction_record('acknowledgement')

message = _factory_record.get_transaction_record('message')

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
    decoder = AcknowledgementDictionaryDecoder()
    return decoder.decode(parsed)


def _to_message_record(parsed):
    """
    Transforms the final parsing result into a MessageRecord instance.

    :param parsed: result of parsing a Message record
    :return: a MessageRecord created from the parsed record
    """
    decoder = MessageDictionaryDecoder()
    return decoder.decode(parsed)