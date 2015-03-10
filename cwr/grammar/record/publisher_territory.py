# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table, society
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import publisher_territory as field_territory
from cwr.interested_party import IPTerritoryRecord


"""
CWR Publisher Territory of Control (SPT) grammar.
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

"""
SPT patterns.
"""

territory = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'publisher_territory'), compulsory=True) + field_special.ip_id(compulsory=True) + field_territory.constant + \
            society.pr_share(maximum=50) + society.mr_share() + society.sr_share() + \
            field_table.ie_indicator() + field_table.tis_code() + field_territory.shares_change + field_territory.sequence_n + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

territory.setParseAction(lambda p: _to_publisherterritory(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_publisherterritory(parsed):
    """
    Transforms the final parsing result into an IPTerritoryRecord instance.

    :param parsed: result of parsing the Territory record
    :return: an IPTerritoryRecord created from the parsed record
    """
    return IPTerritoryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                             parsed.ip_id, parsed.ie_indicator, parsed.tis_code, parsed.sequence_n,
                             parsed.pr_share, parsed.mr_share, parsed.sr_share, parsed.shares_change)