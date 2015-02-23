# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing import grammar
from cwr.file import TransmissionHeader


"""
CWR Transmission parsing classes.

These classes allow decoding and encoding Transmission records.

These are the Transmission Header (HDR) and Transmission Trailer (TRL).
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _to_edi_version(parsed):
    """
    Transforms a string with an EDI version into a float.

    :param parsed: result of parsing an EDI version number
    :return: a float with the EDI version
    """
    return float(parsed[0])


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


class TransmissionHeaderDecoder():
    """
    Parses a CWR Transmission Header (HDR) into a TransmissionHeader instance.

    The Transmission Header is the first record on the file.

    It is composed, in order, of:
    - Record type
    - Sender type
    - Sender ID
    - Sender Name
    - EDI Standard
    - Version Number
    - Creation Date
    - Creation Time
    - Transmission Date
    - Character Set
    """

    data = ParserDataStorage()

    # Fields
    _record_type = pp.Literal(data.expected_record_type('transmission_header')).setResultsName('record_type')
    _sender_type = pp.oneOf(data.sender_types()).setResultsName('sender_type')
    _sender_id = grammar.numeric(data.expected_record_field_size('transmission_header', 'sender_id')).setResultsName(
        'sender_id')
    _sender_name = grammar.alphanum(
        data.expected_record_field_size('transmission_header', 'sender_name')).setResultsName('sender_name')
    _edi_version = pp.Literal(data.expected_record_field_value('transmission_header', 'edi_version')).setResultsName(
        'edi_version')
    _creation_date = grammar.date_field.setResultsName('creation_date')
    _creation_time = grammar.time_field.setResultsName('creation_time')
    _transmission_date = grammar.date_field.setResultsName('transmission_date')
    _character_set = grammar.char_code(
        data.expected_record_field_size('transmission_header', 'character_set')).setResultsName('character_set')

    # Transmission Header pattern
    _pattern = grammar.lineStart + _record_type + _sender_type + _sender_id + _sender_name + _edi_version + \
               _creation_date + _creation_time + _transmission_date + (_character_set | pp.empty) + grammar.lineEnd

    # Parsing actions
    _edi_version.setParseAction(_to_edi_version)
    _pattern.setParseAction(_to_transmissionheader)

    def __init__(self):
        pass

    def decode(self, record):
        """
        Decodes the Transmission Header, creating a TransmissionHeader from it.

        :param record: the record to parse
        :return: a TransmissionHeader created from the record
        """
        return self._pattern.parseString(record)[0]