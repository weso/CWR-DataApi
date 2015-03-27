# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Publisher For Writer (PWR) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_factory_field = DefaultFieldFactory(_config.load_field_config('common'))

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Patterns.
"""

publisher = _factory_record.get_transaction_record('writer_publisher')