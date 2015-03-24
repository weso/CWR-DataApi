# -*- coding: utf-8 -*-

import datetime

import pyparsing as pp

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
_transmission_factory = DefaultFieldFactory(_config.load_field_config('transmission'))

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

# EDI Version
edi_version = pp.Literal(_config.field_value('transmission_header', 'edi_version'))
edi_version = edi_version.setName('EDI Version').setResultsName('edi_version')

# Creation Date
creation_date = _transmission_factory.get_field('creation_date', compulsory=True)

# Creation Time
creation_time = _transmission_factory.get_field('creation_time')

# Character Set
character_set = table.char_code(_config.field_size('transmission_header', 'character_set'))
character_set = character_set.setName('Character Set').setResultsName('character_set')

"""
Rules
"""

# Creation date and time pattern
creation_date_time = pp.Group(creation_date + creation_time)
creation_date_time = creation_date_time.setName('Creation Date and Time').setResultsName('creation_date_time')

"""
Parsing actions
"""

creation_date_time.setParseAction(lambda d: _combine_date_time(d[0].creation_date, d[0].creation_time))


def _combine_date_time(date, time):
    """
    Combines the received date and time.

    :param date: date to combine
    :param time: time to combine
    :return: the date and time combined
    """
    return datetime.datetime.combine(date, time)