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
            record = self._record_factory.get_record(group_data['record'])

            if 'at_least_one' in group_data and group_data['at_least_one']:
                record = pp.OneOrMore(record)

            if 'optional' in group_data and group_data['optional']:
                record = pp.Optional(record)

            if not transaction:
                transaction = record
            else:
                transaction = transaction + record

        return transaction