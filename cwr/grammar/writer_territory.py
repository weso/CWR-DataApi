# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar import society
from cwr.grammar.field import table, special, record, basic
from cwr.interested_party import IPTerritoryRecord


"""
CWR Writer Territory of Control (SWT) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
General fields.
"""

# Shares Change
shares_change = basic.boolean()
shares_change = shares_change.setName('Shares Change').setResultsName('shares_change')

# Sequence #
sequence_n = basic.numeric(_config.field_size('writer_territory', 'sequence_n'))
sequence_n = sequence_n.setName('Sequence #').setResultsName('sequence_n')

"""
Patterns.
"""

territory = special.lineStart + record.record_prefix(
    _config.record_type(
        'writer_territory')) + special.ip_id() + society.pr_share() + society.mr_share() + society.sr_share() + \
            table.ie_indicator() + table.tis_code() + shares_change + sequence_n + special.lineEnd

"""
Parsing actions for the patterns.
"""

territory.setParseAction(lambda p: _to_writerterritory(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_writerterritory(parsed):
    """
    Transforms the final parsing result into an IPTerritoryRecord instance.

    :param parsed: result of parsing the Territory record
    :return: an IPTerritoryRecord created from the parsed record
    """
    return IPTerritoryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                             parsed.ip_id, parsed.ie_indicator, parsed.tis_code, parsed.sequence_n,
                             parsed.pr_share, parsed.mr_share, parsed.sr_share, parsed.shares_change)