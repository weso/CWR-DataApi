# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special, record
from cwr.group import GroupHeader, GroupTrailer


"""
CWR Group grammar.

This stores grammar for parsing the CWR Group Header and Group Trailer.

The Group Header contains the following fields:
- Record Type.
- Transaction Type.
- Group ID.
- Version Number.
- Batch Request ID.

Additionally, it contains the following unused fields, which can be safely ignored:
- SD Type.

The Group Trailer contains the following fields:
- Record Type.
- Group ID.
- Transaction Count.
- Record Count.

Additionally, it contains the following unused fields, which can be safely ignored:
- Currency Indicator.
- Total Monetary Value.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

"""
Group fields.

These fields are:
- Record Type. One for the header and another for the trailer, both a pre-defined string.
- Group ID. Numeric.
- Version Number. Must be a predefined string.
- Batch Request ID. Numeric.
"""

# Record Type for the header
record_type_header = pp.Literal(data.record_type('group_header'))
record_type_header = record_type_header.setName('Record Type').setResultsName('record_type')

# Record Type for the trailer
record_type_trailer = pp.Literal(data.record_type('group_trailer'))
record_type_trailer = record_type_trailer.setName('Record Type').setResultsName('record_type')

# Group ID
group_id = special.numeric_from(data.field_size('group_header', 'group_id'), 1)
group_id = group_id.setName('Group ID').setResultsName('group_id')

# Version Number
version_number = pp.Literal(data.field_value('group_header', 'version_number'))
version_number = version_number.setName('Version Number').setResultsName('version_number')

# Batch Request ID
batch_request_id = field.numeric(data.field_size('group_header', 'batch_request_id'))
batch_request_id = batch_request_id.setName('Batch Request ID').setResultsName('batch_request_id')

"""
Unused fields.

These are fields which exist in the standard but are unused and ignored.

They are:
- SD Type
- Currency Indicator
- Total Monetary Value
"""

# SD Type
sd_type = field.alphanum(data.field_size('group_header', 'sd_type'))
sd_type.leaveWhitespace()
sd_type = sd_type.setName('SD Type').setResultsName('sd_type')

# Currency Indicator
currency_indicator = pp.Word(pp.alphanums + ' ',
                             exact=data.field_size('group_trailer', 'currency_indicator'))
currency_indicator.leaveWhitespace()
currency_indicator = currency_indicator.setName('Currency Indicator').setResultsName('currency_indicator')

# Total Monetary Value
total_monetary_value = pp.Word(pp.alphanums + ' ',
                               exact=data.field_size('group_trailer', 'total_monetary_value'))
total_monetary_value.leaveWhitespace()
total_monetary_value = total_monetary_value.setName('Total Monetary Value').setResultsName('total_monetary_value')

"""
Group patterns.

These are the grammatical structures for the Group Header and Group Trailer.
"""

# Group Header pattern
group_header = special.lineStart + record_type_header + record.transaction_type + group_id + version_number + \
               batch_request_id + (sd_type | pp.empty) + special.lineEnd

# Group Trailer pattern
group_trailer = special.lineStart + record_type_trailer + group_id + record.transaction_count + record.record_count + \
                currency_indicator + total_monetary_value + special.lineEnd

"""
Parsing actions for the patterns.

The header will be parsed into a GroupHeader and the trailer into a GroupTrailer.
"""

group_header.setParseAction(lambda h: _to_groupheader(h))
group_trailer.setParseAction(lambda t: _to_grouptrailer(t))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


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