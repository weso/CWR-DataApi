# -*- coding: utf-8 -*-

from abc import abstractmethod

import pyparsing as pp

from cwr.grammar.field import record as field_record
from cwr.parser.decoder.dictionary import *


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


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
        id = data['id']

        record = rule

        if id in self._decoders:
            decoder = self._decoders[id]
            record.setParseAction(lambda p: decoder.decode(p))

        return record.setResultsName(id)


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
        sequence = []

        id = data['id']

        sequence.append(self._lineStart)

        prefix = self._get_prefix(data)

        if prefix is not None:
            sequence.append(prefix)

        sequence.append(rule)

        sequence.append(self._lineEnd)

        record = pp.And(sequence)

        if id in self._decoders:
            decoder = self._decoders[id]
            record.setParseAction(lambda p: decoder.decode(p))

        return record.setResultsName(id)

    def _get_prefix(self, config):
        rule_type = config['rule_type']

        if rule_type == 'transaction':
            header = field_record.record_prefix(config['record_type'], self._factory)
        elif rule_type == 'record':
            header = field_record.record_type(config['record_type'])
        else:
            header = None

        return header
