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

    def __init__(self, record_configs, terminal_rule_factory, decorators=None):
        super(DefaultRuleFactory, self).__init__()
        # Configuration for creating the record
        self._record_configs = self._process_rules(record_configs)
        self._terminal_rule_factory = terminal_rule_factory

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def _process_rules(self, rules):
        processed = {}

        for rule in rules:
            data = list(rule.values())[0]
            data['rule_type'] = list(rule.keys())[0]

            id = data['id']

            processed[id] = data

        return processed

    def get_rule(self, id):

        record_config = self._record_configs[id]
        sequence = []

        for rules in record_config['rules']:
            sequence.append(self._get_group(rules))

        record = pp.And(sequence)

        if 'rule_type' in record_config:
            rule_type = record_config['rule_type']
            if rule_type in self._decorators:
                record = self._decorators[rule_type].decorate(record, record_config)

        if 'results_name' in record_config:
            record = record.setResultsName(record_config['results_name'])
        else:
            record = record.setResultsName(id)

        return record

    def _get_group(self, rules, joiner=None):
        group = None

        group_type = list(rules.keys())[0]
        data = list(rules.values())[0]

        if group_type == 'sequence':
            group = self._build_group(data, pp.And)
        elif group_type == 'option':
            group = self._build_group(data, pp.MatchFirst)
        elif group_type == 'optional':
            group = pp.Optional(self._build_group(data, pp.And))

        if 'modifiers' in rules:
            modifiers = rules['modifiers']
        else:
            modifiers = []

        group = self._apply_modifiers(group, modifiers)

        return group

    def _build_group(self, rules_data, strategy):
        sequence = []

        for rule in rules_data:
            rule_type = list(rule.keys())[0]
            rule_values = list(rule.values())[0]
            if isinstance(rule_values, list):
                modifiers = rule_values[1:]
                rule_id = rule_values[0]
            else:
                modifiers = []
                rule_id = rule_values

            data_rule = {}
            if isinstance(rule_id, dict):
                data_rule = rule
            else:
                data_rule['id'] = rule_id
                data_rule['rule_type'] = rule_type

            rule = self._build_rule(data_rule, modifiers)

            rule = self._apply_modifiers(rule, modifiers)

            sequence.append(rule)

        return strategy(sequence)

    def _build_rule(self, rule_data, modifiers):
        if 'rule_type' in rule_data:
            rule_type = rule_data['rule_type']

            if self._is_terminal(rule_type):
                compulsory = 'compulsory' in modifiers

                rule = self._terminal_rule_factory.get_rule(rule_data['id'], compulsory)
            else:
                rule = self.get_rule(rule_data['id'])
        else:
            rule = self._get_group(rule_data)

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