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
def record_type(values):
    field = pp.oneOf(values)
    field = field.setName('Record Type (one of ' + str(values) + ')')

    return field.setResultsName('record_type')

# Transaction sequence number
transaction_seq_n = basic.numeric(_config.field_size('record_prefix', 'transaction_sequence_n'))
transaction_seq_n = transaction_seq_n.setName('Transaction Sequence Number').setResultsName('transaction_sequence_n')

# Record sequence number
record_seq_n = basic.numeric(_config.field_size('record_prefix', 'record_sequence_n'))
record_seq_n = record_seq_n.setName('Record Sequence Number').setResultsName('record_sequence_n')

# Trailer fields

# Group count
group_count = basic.numeric(
    _config.field_size('trailer_record', 'group_count'), compulsory=True)
group_count = group_count.setName('Group Count').setResultsName('group_count')

# Transaction count
transaction_count = basic.numeric(
    _config.field_size('trailer_record', 'transaction_count'), compulsory=True)
transaction_count = transaction_count.setName('Transaction Count').setResultsName('transaction_count')

# Record count
record_count = basic.numeric(
    _config.field_size('trailer_record', 'record_count'), compulsory=True)
record_count = record_count.setName('Record Count').setResultsName('record_count')

# PATTERNS


# Record prefix pattern
def record_prefix(required_type):
    """
    Creates a record prefix for the specified record type.

    :param required_type: the type of the record using this prefix
    :return: the record prefix
    """
    field = record_type(required_type) + transaction_seq_n + record_seq_n
    field.leaveWhitespace()

    return field