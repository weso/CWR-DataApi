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

transaction_seq_n = field.numeric(
    data.expected_record_field_size('record_prefix', 'transaction_sequence_n')).setName(
    "Transaction Sequence Number").setResultsName(
    "transaction_sequence_n")
record_seq_n = field.numeric(data.expected_record_field_size('record_prefix', 'record_sequence_n')).setName(
    "Record Sequence Number").setResultsName(
    "record_sequence_n")

transaction_count = field.numeric(
    data.expected_record_field_size('trailer_record', 'transaction_count')).setName("Transaction Count").setResultsName(
    "transaction_count")
record_count = field.numeric(
    data.expected_record_field_size('trailer_record', 'record_count')).setName("Record Count").setResultsName(
    "record_count")

record_type = pp.oneOf(data.record_types()).setName('Record Type').setResultsName('record_type')
transaction_type = pp.oneOf(data.transaction_types()).setName("Transaction Type").setResultsName('transaction_type')


# Record prefix pattern
record_prefix = special.lineStart + record_type + transaction_seq_n + record_seq_n + special.lineEnd

# Parsing actions
record_prefix.setParseAction(lambda p: _to_recordprefix(p))


def _to_recordprefix(parsed):
    """
    Transforms the final parsing result into a TransactionRecord instance.

    :param parsed: result of parsing a record prefix
    :return: a TransactionRecord created from the record prefix
    """
    return TransactionRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n)