# -*- coding: utf-8 -*-

from abc import abstractmethod, ABCMeta

import pyparsing as pp

from cwr.grammar.field import record as field_record

"""
Decorators for the grammar rules.

These serve to adapt a basic set of rules for a certain type of work. For
example, for converting a group of rules into the rule for a record.

This works through the basic interface RuleDecorator, which will receive the
rule, and any required additional data, and return the adapted rule.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class RuleDecorator(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def decorate(self, rule, data):
        raise NotImplementedError("The decorate method is not implemented")


class GroupRuleDecorator(RuleDecorator):
    def __init__(self, decoders):
        super(GroupRuleDecorator, self).__init__()

        self._decoders = decoders

    def decorate(self, rule, data):
        rule_id = data['id']

        record = rule

        if rule_id in self._decoders:
            decoder = self._decoders[rule_id]
            record.setParseAction(decoder.decode)

        return record.setResultsName(rule_id)


class RecordRuleDecorator(RuleDecorator):
    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, factory, decoders):
        super(RecordRuleDecorator, self).__init__()
        self._factory = factory

        self._decoders = decoders

    def decorate(self, rule, data):
        rule_id = data['id']

        record = self._build_rule_sequence(rule, data)

        if rule_id in self._decoders:
            decoder = self._decoders[rule_id]
            record.setParseAction(decoder.decode)

        return record.setResultsName(rule_id)

    def _build_rule_sequence(self, rule, data):
        # Line start
        result = self._lineStart

        # Record prefix
        result = result + self._get_prefix(data)

        # Record rule
        result = result + rule

        # Line end
        result = result + self._lineEnd

        return result

    def _get_prefix(self, config):
        return field_record.record_type(config['head'])


class TransactionRecordRuleDecorator(RecordRuleDecorator):
    def __init__(self, factory, decoders):
        super(TransactionRecordRuleDecorator, self).__init__(factory, decoders)

    def _get_prefix(self, config):
        return field_record.record_prefix(config['head'], self._factory)


class OptionalFieldRuleDecorator(object):
    def __init__(self, field_configs, adapters):
        self._field_configs = field_configs
        self._adapters = adapters

    def decorate(self, field_base, field_id):
        # Field configuration info
        config = self._field_configs[field_id]

        # It is not compulsory, the wrapped is added
        field = self._wrap_as_optional(field_base, config['name'],
                                       config['size'])

        adapter = self._adapters[config['type']]
        if (adapter.is_numeric()):
            field = self._wrap_as_optional_numeric(field, config['name'],
                                                   config['size'])

        return field

    def _wrap_as_optional_numeric(self, field, name, columns):
        # Regular expression accepting as many whitespaces as columns
        field_empty = pp.Regex('[0]{' + str(columns) + '}')

        resultsName = field.resultsName

        field_empty.setName(name)

        # Whitespaces are not removed
        field_empty.leaveWhitespace()

        # None is returned by this rule
        field_empty.setParseAction(pp.replaceWith(None))

        field_empty = field_empty.setResultsName(field.resultsName)

        field = field | field_empty

        field.setName(name)
        field = field.setResultsName(resultsName)

        field.leaveWhitespace()

        return field

    def _wrap_as_optional(self, field, name, columns):
        """
        Adds a wrapper rule to the field to accept empty strings.

        This empty string should be of the same size as the columns parameter.
        One smaller or bigger will be rejected.

        This wrapper will return None if the field is empty.

        :param field: the field to wrap
        :param name: name of the field
        :param columns: number of columns it takes
        :return: the field with an additional rule to allow empty strings
        """
        # Regular expression accepting as many whitespaces as columns
        field_empty = pp.Regex('[ ]{' + str(columns) + '}')

        resultsName = field.resultsName

        field_empty.setName(name)

        # Whitespaces are not removed
        field_empty.leaveWhitespace()

        # None is returned by this rule
        field_empty.setParseAction(pp.replaceWith(None))

        field_empty = field_empty.setResultsName(resultsName)

        field = field | field_empty

        field.setName(name)
        field = field.setResultsName(resultsName)

        field.leaveWhitespace()

        return field
