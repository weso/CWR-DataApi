# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from cwr.grammar.factory.rule import DefaultGroupRuleFactory, RuleFactory

import pyparsing as pp


"""
Transactions factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TransactionFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_transaction(self, id):
        raise NotImplementedError("The get_transaction method is not implemented")


class DefaultTransactionFactory(TransactionFactory, RuleFactory):
    """
    Factory for acquiring record rules.
    """

    def __init__(self, transaction_configs, record_factory):
        super(DefaultTransactionFactory, self).__init__()
        self._record_factory = record_factory
        self._transaction_configs = transaction_configs

        factories = {'record': record_factory, 'transaction': self}
        # TODO: This should not be stored inside this factory
        self._group_rule_factory = DefaultGroupRuleFactory(factories)

    def get_transaction(self, id):
        transaction_config = self._transaction_configs[id]
        transactions = self._group_rule_factory.get_rule_group(transaction_config)

        return transactions

    def get_rule(self, id, modifiers):
        return self.get_transaction(id)