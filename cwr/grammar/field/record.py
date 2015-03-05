# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic

"""
Grammar for Records.

This stores general records fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# RECORD FIELDS

# Prefix fields


# Record type
def record_type(values, compulsory=False):
    field = pp.oneOf(values)
    field = field.setName('Record Type (one of ' + str(values) + ')')

    return field.setResultsName('record_type')


# Transaction sequence number
def transaction_seq_n(compulsory=False):
    field = basic.numeric(_config.field_size('record_prefix', 'transaction_sequence_n'), compulsory=compulsory)
    field = field.setName('Transaction Sequence Number')

    return field.setResultsName('transaction_sequence_n')


# Record sequence number
def record_seq_n(compulsory=False):
    field = basic.numeric(_config.field_size('record_prefix', 'record_sequence_n'), compulsory=compulsory)
    field = field.setName('Record Sequence Number')

    return field.setResultsName('record_sequence_n')


# Trailer fields


# Group count
def group_count(compulsory=False):
    field = basic.numeric(
        _config.field_size('trailer_record', 'group_count'), compulsory=compulsory)
    field = field.setName('Group Count')

    return field.setResultsName('group_count')


# Transaction count
def transaction_count(compulsory=False):
    field = basic.numeric(
        _config.field_size('trailer_record', 'transaction_count'), compulsory=compulsory)
    field = field.setName('Transaction Count')

    return field.setResultsName('transaction_count')


# Record count
def record_count(compulsory=False):
    field = basic.numeric(
        _config.field_size('trailer_record', 'record_count'), compulsory=compulsory)
    field = field.setName('Record Count')

    return field.setResultsName('record_count')


# Record prefix
def record_prefix(required_type, compulsory=False):
    """
    Creates a record prefix for the specified record type.

    :param required_type: the type of the record using this prefix
    :return: the record prefix
    """
    field = record_type(required_type, compulsory=compulsory) + transaction_seq_n(compulsory=compulsory) + record_seq_n(
        compulsory=compulsory)
    field.leaveWhitespace()

    return field