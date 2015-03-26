# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import AdditionalRelatedInformationDictionaryDecoder


"""
CWR Additional Related Information grammar.
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
Patterns.
"""

ari = _factory_record.get_transaction_record('ari')

"""
Parsing actions for the patterns.
"""

ari.setParseAction(lambda p: _to_ari(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_ari(parsed):
    """
    Transforms the final parsing result into an AdditionalRelatedInfoRecord instance.

    :param parsed: result of parsing an Additional Related Information record
    :return: a AdditionalRelatedInfoRecord created from the parsed record
    """
    parser = AdditionalRelatedInformationDictionaryDecoder()
    return parser.decode(parsed)