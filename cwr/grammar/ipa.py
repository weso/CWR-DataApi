# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field, field_special, record
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
_tables = CWRTables()
_config = CWRConfiguration()

"""
Interested Party in Agreement fields.
"""


def _society():
    society_field = pp.oneOf(_tables.society_codes())
    society_field_empty = pp.Regex('[ ]{3}')

    society_field.setParseAction(lambda c: int(c[0]))
    society_field_empty.setParseAction(pp.replaceWith(None))
    society_field_empty.leaveWhitespace()

    society_field = society_field_empty | society_field

    return society_field

# Record Type for the agreement
record_prefix_agreement = record.record_prefix(_config.record_type('ipa'))

# Agreement Role Code
agreement_role_code = pp.oneOf(_tables.agreement_roles())
agreement_role_code = agreement_role_code.setName('Agreement Role Code').setResultsName('agreement_role_code')

# Interested Party IPI Name #
ipi = field.numeric(_config.field_size('ipa', 'ipi'))
ipi = ipi.setName('Interested Party IPI Name').setResultsName('ipi')

# IPI Base Number
ipi_base = field_special.ipi_base_number()
ipi_base = ipi_base.setName('IPI Base Number').setResultsName('ipi_base')

# Interested Party #
ip_number = field.alphanum(_config.field_size('ipa', 'ip_number'), compulsory=True)
ip_number = ip_number.setName('Interested Party #').setResultsName('ip_id')

# Interested Party Last Name
ip_last_name = field.alphanum(_config.field_size('ipa', 'ip_last_name'), compulsory=True)
ip_last_name = ip_last_name.setName('Interested Party Last Name').setResultsName('last_name')

# Interested Party Writer First Name
ip_name = field.alphanum(_config.field_size('ipa', 'ip_name'))
ip_name = ip_name.setName('Interested Party Writer First Name').setResultsName('writer_name')

# Performing Rights Affiliation Society
pr_affiliation = _society()
pr_affiliation = pr_affiliation.setName('Performing Rights Affiliation Society').setResultsName('pr_society')

# Performing Rights Share
pr_share = field_special.percentage(_config.field_size('ipa', 'pr_share'))
pr_share = pr_share.setName('Performing Rights Share').setResultsName('pr_share')

# Mechanical Rights Affiliation Society
mr_affiliation = _society()
mr_affiliation = mr_affiliation.setName('Mechanical Rights Affiliation Society').setResultsName('mr_society')

# Mechanical Rights Share
mr_share = field_special.percentage(_config.field_size('ipa', 'mr_share'))
mr_share = mr_share.setName('Mechanical Rights Share').setResultsName('mr_share')

# Synchronization Rights Affiliation Society
sr_affiliation = _society()
sr_affiliation = sr_affiliation.setName('Synchronization Rights Affiliation Society').setResultsName('sr_society')

# Synchronization Rights Share
sr_share = field_special.percentage(_config.field_size('ipa', 'sr_share'))
sr_share = sr_share.setName('Synchronization Rights Share').setResultsName('sr_share')

"""
IPA patterns.
"""

ipa = field_special.lineStart + record_prefix_agreement + agreement_role_code + ipi + ipi_base + \
      ip_number + ip_last_name + ip_name + pr_affiliation + pr_share + mr_affiliation + \
      mr_share + sr_affiliation + sr_share + field_special.lineEnd

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
                                    parsed.ipi, parsed.ipi_base, parsed.pr_society, parsed.pr_share,
                                    parsed.mr_society, parsed.mr_share, parsed.sr_society, parsed.sr_share)