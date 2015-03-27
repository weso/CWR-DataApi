# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import publisher, publisher_territory, writer, writer_territory, \
    writer_publisher
from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables

from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

# Original Publisher
original_publisher_information = publisher.publisher + \
                                 pp.Optional(_factory_record.get_transaction_record('nra_publisher_name')) + \
                                 pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Administrator
administrator_information = publisher.publisher + \
                            pp.Optional(_factory_record.get_transaction_record('nra_publisher_name')) + \
                            pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Subpublisher
subpublisher_information = publisher.publisher + \
                           pp.Optional(_factory_record.get_transaction_record('nra_publisher_name')) + \
                           pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Controlled writer
controlled_writer_information = writer.writer + \
                                pp.Optional(_factory_record.get_transaction_record('nra_writer_name')) + \
                                pp.Optional(pp.OneOrMore(writer_territory.territory)) + \
                                pp.OneOrMore(writer_publisher.publisher)

# Controlled publisher
controlled_publisher_information = original_publisher_information + \
                                   pp.Optional(pp.OneOrMore(administrator_information)) + \
                                   pp.Optional(pp.OneOrMore(subpublisher_information)) + \
                                   pp.Optional(pp.OneOrMore(publisher.publisher))

# IPA
ipa_information = _factory_record.get_transaction_record('interested_party_agreement') + \
                  pp.Optional(_factory_record.get_transaction_record('nra_agreement_party'))

# Territory
territory_information = pp.OneOrMore(_factory_record.get_transaction_record('territory_in_agreement')) \
                        + ipa_information * 2 + \
                        pp.ZeroOrMore(ipa_information)
