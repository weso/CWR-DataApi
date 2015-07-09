# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

import pyparsing as pp

from cwr.grammar.factory.config import rule_at_least

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


class FieldRuleFactory(RuleFactory):
    """
    Factory for acquiring field rules.
    """

    def __init__(self, field_configs, adapters):
        super(FieldRuleFactory, self).__init__()
        # Fields already created
        self._fields = {}
        # Field adapters being used
        self._adapters = adapters
        # Configuration for creating the fields
        self._field_configs = field_configs

    def get_rule(self, field_id):
        """
        Returns the rule for the field identified by the id.

        If it is set as not being compulsory, the rule will be adapted to
        accept string composed only of white characters.

        :param field_id: unique id in the system for the field
        :return: the rule of a field
        """

        if field_id in self._fields:
            # Field already exists
            field = self._fields[field_id]
        else:
            # Field configuration info
            config = self._field_configs[field_id]

            # Field does not exist
            # It is created
            field = self._create_field(field_id, config)

            # Field is saved
            self._fields[field_id] = field

        return field

    def _create_field(self, field_id, config):
        """
        Creates the field with the specified parameters.

        :param field_id: identifier for the field
        :param config: configuration info for the field
        :return: the basic rule for the field
        """

        adapter = self._adapters[config['type']]

        if 'name' in config:
            name = config['name']
        else:
            name = None

        if 'size' in config:
            columns = config['size']
        else:
            columns = None

        if 'values' in config:
            values = config['values']
        else:
            values = None

        field = adapter.get_field(name, columns, values)

        if 'results_name' in config:
            field = field.setResultsName(config['results_name'])
        else:
            field = field.setResultsName(field_id)

        return field


class DefaultRuleFactory(RuleFactory):
    def __init__(self, record_configs, field_rule_factory,
                 optional_terminal_rule_decorator, decorators=None):
        super(DefaultRuleFactory, self).__init__()
        self._debug = False

        # Rules already created
        self._rules = {}

        # Configuration for creating the record
        self._record_configs = record_configs
        self._field_rule_factory = field_rule_factory
        self._optional_field_rule_decorator = optional_terminal_rule_decorator

        if decorators:
            self._decorators = decorators
        else:
            self._decorators = {}

    def get_rule(self, rule_id):
        if rule_id in self._rules:
            rule = self._rules[rule_id]
        else:
            rule_config = self._record_configs[rule_id]

            rule_type = rule_config.rule_type

            if rule_config.rules:
                rule = self._process_rules(rule_config.rules, pp.And)
            else:
                rule = self._build_terminal_rule(rule_config)

            if rule_type in self._decorators:
                rule = self._decorators[rule_type].decorate(rule, rule_config)

            if 'results_name' in rule_config:
                rule = rule.setResultsName(rule_config['results_name'])
            else:
                rule = rule.setResultsName(rule_id)

            rule.setName(rule_id)

            if self._debug:
                rule.setDebug()

            self._rules[rule_id] = rule

        return rule

    def _process_rules(self, rules_data, strategy):
        sequence = []

        for rule in rules_data:
            if rule.rules:
                rule = self._process_rules_group(rule)
            else:
                rule = self._build_terminal_rule(rule)

            sequence.append(rule)

        return strategy(sequence)

    def _process_rules_group(self, rules):
        group = None

        group_type = rules.list_type
        data = rules.rules

        if group_type == 'sequence':
            group = self._process_rules(data, pp.And)
        elif group_type == 'option':
            group = self._process_rules(data, pp.MatchFirst)
        elif group_type == 'optional':
            group = pp.Optional(self._process_rules(data, pp.And))

        return group

    def _build_terminal_rule(self, rule):
        rule_id = rule.rule_name
        modifiers = rule.rule_options
        rule_type = rule.rule_type

        if rule_type == 'field':
            rule = self._field_rule_factory.get_rule(rule_id)

            if self._debug:
                rule.setDebug()

            compulsory = False
            i = 0
            while not compulsory and i < len(modifiers):
                compulsory = modifiers[i] == 'compulsory'

            if not compulsory:
                rule = self._optional_field_rule_decorator.decorate(rule,
                                                                    rule_id)

            rule.setName(rule_id)
        else:
            rule = self.get_rule(rule_id)

        if modifiers and len(modifiers) > 0:
            rule = self._apply_modifiers(rule, modifiers)

        return rule

    def _apply_modifiers(self, rule, modifiers):
        for modifier in modifiers:
            if modifier == 'grouped':
                rule = pp.Group(rule)

            if modifier.startswith('at_least'):
                times = rule_at_least.parseString(modifier)[0]
                if times > 0:
                    rule_multiple = rule
                    for _ in range(1, times):
                        rule_multiple = rule_multiple + rule
                    rule = rule_multiple + pp.ZeroOrMore(rule)
                else:
                    rule = pp.Optional(pp.ZeroOrMore(rule))
            elif modifier == 'optional':
                rule = pp.Optional(rule)

        return rule
