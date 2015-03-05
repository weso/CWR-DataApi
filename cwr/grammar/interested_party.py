# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import publisher, nra, publisher_territory, writer, writer_territory, writer_publisher, \
    agreement_territory, ipa


"""
CWR interested party grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Original Publisher
original_publisher_information = publisher.publisher + \
                                 pp.Optional(nra.npn) + \
                                 pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Administrator
administrator_information = publisher.publisher + pp.Optional(nra.npn) + \
                            pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Subpublisher
subpublisher_information = publisher.publisher + pp.Optional(nra.npn) + \
                           pp.Optional(pp.OneOrMore(publisher_territory.territory))

# Controlled writer
controlled_writer_information = writer.writer + pp.Optional(nra.nwn) + pp.Optional(
    pp.OneOrMore(writer_territory.territory)) + pp.OneOrMore(writer_publisher.publisher)

# Controlled publisher
controlled_publisher_information = original_publisher_information + pp.Optional(
    pp.OneOrMore(administrator_information)) + pp.Optional(pp.OneOrMore(subpublisher_information)) + pp.Optional(
    pp.OneOrMore(publisher.publisher))

# IPA
ipa_information = ipa.ipa + pp.Optional(nra.npa)

# Territory
territory_information = pp.OneOrMore(agreement_territory.territory_in_agreement) + ipa_information * 2 + \
                        pp.ZeroOrMore(ipa_information)
