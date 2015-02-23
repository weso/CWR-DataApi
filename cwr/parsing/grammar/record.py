# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special
from cwr.file import TransactionRecord

"""
Grammar for Records.

This stores general records fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

# RECORD FIELDS

transaction_n = field.numeric(
    data.expected_record_field_size('record_prefix', 'transaction_sequence_n')).setResultsName(
    "transaction_sequence_n")
sequence_n = field.numeric(data.expected_record_field_size('record_prefix', 'record_sequence_n')).setResultsName(
    "record_sequence_n")
record_type = pp.oneOf(data.record_types()).setName('Record Type').setResultsName('record_type')
transaction_type = pp.oneOf(data.transaction_types()).setResultsName('transaction_type')


# Record prefix pattern
record_prefix = special.lineStart + record_type + transaction_n + sequence_n + special.lineEnd

# Parsing actions
record_prefix.setParseAction(lambda p: _to_recordprefix(p))


def _to_recordprefix(parsed):
    """
    Transforms the final parsing result into a TransactionRecord instance.

    :param parsed: result of parsing a record prefix
    :return: a TransactionRecord created from the record prefix
    """
    return TransactionRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n)