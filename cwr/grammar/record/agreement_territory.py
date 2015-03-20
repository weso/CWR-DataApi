# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, record
from cwr.agreement import AgreementTerritoryRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Territory in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = DefaultFieldFactory(_config.load_field_config('table'), CWRTables())

"""
Territory in Agreement patterns.
"""

territory_in_agreement = special.lineStart + record.record_prefix(
    _config.record_type('agreement_territory'), compulsory=True) + _lookup_factory.get_field('ie_indicator') + \
                         _lookup_factory.get_field('tis_code') + special.lineEnd

"""
Parsing actions for the patterns.
"""

territory_in_agreement.setParseAction(lambda p: _to_agreementterritory(p))

"""
Parsing actions for the patterns.
"""


def _to_agreementterritory(parsed):
    """
    Transforms the final parsing result into a AgreementTerritoryRecord instance.

    :param parsed: result of parsing a Territory in Agreement transaction header
    :return: a AgreementTerritoryRecord created from the parsed record
    """
    return AgreementTerritoryRecord(record_type=parsed.record_type,
                                    transaction_sequence_n=parsed.transaction_sequence_n,
                                    record_sequence_n=parsed.record_sequence_n,
                                    tis_numeric_code=parsed.tis_code,
                                    inclusion_exclusion_indicator=parsed.ie_indicator)