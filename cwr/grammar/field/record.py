# -*- encoding: utf-8 -*-

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


def record_type(values, compulsory=False):
    """
    Creates a record type field.

    These serve as the header field on records, identifying them.

    Usually this field can be only an specific value, but sometimes a small range of codes is allowed. This is
    specified by the 'values' parameter.

    While it is possible to set this field as optional, it is expected to be compulsory.

    :param values: allowed record type codes
    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the record type field
    """
    field = basic.lookup(values, columns=_config.field_size('table', 'record_type'),
                         compulsory=compulsory,
                         name='Record Type (one of ' + str(values) + ')')

    return field.setResultsName('record_type')


def transaction_seq_n(compulsory=False):
    """
    Creates a transaction sequence field.

    This represents the position of a transaction in a group.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the transaction sequence number field
    """
    field = basic.numeric(_config.field_size('record_prefix', 'transaction_sequence_n'), compulsory=compulsory)
    field = field.setName('Transaction Sequence Number')

    return field.setResultsName('transaction_sequence_n')


def record_seq_n(compulsory=False):
    """
    Creates a record sequence field.

    This represents the position of a record in a transaction.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the record sequence number field
    """
    field = basic.numeric(_config.field_size('record_prefix', 'record_sequence_n'), compulsory=compulsory)
    field = field.setName('Record Sequence Number')

    return field.setResultsName('record_sequence_n')


# Trailer fields


def group_count(compulsory=False):
    """
    Creates a group count field.

    This field is used on trailer records to indicate the total number of groups previous to this record.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the group count field
    """
    field = basic.numeric(
        _config.field_size('trailer_record', 'group_count'), compulsory=compulsory)
    field = field.setName('Group Count')

    return field.setResultsName('group_count')


# Transaction count
def transaction_count(compulsory=False):
    """
    Creates a transaction count field.

    This field is used on trailer records to indicate the total number of transactions previous to this record.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the transaction count field
    """
    field = basic.numeric(
        _config.field_size('trailer_record', 'transaction_count'), compulsory=compulsory)
    field = field.setName('Transaction Count')

    return field.setResultsName('transaction_count')


# Record count
def record_count(compulsory=False):
    """
    Creates a record count field.

    This field is used on trailer records to indicate the total number of records previous to this record.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the record count field
    """
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