# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.record import publisher, nra, writer, agreement, work, acknowledgement, ari
from cwr.grammar import work_detail, interested_party
from cwr.grammar.record import work_detail as rule_work_detail


"""
CWR transaction grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Agreement
agreement_transaction = agreement.agreement + pp.OneOrMore(interested_party.territory_information)

# Work
work_transaction = work.work_record + pp.Optional(pp.OneOrMore(interested_party.controlled_publisher_information)) + \
                   pp.Optional(pp.OneOrMore(publisher.publisher)) + \
                   pp.Optional(pp.OneOrMore(interested_party.controlled_writer_information)) + \
                   pp.Optional(pp.OneOrMore(writer.writer)) + \
                   pp.Optional(pp.OneOrMore(rule_work_detail.alternate)) + pp.Optional(nra.nat) + \
                   pp.Optional(work_detail.information_for_excerpts) + pp.Optional(work_detail.information_for_versions) \
                   + pp.Optional(pp.OneOrMore(rule_work_detail.performing)) + pp.Optional(pp.OneOrMore(nra.npr)) + \
                   pp.Optional(rule_work_detail.recording) + pp.Optional(rule_work_detail.origin) + \
                   pp.Optional(pp.OneOrMore(work_detail.instrumentation_information)) + \
                   pp.Optional(pp.OneOrMore(work_detail.information_for_components)) + \
                   pp.Optional(pp.OneOrMore(ari.ari))

# Acknowledgement
acknowledgement_transaction = acknowledgement.acknowledgement + pp.Optional(pp.OneOrMore(acknowledgement.message)) + (
    agreement.agreement | (work.work_record + pp.Optional(work.conflict)))
