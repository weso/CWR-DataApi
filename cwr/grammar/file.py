# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import transmission, group
from cwr.grammar import transaction
from cwr.file import Transmission, TransactionGroup


"""
CWR file grammar.

This contains rules for the internal structure of a CWR file.

This have been created from the BNF description included in the CWR specification.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

"""
Fields.
"""

group_transactions = pp.OneOrMore(
    pp.Group(transaction.agreement_transaction | transaction.work_transaction | \
             transaction.acknowledgement_transaction))
group_transactions = group_transactions.setName('Group Transactions').setResultsName('transactions')

group_info = group.group_header + group_transactions + group.group_trailer

_transmission_groups = pp.OneOrMore(group_info)
_transmission_groups = _transmission_groups.setName('Transmission Groups').setResultsName('groups')

"""
Rules.
"""

# File rule
cwr_transmission = transmission.transmission_header + _transmission_groups + transmission.transmission_trailer + pp.ZeroOrMore(
    pp.lineEnd().suppress()).suppress()

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
    return TransactionGroup(parsed.group_header, parsed.group_trailer, parsed.transactions)