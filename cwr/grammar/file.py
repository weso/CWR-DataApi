# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import transmission, group
from cwr.grammar import transaction
from cwr.file import Transmission


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

# Transaction and group
transaction_info = pp.OneOrMore(transaction.agreement_transaction) | pp.OneOrMore(
    transaction.work_transaction) | pp.OneOrMore(transaction.acknowledgement_transaction)

group_info = group.group_header + transaction_info + group.group_trailer

_transmission_groups = pp.OneOrMore(group_info)
_transmission_groups = _transmission_groups.setName('Transmission Groups').setResultsName('transmission_groups')

"""
Rules.
"""

# File rule
cwr_transmission = transmission.transmission_header + _transmission_groups + transmission.transmission_trailer

"""
Parsing actions for the patterns.
"""

cwr_transmission.setParseAction(lambda a: _to_transmission(a))

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
    return Transmission(parsed.transmission_header, parsed.transmission_trailer, parsed.transmission_groups)