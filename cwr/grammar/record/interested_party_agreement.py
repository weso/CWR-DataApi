# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import InterestedPartyForAgreementDecoder


"""
CWR Interested Party in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
IPA patterns.
"""

interested_party_agreement = _factory_record.get_transaction_record('interested_party_agreement')

"""
Parsing actions for the patterns.
"""

interested_party_agreement.setParseAction(lambda p: _to_interested_party_agreement(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_interested_party_agreement(parsed):
    """
    Transforms the final parsing result into an AgreementInterestedParty instance.

    :param parsed: result of parsing an IPA record
    :return: an AgreementInterestedParty created from the parsed record
    """
    parser = InterestedPartyForAgreementDecoder()
    return parser.decode(parsed)