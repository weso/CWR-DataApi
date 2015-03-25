# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.agreement import InterestedPartyForAgreementRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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