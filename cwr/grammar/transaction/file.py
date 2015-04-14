# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.field import special
from cwr.group import Group
from cwr.transmission import Transmission
from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import DefaultPrefixBuilder, DefaultRecordFactory
from cwr.grammar.factory.transaction import DefaultTransactionFactory


"""
CWR file grammar.

This contains rules for the internal structure of a CWR file.

This have been created from the BNF description included in the CWR specification.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = DefaultPrefixBuilder(_config.record_types())
_factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)
_factory_transaction = DefaultTransactionFactory(_config.load_transaction_config('common'), _factory_record)

"""
Fields.
"""

group_transactions = pp.OneOrMore(
    pp.Group(_factory_transaction.get_transaction('agreement_transaction') |
             _factory_transaction.get_transaction('work_transaction') | \
             _factory_transaction.get_transaction('acknowledgement_transaction')))
group_transactions = group_transactions.setName('Group Transactions').setResultsName('transactions')

group_info = _factory_record.get_record('group_header') + \
             group_transactions + \
             _factory_record.get_record('group_trailer')

transmission_groups = pp.OneOrMore(group_info)
transmission_groups = transmission_groups.setName('Transmission Groups').setResultsName('groups')

"""
Rules.
"""

# File rule
cwr_transmission = _factory_record.get_record('transmission_header') + \
                   transmission_groups + \
                   _factory_record.get_record('transmission_trailer') + \
                   pp.ZeroOrMore(special.lineEnd)

"""
Parsing actions for the patterns.
"""

cwr_transmission.setParseAction(lambda a: _to_transmission(a))

group_info.setParseAction(lambda a: _to_group(a))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_transmission(parsed):
    """
    Transforms the final parsing result into a Transmission instance.

    :param parsed: result of parsing a Transmission
    :return: a Transmission created from the parsed record
    """
    return Transmission(parsed.transmission_header, parsed.transmission_trailer, parsed.groups)


def _to_group(parsed):
    """
    Transforms the final parsing result into a TransactionGroup instance.

    :param parsed: result of parsing a Transactions Group
    :return: a TransactionGroup created from the parsed record
    """
    return Group(parsed.group_header, parsed.group_trailer, parsed.transactions)