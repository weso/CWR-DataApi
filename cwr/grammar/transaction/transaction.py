# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import writer, work
from cwr.grammar.transaction import interested_party, work_detail
from cwr.grammar.record import work_detail as rule_work_detail
from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

# Agreement
agreement_transaction = _factory_record.get_transaction_record('agreement') + \
                        pp.OneOrMore(interested_party.territory_information)

# Work
work_transaction = work.work_record + pp.Optional(pp.OneOrMore(interested_party.controlled_publisher_information)) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('publisher'))) + \
                   pp.Optional(pp.OneOrMore(interested_party.controlled_writer_information)) + \
                   pp.Optional(pp.OneOrMore(writer.writer)) + \
                   pp.Optional(pp.OneOrMore(rule_work_detail.alternate)) + \
                   pp.Optional(_factory_record.get_transaction_record('nra_title')) + \
                   pp.Optional(work_detail.information_for_excerpts) + \
                   pp.Optional(work_detail.information_for_versions) + \
                   pp.Optional(pp.OneOrMore(rule_work_detail.performing)) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('nra_performance_data'))) + \
                   pp.Optional(rule_work_detail.recording) + \
                   pp.Optional(rule_work_detail.origin) + \
                   pp.Optional(pp.OneOrMore(work_detail.instrumentation_information)) + \
                   pp.Optional(pp.OneOrMore(work_detail.information_for_components)) + \
                   pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('additional_related_information')))

# Acknowledgement
acknowledgement_transaction = _factory_record.get_transaction_record('acknowledgement') + \
                              pp.Optional(pp.OneOrMore(_factory_record.get_transaction_record('message'))) + \
                              (_factory_record.get_transaction_record('agreement') | (
                                  work.work_record + pp.Optional(work.conflict)))
