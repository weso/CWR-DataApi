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


class GroupRuleFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_rule_group(self, groups):
        raise NotImplementedError("The get_rule_group method is not implemented")


class DefaultGroupRuleFactory(GroupRuleFactory):
    def __init__(self, rule_factories, decorators=None):
        super(DefaultGroupRuleFactory, self).__init__()
        self.rule_factories = rule_factories

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def get_rule_group(self, groups):
        record = None

        for group_data in groups:
            group = self._get_group(group_data)

            if record is None:
                record = group
            else:
                record = pp.And([record, group])

        return record

    def _get_group(self, group_data):
        group = None

        if group_data['group_type'] == 'sequence':
            group = self._get_sequence(group_data)
        elif group_data['group_type'] == 'option':
            group = self._get_option(group_data)

        return group

    def _get_sequence(self, group):
        sequence = []

        for rule_data in group['rules']:
            if 'modifiers' in rule_data:
                modifiers = rule_data['modifiers']
            else:
                modifiers = []

            rule = self.rule_factories[rule_data['rule_type']].get_rule(rule_data['id'], modifiers)

            if self._decorators and id in self._decorators:
                rule = self._decorators[id].decorate(rule)

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
    def decorate(self, id, rule):
        raise NotImplementedError("The decorate method is not implemented")