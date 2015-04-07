# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Work detail grammar.

This is for the following records:
- Alternate Title (ALT)
- Entire Work Title for Excerpts (EWT)
- Original Work Title for Versions (VER)
- Performing Artist (PER)
- Recording Detail (REC)
- Work Origin (ORN)
- Instrumentation Summary (INS)
- Instrumentation Detail (IND)
- Component (COM)
- Additional Related Information (ARI)
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
Patterns.
"""

alternate = _factory_record.get_transaction_record('work_alternate_title')

entire_title = _factory_record.get_transaction_record('entire_work_title')

version = _factory_record.get_transaction_record('original_work_title')

performing = _factory_record.get_transaction_record('performing_artist')

recording = _factory_record.get_transaction_record('recording_detail')

origin = _factory_record.get_transaction_record('work_origin')

inst_summary = _factory_record.get_transaction_record('instrumentation_summary')

inst_detail = _factory_record.get_transaction_record('instrumentation_detail')

component = _factory_record.get_transaction_record('component')