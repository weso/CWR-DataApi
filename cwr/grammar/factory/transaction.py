# -*- coding: utf-8 -*-

from abc import ABCMeta

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

    def get_transaction(self, id):
        pass


class DefaultTransactionFactory(TransactionFactory):
    """
    Factory for acquiring record rules.
    """

    def __init__(self, transaction_configs, record_factory):
        super(DefaultTransactionFactory, self).__init__()
        self._record_factory = record_factory
        self._transaction_configs = transaction_configs

    def get_transaction(self, id):
        transaction_config = self._transaction_configs[id]
        transaction = None

        for group_data in transaction_config:

            if 'record' in group_data:
                entry = self._record_factory.get_record(group_data['record'])
            elif 'transaction' in group_data:
                entry = self.get_transaction(group_data['transaction'])

            # TODO: Use a class to handle these rules
            if 'at_least_one' in group_data and group_data['at_least_one']:
                entry = pp.OneOrMore(entry)

            if 'at_least_two' in group_data and group_data['at_least_two']:
                entry = (entry * 2) + pp.ZeroOrMore(entry)

            if 'optional' in group_data and group_data['optional']:
                entry = pp.Optional(entry)

            if not transaction:
                transaction = entry
            else:
                transaction = transaction + entry

        return transaction