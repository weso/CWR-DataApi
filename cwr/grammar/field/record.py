# -*- coding: utf-8 -*-

from config_cwr.accessor import CWRConfiguration
from cwr.grammar.field import basic

"""
Grammar for Records.

This stores general records fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# RECORD FIELDS

# Prefix fields


def record_type(values):
    """
    Creates a record type field.

    These serve as the header field on records, identifying them.

    Usually this field can be only an specific value, but sometimes a small range of codes is allowed. This is
    specified by the 'values' parameter.

    While it is possible to set this field as optional, it is expected to be compulsory.

    :param values: allowed record type codes
    :return: grammar for the record type field
    """
    field = basic.lookup(values, name='Record Type (one of ' + str(values) + ')')

    return field.setResultsName('record_type')


# Record prefix
def record_prefix(required_type, factory):
    """
    Creates a record prefix for the specified record type.

    :param required_type: the type of the record using this prefix
    :param factory: field factory
    :return: the record prefix
    """
    field = record_type(required_type)
    field += factory.get_rule('transaction_sequence_n')
    field += factory.get_rule('record_sequence_n')

    # field.leaveWhitespace()

    return field