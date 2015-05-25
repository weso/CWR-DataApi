# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

import pyparsing as pp

"""
Rules factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class RuleFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_rule(self, rule_id):
        raise NotImplementedError("The get_rule method is not implemented")


class DefaultRuleFactory(RuleFactory):
    """
    Rules are a tree:

    root
        rules_list
            rule
            rule
            rule
            rules_list
                rule
                rule
        rules_list
            rule
            rule

    For example:

    group_trailer rules tree:
    rules (root)
        group_id (rule)
        transaction_count (rule)
        record_count (rule)
        optional (rules_list)
            currency_indicator (rule)
            total_monetary_value (rule)
    """

    def __init__(self, record_configs, terminal_rule_factory, optional_terminal_rule_decorator, decorators=None):
        super(DefaultRuleFactory, self).__init__()
        # Configuration for creating the record
        self._record_configs = record_configs
        self._terminal_rule_factory = terminal_rule_factory
        self._optional_terminal_rule_decorator = optional_terminal_rule_decorator

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def get_rule(self, rule_id):
        record_config = self._record_configs[rule_id]
        sequence = []

        rule_type = record_config['rule_type']
        if 'rules' in record_config:
            # Rules list
            for rules in record_config['rules']:
                sequence.append(self._process_rules_list(rules))

            record = pp.And(sequence)
        else:
            # Rule
            record = None

            if self._is_terminal(rule_type):
                pass

        if rule_type in self._decorators:
            record = self._decorators[rule_type].decorate(record, record_config)

        if 'results_name' in record_config:
            record = record.setResultsName(record_config['results_name'])
        else:
            record = record.setResultsName(rule_id)

        return record

    def _process_rules_list(self, rules):
        group = None

        group_type = rules.list_type
        data = rules.rules

        if group_type == 'sequence':
            group = self._build_from_rules_list(data, pp.And)
        elif group_type == 'option':
            group = self._build_from_rules_list(data, pp.MatchFirst)
        elif group_type == 'optional':
            group = pp.Optional(self._build_from_rules_list(data, pp.And))

        if 'modifiers' in rules:
            modifiers = rules['modifiers']
        else:
            modifiers = []

        group = self._apply_modifiers(group, modifiers)

        return group

    def _build_from_rules_list(self, rules_data, strategy):
        sequence = []

        for rule in rules_data:
            rule_type = rule.rule_type
            rule_id = rule.rule_name
            modifiers = rule.rule_options
            if not modifiers:
                modifiers = []

            if isinstance(rule_id, dict):
                rule = self._process_rules_list(rule)
            else:
                rule = self._build_rule(rule_id, rule_type, modifiers)

            sequence.append(rule)

        return strategy(sequence)

    def _build_rule(self, rule_id, rule_type, modifiers):
        if self._is_terminal(rule_type):
            rule = self._terminal_rule_factory.get_rule(rule_id)
            if 'compulsory' not in modifiers:
                rule = self._optional_terminal_rule_decorator.decorate(rule, rule_id)
        else:
            rule = self.get_rule(rule_id)

        rule = self._apply_modifiers(rule, modifiers)

        return rule

    def _is_terminal(self, rule_type):
        return rule_type == 'field'

    def _apply_modifiers(self, rule, modifiers):
        if 'grouped' in modifiers:
            rule = pp.Group(rule)

        if 'at_least_one' in modifiers:
            rule = pp.OneOrMore(rule)
        elif 'at_least_two' in modifiers:
            rule = pp.And([(rule * 2), pp.ZeroOrMore(rule)])

        if 'optional' in modifiers:
            rule = pp.Optional(rule)

        return rule
