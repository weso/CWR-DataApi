# -*- coding: utf-8 -*-

import pyparsing as pp


"""
Classes for handling the configuration files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

_rule_config_string = pp.Regex('[^()\[\]\\n,:]*')
_rule_config_string.setParseAction(lambda s: _clear_str(s))


def _clear_str(str):
    return str[0].strip()


_line_end = pp.LineEnd()
_line_end.suppress()

_rule_identifier = _rule_config_string + pp.Literal(':').suppress()
_rule_identifier.setParseAction(lambda id: id[0])

_rule_options_list = pp.delimitedList(_rule_config_string)
rule_options = pp.Literal('(').suppress() + pp.Optional(_rule_options_list).setResultsName('values') + pp.Literal(
    ')').suppress()

rule_id = pp.Group(pp.Literal('id:') + _rule_config_string.setResultsName('value'))
rule_id.setName('ID field')
rule_id.setParseAction(lambda id: id[0])
rule_id.addParseAction(lambda id: id.value)

rule_head = pp.Group(pp.Literal('head:') + _rule_config_string.setResultsName('value'))
rule_head.setName('Head field')
rule_head.setParseAction(lambda id: id[0])
rule_head.addParseAction(lambda id: id.value)

rule_results = pp.Group(pp.Literal('results_name:') + _rule_config_string.setResultsName('value'))
rule_results.setName('Results name field')
rule_results.setParseAction(lambda id: id[0])
rule_results.addParseAction(lambda id: id.value)

rule_terminal = _rule_identifier.setResultsName('rule_type') + \
                _rule_config_string.setResultsName('rule_name') + \
                pp.Optional(rule_options).setResultsName('rule_options')

rule_rules_list = _rule_identifier.setResultsName('list_type') + \
                  pp.Literal('[').suppress() + \
                  pp.ZeroOrMore(pp.Group(rule_terminal)).setResultsName('rules') + \
                  pp.Literal(']').suppress()

rule_rules_list_group = _rule_identifier.setResultsName('list_type') + \
                        pp.Literal('[').suppress() + \
                        pp.ZeroOrMore(pp.Group(rule_rules_list)).setResultsName('rules') + \
                        pp.Literal(']').suppress()

rule_rules_tree = pp.Forward()
_rule_rules_tree_part = _rule_identifier.setResultsName('list_type') + \
                        pp.Literal('[').suppress() + \
                        pp.ZeroOrMore(pp.Group(rule_rules_tree)).setResultsName('rules') + \
                        pp.Literal(']').suppress()
rule_rules_tree << (rule_rules_list | _rule_rules_tree_part | pp.Group(rule_terminal).setResultsName('rules'))
rule_rules_tree = pp.OneOrMore(rule_rules_tree)

_rule_rules_root = pp.Literal('rules:').suppress() + \
                   pp.Literal('[').suppress() + \
                   pp.Group(rule_rules_tree).setResultsName('rules') + \
                   pp.Literal(']').suppress()
_rule_rules_root.setParseAction(lambda r: r[0].rules)

rule_config_set = _rule_identifier.setResultsName('rule_type') + \
                  rule_id.setResultsName('id') + \
                  pp.Optional(rule_head.setResultsName('head')) + \
                  pp.Optional(rule_results.setResultsName('results_name')) + \
                  _rule_rules_root.setResultsName('rules')

rule_config_file = pp.ZeroOrMore(pp.Group(rule_config_set))