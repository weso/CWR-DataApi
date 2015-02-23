# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special
from cwr.file import TransmissionHeader


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
record_type = pp.Literal(data.expected_record_type('transmission_header'))
record_type.setName('Record Type')
record_type.setResultsName('record_type')

sender_type = pp.oneOf(data.sender_types())
record_type.setName('Sender Type')
sender_type.setResultsName('sender_type')

sender_id = field.numeric(data.expected_record_field_size('transmission_header', 'sender_id'))
record_type.setName('Sender ID')
sender_id.setResultsName('sender_id')

sender_name = field.alphanum(data.expected_record_field_size('transmission_header', 'sender_name'))
record_type.setName('Sender Name')
sender_name.setResultsName('sender_name')

edi_version = pp.Literal(data.expected_record_field_value('transmission_header', 'edi_version'))
record_type.setName('EDI Version')
edi_version.setResultsName('edi_version')

creation_date = field.date_field.setResultsName('creation_date')
record_type.setName('Creation Date')

creation_time = field.time_field.setResultsName('creation_time')
record_type.setName('Creation Time')

transmission_date = field.date_field.setResultsName('transmission_date')
record_type.setName('Transmission Date')

character_set = special.char_code(
    data.expected_record_field_size('transmission_header', 'character_set'))
character_set.setResultsName('character_set')
record_type.setName('Character Set')


# Transmission Header pattern
transmission_header = special.lineStart + record_type + sender_type + sender_id + sender_name + edi_version + \
                      creation_date + creation_time + transmission_date + (character_set | pp.empty) + special.lineEnd


# Parsing actions
edi_version.setParseAction(lambda v: float(v[0]))
transmission_header.setParseAction(lambda h: _to_transmissionheader(h))


def _to_transmissionheader(parsed):
    """
    Transforms the final parsing result into a TransmissionHeader instance.

    :param parsed: result of parsing a record prefix
    :return: a TransmissionHeader created from the record prefix
    """
    creation_datetime = datetime.datetime.combine(parsed.creation_date, parsed.creation_time)

    return TransmissionHeader(parsed.record_type, parsed.sender_id, parsed.sender_name, parsed.sender_type,
                              creation_datetime,
                              parsed.transmission_date, parsed.edi_version, parsed.character_set)