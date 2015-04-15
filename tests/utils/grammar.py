# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import DefaultPrefixBuilder, DefaultRecordFactory

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def getCommonGrammar(id):
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))

    _factory_field = DefaultFieldFactory(_data, CWRTables())

    _prefixer = DefaultPrefixBuilder(_config.record_types(), _factory_field)
    _factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

    return _factory_record.get_record(id)


def getFilenameGrammar(id):
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))
    _data.update(_config.load_field_config('filename'))

    _factory_field = DefaultFieldFactory(_data, CWRTables())

    _prefixer = DefaultPrefixBuilder(_config.record_types(), _factory_field)
    _factory_record = DefaultRecordFactory(_config.load_record_config('filename'), _prefixer, _factory_field)

    return _factory_record.get_record(id)