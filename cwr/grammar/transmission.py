# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.data.accessor import ParserDataStorage
from cwr.grammar import field, special, record
from cwr.transmission import TransmissionHeader, TransmissionTrailer


"""
CWR Transmission grammar.

This stores grammar for parsing the CWR Transmission Header and Transmission Trailer.

The Transmission Header contains the following fields:
- Record Type.
- Sender Type.
- Sender ID.
- Sender Name
- EDI Version.
- Creation Date.
- Creation Time.
- Transmission Date.
- Character Set.

The Transmission Trailer contains the following fields:
- Record Type.
- Group Count.
- Transaction Count.
- Record Count.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

"""
Transmission fields.

These fields are:
- Record Type. One for the header and another for the trailer, both a pre-defined string.
- Sender Type. Alphanumeric.
- Sender ID. Alphanumeric.
- Sender Name. Alphanumeric.
- EDI Version. Must be a predefined string.
- Creation Date. Date.
- Creation Time. Time.
- Transmission Date. Date.
- Character Set. Alphanumeric.
"""

# Record Type for the header
record_type_header = record.record_type(data.record_type('transmission_header'))

# Record Type for the trailer
record_type_trailer = record.record_type(data.record_type('transmission_trailer'))

# Sender Type
sender_type = pp.oneOf(data.sender_types())
sender_type = sender_type.setName('Sender Type').setResultsName('sender_type')

# Sender ID
sender_id = field.numeric(data.field_size('transmission_header', 'sender_id'))
sender_id = sender_id.setName('Sender ID').setResultsName('sender_id')

# Sender Name
sender_name = field.alphanum(data.field_size('transmission_header', 'sender_name'))
sender_name = sender_name.setName('Sender Name').setResultsName('sender_name')

# EDI Version
edi_version = pp.Literal(data.field_value('transmission_header', 'edi_version'))
edi_version = edi_version.setName('EDI Version').setResultsName('edi_version')

# Creation Date
creation_date = field.date(compulsory=True)
creation_date = creation_date.setName('Creation Date').setResultsName('creation_date')

# Creation Time
creation_time = field.time()
creation_time = creation_time.setName('Creation Time').setResultsName('creation_time')

# Transmission Date
transmission_date = field.date(compulsory=True)
transmission_date = transmission_date.setName('Transmission Date').setResultsName('transmission_date')

# Character Set
character_set = special.char_code(
    data.field_size('transmission_header', 'character_set'))
character_set = character_set.setName('Character Set').setResultsName('character_set')

"""
Transmission patterns.

These are the grammatical structures for the Transmission Header and Transmission Trailer.
"""

# Transmission Header pattern
transmission_header = special.lineStart + record_type_header + sender_type + sender_id + sender_name + edi_version + \
                      creation_date + creation_time + transmission_date + (character_set | pp.empty) + special.lineEnd
# Transmission Header pattern
transmission_trailer = special.lineStart + record_type_trailer + record.group_count + record.transaction_count + \
                       record.record_count + special.lineEnd

"""
Parsing actions for the patterns.

The header will be parsed into a TransmissionHeader and the trailer into a TransmissionTrailer.
"""

transmission_header.setParseAction(lambda h: _to_transmissionheader(h))
transmission_trailer.setParseAction(lambda t: _to_transmissiontrailer(t))


def _to_transmissionheader(parsed):
    """
    Transforms the final parsing result into a TransmissionHeader instance.

    :param parsed: result of parsing a Transmission Header
    :return: a TransmissionHeader created from the parsed record
    """
    creation_datetime = datetime.datetime.combine(parsed.creation_date, parsed.creation_time)

    return TransmissionHeader(parsed.record_type, parsed.sender_id, parsed.sender_name, parsed.sender_type,
                              creation_datetime,
                              parsed.transmission_date, parsed.edi_version, parsed.character_set)


def _to_transmissiontrailer(parsed):
    """
    Transforms the final parsing result into a TransmissionTrailer instance.

    :param parsed: result of parsing a Transmission Trailer
    :return: a TransmissionTrailer created from the parsed record
    """
    return TransmissionTrailer(parsed.record_type, parsed.group_count, parsed.transaction_count, parsed.record_count)