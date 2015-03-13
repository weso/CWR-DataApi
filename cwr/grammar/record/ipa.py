# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table, society
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import ipa as field_ipa
from cwr.agreement import AgreementInterestedParty


"""
CWR Interested Party in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
IPA patterns.
"""

ipa = field_special.lineStart + field_record.record_prefix(_config.record_type('ipa'), compulsory=True) + \
      field_table.agreement_role_code(compulsory=True) + \
      field_special.ipi_name_number() + field_special.ipi_base_number() + \
      field_special.ip_n(compulsory=True) + field_ipa.ip_last_name + field_ipa.ip_writer_first_name + \
      society.pr_affiliation() + society.pr_share() + \
      society.mr_affiliation() + society.mr_share() + \
      society.sr_affiliation() + society.sr_share() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

ipa.setParseAction(lambda p: _to_ipa(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_ipa(parsed):
    """
    Transforms the final parsing result into an AgreementInterestedParty instance.

    :param parsed: result of parsing an IPA record
    :return: an AgreementInterestedParty created from the parsed record
    """
    return AgreementInterestedParty(record_type=parsed.record_type,
                                    transaction_sequence_n=parsed.transaction_sequence_n,
                                    record_sequence_n=parsed.record_sequence_n,
                                    ip_n=parsed.ip_n,
                                    ip_last_name=parsed.ip_last_name,
                                    agreement_role_code=parsed.agreement_role_code,
                                    ip_writer_first_name=parsed.ip_writer_first_name,
                                    ipi_name_n=parsed.ipi_name_n, ipi_base_n=parsed.ipi_base_n,
                                    pr_society=parsed.pr_society, pr_share=parsed.pr_share,
                                    mr_society=parsed.mr_society, mr_share=parsed.mr_share,
                                    sr_society=parsed.sr_society, sr_share=parsed.sr_share)