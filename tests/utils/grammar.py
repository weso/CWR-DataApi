# -*- coding: utf-8 -*-

from data_commonworks.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldTerminalRuleFactory
from data_commonworks.accessor import CWRTables
from cwr.grammar.factory.decorator import RecordRuleDecorator, GroupRuleDecorator
from cwr.grammar.factory.rule import DefaultRuleFactory

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))
_data.update(_config.load_field_config('filename'))

_factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

_rules = _config.load_transaction_config('common')
_rules.update(_config.load_record_config('common'))
_rules.update(_config.load_group_config('common'))

_decorators = {'transaction': RecordRuleDecorator(_factory_field), 'record': RecordRuleDecorator(_factory_field),
               'group': GroupRuleDecorator()}
_group_rule_factory = DefaultRuleFactory(_rules, _factory_field, _decorators)

_group_rule_factory_filename = DefaultRuleFactory(_config.load_record_config('filename'), _factory_field)


def getRecordGrammar(id):
    return _group_rule_factory.get_rule(id)


def getFilenameGrammar(id):
    return _group_rule_factory_filename.get_rule(id)