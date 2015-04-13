# -*- coding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, DefaultRecordFactory
from cwr.grammar.factory.transaction import DefaultTransactionFactory


"""
CWR transaction grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)
_factory_transaction = DefaultTransactionFactory(_config.load_transaction_config('common'), _factory_record)

# Agreement
agreement_transaction = _factory_record.get_record('agreement') + \
                        pp.OneOrMore(_factory_transaction.get_transaction('territory_information'))

# Work
work_transaction = _factory_record.get_record('work') + \
                   pp.Optional(pp.OneOrMore(_factory_transaction.get_transaction('controlled_publisher_information'))) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('publisher'))) + \
                   pp.Optional(pp.OneOrMore(_factory_transaction.get_transaction('controlled_writer_information'))) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('writer'))) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('work_alternate_title'))) + \
                   pp.Optional(_factory_record.get_record('nra_title')) + \
                   pp.Optional(_factory_transaction.get_transaction('information_for_excerpts')) + \
                   pp.Optional(_factory_transaction.get_transaction('information_for_versions')) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('performing_artist'))) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('nra_performance_data'))) + \
                   pp.Optional(_factory_record.get_record('recording_detail')) + \
                   pp.Optional(_factory_record.get_record('work_origin')) + \
                   pp.Optional(pp.OneOrMore(_factory_transaction.get_transaction('instrumentation_information'))) + \
                   pp.Optional(pp.OneOrMore(_factory_transaction.get_transaction('information_for_components'))) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_record('additional_related_information')))

# Acknowledgement
acknowledgement_transaction = _factory_record.get_record('acknowledgement') + \
                              pp.Optional(pp.OneOrMore(_factory_record.get_record('message'))) + \
                              (_factory_record.get_record('agreement') | (
                                  _factory_record.get_record('work') +
                                  pp.Optional(_factory_record.get_record('work_conflict'))))
