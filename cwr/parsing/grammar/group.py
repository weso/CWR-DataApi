# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special, record
from cwr.file import GroupHeader, GroupTrailer


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
record_type_header = pp.Literal(data.expected_record_type('group_header'))
record_type_header.setName('Record Type')
record_type_header.setResultsName('record_type')

record_type_trailer = pp.Literal(data.expected_record_type('group_trailer'))
record_type_trailer.setName('Record Type')
record_type_trailer.setResultsName('record_type')

group_id = special.numeric_from(data.expected_record_field_size('group_header', 'group_id'), 1)
group_id.setName('Group ID')
group_id.setResultsName('group_id')

version_number = pp.Literal(data.expected_record_field_value('group_header', 'version_number'))
version_number.setName('Version Number')
version_number.setResultsName('version_number')

batch_request_id = field.numeric(data.expected_record_field_size('group_header', 'batch_request_id'))
batch_request_id.setName('Batch Request ID')
batch_request_id.setResultsName('batch_request_id')

sd_type = field.alphanum(data.expected_record_field_size('group_header', 'sd_type'))
sd_type.leaveWhitespace()
sd_type.setName('SD Type')
sd_type.setResultsName('sd_type')

# Unused fields

currency_indicator = pp.Word(pp.alphanums + ' ',
                             exact=data.expected_record_field_size('group_trailer', 'currency_indicator'))
currency_indicator.leaveWhitespace()
currency_indicator.setName('Currency Indicator')
currency_indicator.setResultsName('currency_indicator')

total_monetary_value = pp.Word(pp.alphanums + ' ',
                               exact=data.expected_record_field_size('group_trailer', 'total_monetary_value'))
total_monetary_value.leaveWhitespace()
total_monetary_value.setName('Total Monetary Value')
total_monetary_value.setResultsName('total_monetary_value')

# Group Header pattern
group_header = special.lineStart + record_type_header + record.transaction_type + group_id + version_number + \
               batch_request_id + (sd_type | pp.empty) + special.lineEnd

# Group Trailer pattern
group_trailer = special.lineStart + record_type_trailer + group_id + record.transaction_count + record.record_count + currency_indicator + \
                total_monetary_value + special.lineEnd

# Parsing actions
group_header.setParseAction(lambda h: _to_groupheader(h))
group_trailer.setParseAction(lambda t: _to_grouptrailer(t))


def _to_groupheader(parsed):
    """
    Transforms the final parsing result into a GroupHeader instance.

    :param parsed: result of parsing a group header
    :return: a GroupHeader created from the string
    """

    return GroupHeader(parsed.record_type, parsed.group_id, parsed.transaction_type, parsed.version_number,
                       parsed.batch_request_id)


def _to_grouptrailer(parsed):
    """
    Transforms the final parsing result into a GroupTrailer instance.

    :param parsed: result of parsing a group trailer
    :return: a GroupTrailer created from the string
    """

    return GroupTrailer(parsed.record_type, parsed.group_id, parsed.transaction_count, parsed.record_count)