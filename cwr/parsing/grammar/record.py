# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field

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

# Prefix fields

# Record type
record_type = pp.oneOf(data.record_types())
record_type = record_type.setName('Record Type').setResultsName('record_type')

# Transaction sequence number
transaction_seq_n = field.numeric(data.expected_record_field_size('record_prefix', 'transaction_sequence_n'))
transaction_seq_n = transaction_seq_n.setName('Transaction Sequence Number').setResultsName('transaction_sequence_n')

# Record sequence number
record_seq_n = field.numeric(data.expected_record_field_size('record_prefix', 'record_sequence_n'))
record_seq_n = record_seq_n.setName('Record Sequence Number').setResultsName('record_sequence_n')

# Trailer fields

# Group count
group_count = field.numeric(
    data.expected_record_field_size('trailer_record', 'group_count'))
group_count = group_count.setName('Group Count').setResultsName('group_count')

# Transaction count
transaction_count = field.numeric(
    data.expected_record_field_size('trailer_record', 'transaction_count'))
transaction_count = transaction_count.setName('Transaction Count').setResultsName('transaction_count')

# Record count
record_count = field.numeric(
    data.expected_record_field_size('trailer_record', 'record_count'))
record_count = record_count.setName('Record Count').setResultsName('record_count')

# Miscellany fields

# Transaction type
transaction_type = pp.oneOf(data.transaction_types())
transaction_type = transaction_type.setName('Transaction Type').setResultsName('transaction_type')

# PATTERNS

# Record prefix pattern
record_prefix = record_type + transaction_seq_n + record_seq_n
record_prefix.leaveWhitespace()