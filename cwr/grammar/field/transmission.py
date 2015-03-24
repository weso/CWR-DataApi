# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table
from cwr.grammar.factory.field import DefaultFieldFactory


"""
CWR Transmission record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_common_factory = DefaultFieldFactory(_config.load_field_config('common'))

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

# Character Set
character_set = table.char_code(_config.field_size('transmission_header', 'character_set'), name='Character Set')
character_set = character_set.setResultsName('character_set')
