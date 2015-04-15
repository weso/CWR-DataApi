# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldTerminalRuleFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import RecordRuleDecorator
from cwr.grammar.factory.rule import DefaultGroupRuleFactory

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def getRecordGrammar(id):
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))

    _factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

    _decorators = {'transaction': RecordRuleDecorator(_factory_field), 'record': RecordRuleDecorator(_factory_field)}
    _group_rule_factory = DefaultGroupRuleFactory(_config.load_record_config('common'), _factory_field, _decorators)

    return _group_rule_factory.get_rule(id)


def getTransactionGrammar(id):
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))

    _factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

    _rules = _config.load_transaction_config('common')
    _rules.update(_config.load_record_config('common'))

    _decorators = {'transaction': RecordRuleDecorator(_factory_field), 'record': RecordRuleDecorator(_factory_field)}
    _group_rule_factory = DefaultGroupRuleFactory(_rules, _factory_field, _decorators)

    return _group_rule_factory.get_rule(id)


def getFilenameGrammar(id):
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))
    _data.update(_config.load_field_config('filename'))

    _factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

    _group_rule_factory = DefaultGroupRuleFactory(_config.load_record_config('filename'), _factory_field)

    return _group_rule_factory.get_rule(id)