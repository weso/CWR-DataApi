# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Transmission patterns.

These are the grammatical structures for the Transmission Header and Transmission Trailer.
"""

# Transmission Header pattern
transmission_header = _factory_record.get_record('transmission_header')
transmission_header = transmission_header.setName('Transmission Header').setResultsName('transmission_header')

# Transmission Header pattern
transmission_trailer = _factory_record.get_record('transmission_trailer')
transmission_trailer = transmission_trailer.setName('Transmission Trailer').setResultsName('transmission_trailer')

transmission_trailer.leaveWhitespace()