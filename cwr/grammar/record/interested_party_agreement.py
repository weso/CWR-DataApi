# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import society
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.agreement import InterestedPartyForAgreementRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Interested Party in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = DefaultFieldFactory(_config.load_field_config('table'), CWRTables())
_common_factory = DefaultFieldFactory(_config.load_field_config('common'))

"""
IPA patterns.
"""

interested_party_agreement = field_special.lineStart + \
                             field_record.record_prefix(_config.record_type('ipa'), compulsory=True) + \
                             _lookup_factory.get_field('agreement_role_code', compulsory=True) + \
                             _common_factory.get_field('ipi_name_n') + \
                             _common_factory.get_field('ipi_base_n') + \
                             _common_factory.get_field('ip_n', compulsory=True) + \
                             _common_factory.get_field('ip_last_name', compulsory=True) + \
                             _common_factory.get_field('ip_writer_first_name') + \
                             _lookup_factory.get_field('pr_affiliation') + \
                             society.pr_share() + \
                             _lookup_factory.get_field('mr_affiliation') + \
                             society.mr_share() + \
                             _lookup_factory.get_field('sr_affiliation') + \
                             society.sr_share() + \
                             field_special.lineEnd

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
    return InterestedPartyForAgreementRecord(record_type=parsed.record_type,
                                             transaction_sequence_n=parsed.transaction_sequence_n,
                                             record_sequence_n=parsed.record_sequence_n,
                                             ip_n=parsed.ip_n,
                                             ip_last_name=parsed.ip_last_name,
                                             agreement_role_code=parsed.agreement_role_code,
                                             ip_writer_first_name=parsed.ip_writer_first_name,
                                             ipi_name_n=parsed.ipi_name_n, ipi_base_n=parsed.ipi_base_n,
                                             pr_society=parsed.pr_affiliation, pr_share=parsed.pr_share,
                                             mr_society=parsed.mr_affiliation, mr_share=parsed.mr_share,
                                             sr_society=parsed.sr_affiliation, sr_share=parsed.sr_share)