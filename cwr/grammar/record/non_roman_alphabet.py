# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Non-Roman Alphabet records grammar.

This is for the following records:
- Non-Roman Alphabet Agreement Party Name (NPA)
- Non-Roman Alphabet Publisher Name (NPN)
- Non-Roman Alphabet Writer Name (NWN)
- Non-Roman Alphabet Title (NAT)
- Performance Data in non-roman alphabet (NPR)
- Non-Roman Alphabet Entire Work Title for Excerpts (NET)
- Non-Roman Alphabet Title for Components (NCT)
- Non-Roman Alphabet Original Title for Version (NVT)
- Non-Roman Alphabet Other Writer Name (NOW)
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
NRA patterns.
"""

npa = _factory_record.get_transaction_record('nra_agreement_party')

npn = _factory_record.get_transaction_record('nra_publisher_name')

nwn = _factory_record.get_transaction_record('nra_writer_name')

nat = _factory_record.get_transaction_record('nra_title')

npr = _factory_record.get_transaction_record('nra_performance_data')

nra_work = _factory_record.get_transaction_record('nra_work')

now = _factory_record.get_transaction_record('nra_other_writer')