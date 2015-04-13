# -*- coding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration

from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, DefaultRecordFactory
from cwr.grammar.factory.transaction import DefaultTransactionFactory


"""
CWR interested party grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = DefaultRecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)
_factory_transaction = DefaultTransactionFactory(_config.load_transaction_config('common'), _factory_record)

# Controlled publisher
controlled_publisher_information = _factory_transaction.get_transaction('original_publisher_information') + \
                                   pp.Optional(pp.OneOrMore(
                                       _factory_transaction.get_transaction('administrator_information'))) + \
                                   pp.Optional(
                                       pp.OneOrMore(_factory_transaction.get_transaction('subpublisher_information'))) + \
                                   pp.Optional(pp.OneOrMore(_factory_record.get_record('publisher')))

# Territory
territory_information = pp.OneOrMore(_factory_record.get_record('territory_in_agreement')) + \
                        _factory_transaction.get_transaction('ipa_information') * 2 + \
                        pp.ZeroOrMore(_factory_transaction.get_transaction('ipa_information'))
