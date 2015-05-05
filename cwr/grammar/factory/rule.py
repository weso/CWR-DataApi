# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

import pyparsing as pp


"""
Rules factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TerminalRuleFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_rule(self, id, modifiers):
        raise NotImplementedError("The get_rule method is not implemented")

    @abstractmethod
    def is_terminal(self, type):
        raise NotImplementedError("The is_terminal method is not implemented")


class RuleFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self, logger=None):
        # Logger
        self._logger = logger

    @abstractmethod
    def get_rule(self, groups):
        raise NotImplementedError("The get_rule method is not implemented")


class DefaultRuleFactory(RuleFactory):
    def __init__(self, record_configs, terminal_rule_factory, decorators=None):
        super(DefaultRuleFactory, self).__init__()
        # Configuration for creating the record
        self._record_configs = record_configs
        self._terminal_rule_factory = terminal_rule_factory

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def get_rule(self, id):
        if self._logger:
            self._logger.info('Acquiring rule %s' % id)

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

    def _get_group(self, rules):
        group = None

        if rules['group_type'] == 'sequence':
            group = self._build_group(rules, pp.And)
        elif rules['group_type'] == 'option':
            group = self._build_group(rules, pp.MatchFirst)
        elif rules['group_type'] == 'optional':
            group = pp.Optional(self._build_group(rules, pp.And))

        if 'modifiers' in rules:
            modifiers = rules['modifiers']
        else:
            modifiers = []

        group = self._apply_modifiers(group, modifiers)

        return group

    def _build_group(self, group, strategy):
        sequence = []

        for rule_data in group['rules']:
            if 'modifiers' in rule_data:
                modifiers = rule_data['modifiers']
            else:
                modifiers = []

            rule = self._build_rule(rule_data, modifiers)

            rule = self._apply_modifiers(rule, modifiers)

            sequence.append(rule)

        return strategy(sequence)

    def _build_rule(self, rule_data, modifiers):
        if 'rule_type' in rule_data:
            rule_type = rule_data['rule_type']

            if self._terminal_rule_factory.is_terminal(rule_type):
                rule = self._terminal_rule_factory.get_rule(rule_data['id'], modifiers)
            else:
                rule = self.get_rule(rule_data['id'])
        else:
            rule = self._get_group(rule_data)

        return rule

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


class RuleDecorator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def decorate(self, rule, data):
        raise NotImplementedError("The decorate method is not implemented")