# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special


"""
CWR Group grammar.

This stores grammar for parsing the CWR Group Header and Group Trailer.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

# Fields
record_type = pp.Literal(data.expected_record_type('group_header')).setResultsName('record_type')
group_id = special.numeric_from(data.expected_record_field_size('group_header', 'group_id'), 1).setResultsName(
    'group_id')
version_number = pp.Literal(data.expected_record_field_value('group_header', 'version_number')).setResultsName(
    'version_number')
batch_request_id = field.numeric(
    data.expected_record_field_size('group_header', 'batch_request_id')).setResultsName(
    'batch_request_id')
sd_type = field.alphanum(data.expected_record_field_size('group_header', 'sd_type')).setResultsName(
    'sd_type')

# Group Header pattern
group_header = special.lineStart + record_type + field.transaction_type + group_id + version_number + \
               batch_request_id + (sd_type | pp.empty) + special.lineEnd