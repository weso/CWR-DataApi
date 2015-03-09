# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.group import GroupHeader, GroupTrailer
from cwr.grammar.field import group as field_group
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record


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

# Acquires data sources
_config = CWRConfiguration()

"""
Group patterns.

These are the grammatical structures for the Group Header and Group Trailer.
"""

# Group Header pattern
group_header = field_special.lineStart + field_record.record_type(
    _config.record_type('group_header'), compulsory=True) + field_table.transaction_type(
    True) + field_group.group_id + field_group.version_number + \
               field_group.batch_request_id + field_group.sd_type + field_special.lineEnd
group_header = group_header.setName('Group Header').setResultsName('group_header')

# Group Trailer pattern
group_trailer = field_special.lineStart + field_record.record_type(
    _config.record_type('group_trailer'), compulsory=True) + field_group.group_id + field_record.transaction_count(
    compulsory=True) + field_record.record_count(compulsory=True) + \
                field_group.currency_indicator + field_group.total_monetary_value + field_special.lineEnd
group_trailer = group_trailer.setName('Group Trailer').setResultsName('group_trailer')

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
    :return: a GroupHeader created from the parsed record
    """
    return GroupHeader(parsed.record_type, parsed.group_id, parsed.transaction_type, parsed.version_number,
                       parsed.batch_request_id)


def _to_grouptrailer(parsed):
    """
    Transforms the final parsing result into a GroupTrailer instance.

    :param parsed: result of parsing a group trailer
    :return: a GroupTrailer created from the parsed record
    """

    return GroupTrailer(parsed.record_type, parsed.group_id, parsed.transaction_count, parsed.record_count)