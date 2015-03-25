# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.transmission import TransmissionHeader, TransmissionTrailer
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


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
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory = DefaultFieldFactory(_data, CWRTables())

"""
Transmission patterns.

These are the grammatical structures for the Transmission Header and Transmission Trailer.
"""

# Transmission Header pattern
transmission_header = field_special.lineStart + \
                      field_record.record_type(_config.record_type('transmission_header')) + \
                      _factory.get_field('sender_type', compulsory=True) + \
                      _factory.get_field('sender_id', compulsory=True) + \
                      _factory.get_field('sender_name', compulsory=True) + \
                      _factory.get_field('edi_version', compulsory=True) + \
                      _factory.get_field('creation_date_time', compulsory=True) + \
                      _factory.get_field('transmission_date', compulsory=True) + \
                      _factory.get_field('character_set') + \
                      field_special.lineEnd
transmission_header = transmission_header.setName('Transmission Header').setResultsName('transmission_header')

# Transmission Header pattern
transmission_trailer = field_special.lineStart + \
                       field_record.record_type(_config.record_type('transmission_trailer')) + \
                       _factory.get_field('group_count', compulsory=True) + \
                       _factory.get_field('transaction_count', compulsory=True) + \
                       _factory.get_field('record_count', compulsory=True)
transmission_trailer = transmission_trailer.setName('Transmission Trailer').setResultsName('transmission_trailer')

transmission_trailer.leaveWhitespace()
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
    return TransmissionHeader(parsed.record_type, parsed.sender_id, parsed.sender_name, parsed.sender_type,
                              parsed.creation_date_time,
                              parsed.transmission_date, parsed.edi_version, parsed.character_set)


def _to_transmissiontrailer(parsed):
    """
    Transforms the final parsing result into a TransmissionTrailer instance.

    :param parsed: result of parsing a Transmission Trailer
    :return: a TransmissionTrailer created from the parsed record
    """
    return TransmissionTrailer(parsed.record_type, parsed.group_count, parsed.transaction_count, parsed.record_count)