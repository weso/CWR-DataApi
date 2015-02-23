# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special, record
from cwr.file import TransmissionHeader, TransmissionTrailer


"""
CWR Transmission grammar.

This stores grammar for parsing the CWR Transmission Header and Transmission Trailer.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

# Fields
record_type_header = pp.Literal(data.record_type('transmission_header'))
record_type_header = record_type_header.setName('Record Type').setResultsName('record_type')

record_type_trailer = pp.Literal(data.record_type('transmission_trailer'))
record_type_trailer = record_type_trailer.setName('Record Type').setResultsName('record_type')

sender_type = pp.oneOf(data.sender_types())
sender_type = sender_type.setName('Sender Type').setResultsName('sender_type')

sender_id = field.numeric(data.field_size('transmission_header', 'sender_id'))
sender_id = sender_id.setName('Sender ID').setResultsName('sender_id')

sender_name = field.alphanum(data.field_size('transmission_header', 'sender_name'))
sender_name = sender_name.setName('Sender Name').setResultsName('sender_name')

edi_version = pp.Literal(data.field_value('transmission_header', 'edi_version'))
edi_version = edi_version.setName('EDI Version').setResultsName('edi_version')

creation_date = field.date_field.setResultsName('creation_date')
creation_date = creation_date.setName('Creation Date')

creation_time = field.time_field.setResultsName('creation_time')
creation_time = creation_time.setName('Creation Time')

transmission_date = field.date_field.setResultsName('transmission_date')
transmission_date = transmission_date.setName('Transmission Date')

character_set = special.char_code(
    data.field_size('transmission_header', 'character_set'))
character_set = character_set.setResultsName('character_set').setName('Character Set')


# Transmission Header pattern
transmission_header = special.lineStart + record_type_header + sender_type + sender_id + sender_name + edi_version + \
                      creation_date + creation_time + transmission_date + (character_set | pp.empty) + special.lineEnd
transmission_trailer = special.lineStart + record_type_trailer + record.group_count + record.transaction_count + \
                       record.record_count + special.lineEnd


# Parsing actions
transmission_header.setParseAction(lambda h: _to_transmissionheader(h))
transmission_trailer.setParseAction(lambda t: _to_transmissiontrailer(t))


def _to_transmissionheader(parsed):
    """
    Transforms the final parsing result into a TransmissionHeader instance.

    :param parsed: result of parsing a Transmission Header
    :return: a TransmissionHeader created from the record prefix
    """
    creation_datetime = datetime.datetime.combine(parsed.creation_date, parsed.creation_time)

    return TransmissionHeader(parsed.record_type, parsed.sender_id, parsed.sender_name, parsed.sender_type,
                              creation_datetime,
                              parsed.transmission_date, parsed.edi_version, parsed.character_set)


def _to_transmissiontrailer(parsed):
    """
    Transforms the final parsing result into a TransmissionTrailer instance.

    :param parsed: result of parsing a Transmission Trailer
    :return: a TransmissionTrailer created from the record prefix
    """
    return TransmissionTrailer(parsed.record_type, parsed.group_count, parsed.transaction_count, parsed.record_count)