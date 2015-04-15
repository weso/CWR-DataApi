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
    def get_rule(self, id, modifiers):
        raise NotImplementedError("The get_rule method is not implemented")

    @abstractmethod
    def is_terminal(self, type):
        raise NotImplementedError("The is_terminal method is not implemented")


class GroupRuleFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_rule_group(self, groups):
        raise NotImplementedError("The get_rule_group method is not implemented")


class DefaultGroupRuleFactory(GroupRuleFactory):
    def __init__(self, record_configs, terminal_rule_factory, decorators=None):
        super(DefaultGroupRuleFactory, self).__init__()
        # Configuration for creating the record
        self._record_configs = record_configs
        self._terminal_rule_factory = terminal_rule_factory

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def get_rule(self, id):
        record_config = self._record_configs[id]

        return self.get_rule_group(record_config)

    def get_rule_group(self, rules_data):
        record = None

        for rules in rules_data['rules']:
            group = self._get_group(rules)

            if record is None:
                record = group
            else:
                record = pp.And([record, group])

        if 'rule_type' in rules_data:
            rule_type = rules_data['rule_type']
            if rule_type in self._decorators:
                record = self._decorators[rule_type].decorate(record, rules_data)

        return record

    def _get_group(self, rules):
        group = None

        if rules['group_type'] == 'sequence':
            group = self._get_sequence(rules)
        elif rules['group_type'] == 'option':
            group = self._get_option(rules)

        return group

    def _get_sequence(self, group):
        sequence = []

        for rule_data in group['rules']:
            if 'modifiers' in rule_data:
                modifiers = rule_data['modifiers']
            else:
                modifiers = []

            rule_type = rule_data['rule_type']

            if self._terminal_rule_factory.is_terminal(rule_type):
                rule = self._terminal_rule_factory.get_rule(rule_data['id'], modifiers)
            else:
                rule = self.get_rule(rule_data['id'])

            if 'at_least_one' in modifiers:
                rule = pp.OneOrMore(rule)
            elif 'at_least_two' in modifiers:
                rule = pp.And([(rule * 2), pp.ZeroOrMore(rule)])

            if 'optional' in modifiers:
                rule = pp.Optional(rule)

            sequence.append(rule)

        return pp.And(sequence)

    def _get_option(self, group):
        options = None

        for group_data in group['rules']:
            group = self._get_group(group_data)

            if options is None:
                options = group
            else:
                options = pp.MatchFirst([options, group])

        return options


class RuleDecorator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def decorate(self, rule, data):
        raise NotImplementedError("The decorate method is not implemented")