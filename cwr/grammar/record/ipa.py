# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table, society
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import ipa as field_ipa
from cwr.agreement import AgreementInterestedParty
from cwr.constraints import ipa as constraints


"""
CWR Interested Party in Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
IPA patterns.
"""

ipa = field_special.lineStart + field_record.record_prefix(_config.record_type('ipa'), compulsory=True) + \
      field_table.agreement_role_code(True) + \
      field_special.ipi_name_number() + field_special.ipi_base_number() + \
      field_special.ip_id(compulsory=True) + field_ipa.ip_last_name + field_ipa.ip_name + \
      society.pr_affiliation() + society.pr_share() + \
      society.mr_affiliation() + society.mr_share() + \
      society.sr_affiliation() + society.sr_share() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

ipa.setParseAction(lambda p: _to_ipa(p))

"""
Validation actions for the patterns.
"""

ipa.addParseAction(lambda p: constraints.acquiror_has_shares(p[0]))
ipa.addParseAction(lambda p: constraints.shares_have_society(p[0]))

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
    return AgreementInterestedParty(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                    parsed.ip_id, parsed.last_name, parsed.agreement_role_code, parsed.writer_name,
                                    parsed.ipi_name, parsed.ipi_base, parsed.pr_society, parsed.pr_share,
                                    parsed.mr_society, parsed.mr_share, parsed.sr_society, parsed.sr_share)