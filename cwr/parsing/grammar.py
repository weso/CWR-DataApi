# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data import __data__ as data


"""
Grammar for CWR files.

This is used along with pyparsing to create a BNF grammar.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Fields
record_type = pp.oneOf(data.record_types()).setResultsName("record_type")
transaction_n = pp.Word(pp.nums, exact=8).setResultsName("transaction_sequence_n")
sequence_n = pp.Word(pp.nums, exact=8).setResultsName("record_sequence_n")

# Patterns
record_prefix = record_type + transaction_n + sequence_n


