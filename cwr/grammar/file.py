# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import transmission, group
from cwr.grammar import transaction


"""
CWR file grammar.

This contains rules for the internal structure of a CWR file.

This have been created from the BNF description included in the CWR specification.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Transaction and group
transaction_info = transaction.agreement_transaction | transaction.work_transaction | transaction.acknowledgement_transaction

group_info = group.group_header + pp.OneOrMore(transaction_info) + group.group_trailer

# File rule
cwr_file = transmission.transmission_header + pp.OneOrMore(group_info) + transmission.transmission_trailer