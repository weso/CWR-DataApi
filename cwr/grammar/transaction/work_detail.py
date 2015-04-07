# -*- coding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR work detail grammar.

This contains rules for work details.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

# Instrumentation
instrumentation_information = _factory_record.get_transaction_record('instrumentation_summary') + \
                              pp.Optional(
                                  pp.OneOrMore(_factory_record.get_transaction_record('instrumentation_detail')))

# Excerpts
information_for_excerpts = _factory_record.get_transaction_record('entire_work_title') + \
                           pp.Optional(_factory_record.get_transaction_record('nra_work')) + \
                           pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('nra_other_writer')))

# Versions
information_for_versions = _factory_record.get_transaction_record('original_work_title') + \
                           pp.Optional(_factory_record.get_transaction_record('nra_work')) + \
                           pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('nra_other_writer')))

# Components
information_for_components = _factory_record.get_transaction_record('component') + \
                             pp.Optional(_factory_record.get_transaction_record('nra_work')) + \
                             pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('nra_other_writer')))
