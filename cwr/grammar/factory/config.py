# -*- coding: utf-8 -*-

import pyparsing as pp

"""
Classes for handling the configuration files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

rule_at_least = \
    pp.Literal('at_least_').suppress() + \
    pp.Word(pp.nums).setResultsName('count')
rule_at_least.setParseAction(lambda v: int(v[0]))

_rule_config_string = pp.Regex('[^()\[\]\\n,:]*')
_rule_config_string.setParseAction(lambda v: v[0].strip())

_rule_identifier = _rule_config_string + pp.Literal(':').suppress()
_rule_identifier.setParseAction(lambda rule: rule[0])

_rule_options_list = pp.Group(pp.delimitedList(_rule_config_string))
_rule_options_list.setParseAction(lambda rule: rule[0].asList())

rule_options = pp.Literal('(').suppress() + pp.Optional(_rule_options_list). \
    setResultsName('values') + pp.Literal(')').suppress()

rule_id = pp.Literal('id:').suppress() + _rule_config_string.setResultsName(
    'value')
rule_id.setName('ID field')
rule_id.setParseAction(lambda field: field[0])

rule_head = pp.Literal('head:').suppress() + _rule_options_list. \
    setResultsName('value')
rule_head.setName('Head field')

rule_results = \
    pp.Group(pp.Literal('results_name:') +
             _rule_config_string.setResultsName('value'))
rule_results.setName('Results name field')
rule_results.setParseAction(lambda results: results[0])
rule_results.addParseAction(lambda results: results.value)

rule_terminal = \
    _rule_identifier.setResultsName('rule_type') + \
    _rule_config_string.setResultsName('rule_name') + \
    pp.Optional(rule_options).setResultsName('rule_options')
rule_terminal = rule_terminal

_rule_rules_tree_terminal = pp.OneOrMore(pp.Group(rule_terminal))
_rule_rules_tree_recursive = pp.Forward()
_rule_rules_tree_recursive << \
_rule_config_string.setResultsName('list_type') + \
pp.Literal('[').suppress() + \
pp.ZeroOrMore(
    pp.Group(_rule_rules_tree_recursive) |
    pp.Group(rule_terminal)).setResultsName('rules') + \
pp.Literal(']').suppress()
_rule_rules_tree_recursive = \
    pp.ZeroOrMore(
        pp.Group(_rule_rules_tree_recursive)) + \
    (pp.Group(_rule_rules_tree_recursive) |
     pp.ZeroOrMore(pp.Group(rule_terminal))) + \
    pp.ZeroOrMore(pp.Group(_rule_rules_tree_recursive))
rule_rules_tree = _rule_rules_tree_recursive

_rule_rules_root = \
    pp.Literal('rules:').suppress() + \
    pp.Literal('[').suppress() + \
    pp.Optional(rule_rules_tree) + \
    pp.Literal(']').suppress()

rule_config_set = \
    _rule_identifier.setResultsName('rule_type') + \
    rule_id.setResultsName('id') + \
    pp.Optional(rule_head.setResultsName('head')) + \
    pp.Optional(rule_results.setResultsName('results_name')) + \
    pp.Group(_rule_rules_root).setResultsName('rules')

rule_config_file = pp.ZeroOrMore(pp.Group(rule_config_set))
