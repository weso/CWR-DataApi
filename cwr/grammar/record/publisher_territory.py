# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.interested_party import IPTerritoryOfControlRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Publisher Territory of Control (SPT) grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_table_data = _config.load_field_config('table')
_common_data = _config.load_field_config('common')

_data = dict(_table_data.items() + _common_data.items())

_factory = DefaultFieldFactory(_data, CWRTables())

"""
General fields.
"""

"""
SPT patterns.
"""

territory = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('publisher_territory')) + \
            _factory.get_field('ip_n', compulsory=True) + \
            _factory.get_field('constant') + \
            _factory.get_field('pr_share_50') + \
            _factory.get_field('mr_share') + \
            _factory.get_field('sr_share') + \
            _factory.get_field('ie_indicator') + \
            _factory.get_field('tis_code') + \
            _factory.get_field('shares_change') + \
            _factory.get_field('sequence_n') + \
            field_special.lineEnd

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
    return IPTerritoryOfControlRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                      parsed.ip_n, parsed.ie_indicator, parsed.tis_code, parsed.sequence_n,
                                      parsed.pr_share, parsed.mr_share, parsed.sr_share, parsed.shares_change)