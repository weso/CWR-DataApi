# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import publisher, nra, publisher_territory, writer, writer_territory, writer_publisher, \
    work_detail, transmission, group, agreement, work, acknowledgement, agreement_territory, ipa, ari


"""
CWR file grammar.

This contains rules for the internal structure of a CWR file.

This have been created from the BNF description included in the CWR specification.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

original_publisher_information = publisher.publisher + \
                                 pp.Optional(nra.npn) + \
                                 pp.Optional(pp.OneOrMore(publisher_territory.territory))

administrator_information = publisher.publisher + pp.Optional(nra.npn) + \
                            pp.Optional(pp.OneOrMore(publisher_territory.territory))

subpublisher_information = publisher.publisher + pp.Optional(nra.npn) + \
                           pp.Optional(pp.OneOrMore(publisher_territory.territory))

controlled_writer_information = writer.writer + pp.Optional(nra.nwn) + pp.Optional(
    pp.OneOrMore(writer_territory.territory)) + pp.OneOrMore(writer_publisher.publisher)

instrumentation_information = work_detail.inst_summary + pp.Optional(pp.OneOrMore(work_detail.inst_detail))

information_for_excerpts = work_detail.entire_work_title + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

information_for_versions = work_detail.original_title + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

information_for_components = work_detail.component + pp.Optional(nra.nra_work) + pp.Optional(
    pp.OneOrMore(nra.now))

controlled_publisher_information = original_publisher_information + pp.Optional(
    pp.OneOrMore(administrator_information)) + pp.Optional(pp.OneOrMore(subpublisher_information)) + pp.Optional(
    pp.OneOrMore(publisher.publisher))

nwr_transaction = work.work_record + pp.Optional(pp.OneOrMore(publisher.publisher)) + pp.Optional(
    pp.OneOrMore(publisher.publisher)) + pp.Optional(pp.OneOrMore(writer.writer)) + pp.Optional(
    pp.OneOrMore(writer.writer)) + pp.Optional(pp.OneOrMore(work_detail.alternate_title)) + pp.OneOrMore(
    nra.nat) + pp.OneOrMore(information_for_excerpts) + pp.OneOrMore(information_for_versions) + pp.Optional(
    pp.OneOrMore(work_detail.performing)) + pp.Optional(pp.OneOrMore(nra.npr)) + pp.OneOrMore(
    work_detail.recording) + pp.OneOrMore(work_detail.origin) + pp.Optional(
    pp.OneOrMore(instrumentation_information)) + pp.Optional(pp.OneOrMore(information_for_components)) + pp.Optional(
    pp.OneOrMore(ari.ari))

acknowledgement_transaction = acknowledgement.acknowledgement + pp.Optional(pp.OneOrMore(acknowledgement.message)) + (
    agreement.agreement | (work.work_record + pp.Optional(work.conflict)))

acquirer_information = ipa.ipa + pp.Optional(nra.npa)

assignor_information = ipa.ipa + pp.Optional(nra.npa)

territory_information = pp.OneOrMore(agreement_territory.territory_in_agreement) + pp.OneOrMore(assignor_information) + \
                        pp.OneOrMore(acquirer_information)

agreement_transaction = agreement.agreement + pp.OneOrMore(territory_information)

transaction_info = agreement.agreement | work.work_record | acknowledgement.acknowledgement

group_info = group.group_header + pp.OneOrMore(transaction_info) + group.group_trailer

cwr_file = transmission.transmission_header + pp.OneOrMore(group_info) + transmission.transmission_trailer