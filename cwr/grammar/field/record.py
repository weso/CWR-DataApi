# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic
from cwr.grammar.factory.field import DefaultFieldFactory

"""
Grammar for Records.

This stores general records fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_record_factory = DefaultFieldFactory(_config.load_field_config('record'))

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
    field = basic.lookup(values, columns=_config.field_size('record', 'record_type'),
                         compulsory=compulsory,
                         name='Record Type (one of ' + str(values) + ')')

    return field.setResultsName('record_type')


# Record prefix
def record_prefix(required_type, compulsory=False):
    """
    Creates a record prefix for the specified record type.

    :param required_type: the type of the record using this prefix
    :return: the record prefix
    """
    field = record_type(required_type, compulsory=compulsory) + \
            _record_factory.get_field('transaction_sequence_n', compulsory=compulsory) + \
            _record_factory.get_field('record_sequence_n', compulsory=compulsory)
    field.leaveWhitespace()

    return field