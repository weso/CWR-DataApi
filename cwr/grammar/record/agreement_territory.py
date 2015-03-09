# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table, special, record
from cwr.agreement import AgreementTerritoryRecord


"""
CWR Territory in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Territory in Agreement patterns.
"""

territory_in_agreement = special.lineStart + record.record_prefix(
    _config.record_type('agreement_territory'), compulsory=True) + table.ie_indicator(True) + table.tis_code(
    compulsory=True) + special.lineEnd

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
    return AgreementTerritoryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                    parsed.tis_code, parsed.ie_indicator)