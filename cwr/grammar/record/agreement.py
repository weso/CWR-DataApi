# -*- encoding: utf-8 -*-

import cwr.constraints.agreement as constraints
from data.accessor import CWRConfiguration
from cwr.grammar.field import table, special, record, basic
from cwr.agreement import AgreementRecord


"""
CWR Agreement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Agreement fields.
"""

# Submitter's Agreement Number
submitter_agreement_n = basic.alphanum(_config.field_size('agreement', 'agreement_id'), compulsory=True)
submitter_agreement_n = submitter_agreement_n.setName('Submitters Agreement Number').setResultsName('agreement_id')

# International Standard Agreement Code
is_code = basic.alphanum(_config.field_size('agreement', 'international_standard_code'))
is_code = is_code.setName('International Standard Agreement Code').setResultsName('international_standard_code')

# Agreement Start Date
agreement_start_date = basic.date(compulsory=True)
agreement_start_date = agreement_start_date.setName('Agreement Start Date').setResultsName('start_date')

# Agreement End Date
agreement_end_date = basic.date()
agreement_end_date = agreement_end_date.setName('Agreement End Date').setResultsName('end_date')

# Retention End Date
retention_end_date = basic.date()
retention_end_date = retention_end_date.setName('Retention End Date').setResultsName('retention_end_date')

# Prior Royalty Start Date
prior_royalty_start_date = basic.date()
prior_royalty_start_date = prior_royalty_start_date.setName('Prior Royalty Start Date').setResultsName(
    'prior_royalty_start_date')

# Post Term Collection End Date
post_term_collection_end_date = basic.date()
post_term_collection_end_date = post_term_collection_end_date.setName('Post Term Collection End Date').setResultsName(
    'post_term_collection_end_date')

# Date of Signature of Agreement
date_of_signature = basic.date()
date_of_signature = date_of_signature.setName('Date of Signature of Agreement').setResultsName('signature_date')

# Number of Works
number_works = basic.numeric(_config.field_size('agreement', 'number_works'), compulsory=True)
number_works = number_works.setName('Number of Works').setResultsName('works_number')

# Shares Change
sales_change = basic.boolean()
sales_change = sales_change.setName('Shares Change').setResultsName('shares_change')

# Advance Given
advance_given = basic.boolean()
advance_given = advance_given.setName('Advance Given').setResultsName('advance_given')

# Society Given Agreement Number
society_id = basic.alphanum(_config.field_size('agreement', 'society_agreement_number'))
society_id = society_id.setName('Society Given Agreement Number').setResultsName('society_agreement_number')
society_id.leaveWhitespace()

"""
Agreement patterns.
"""

# Agreement Pattern
agreement = special.lineStart + record.record_prefix(
    _config.record_type('agreement'), compulsory=True) + submitter_agreement_n + is_code + table.agreement_type() + \
            agreement_start_date + agreement_end_date + retention_end_date + table.prior_royalty_status(True) + \
            prior_royalty_start_date + table.post_term_collection_status(True) + post_term_collection_end_date + \
            date_of_signature + number_works + table.sm_clause() + sales_change + advance_given + society_id + \
            special.lineEnd

"""
Parsing actions for the patterns.
"""

agreement.setParseAction(lambda a: _to_agreement(a))

"""
Validation actions for the patterns.
"""

agreement.addParseAction(lambda p: constraints.prior_royalty_status_and_date_coherency(p[0]))
agreement.addParseAction(lambda p: constraints.post_term_collection_status_and_date_coherency(p[0]))
agreement.addParseAction(lambda p: constraints.retention_end_date_after_agreement_end_date(p[0]))
agreement.addParseAction(lambda p: constraints.prior_royalty_start_date_before_agreement_start_date(p[0]))
agreement.addParseAction(lambda p: constraints.post_term_collection_end_date_after_end_dates(p[0]))
agreement.addParseAction(lambda p: constraints.sales_manufacture_required_by_agreement_type(p[0]))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_agreement(parsed):
    """
    Transforms the final parsing result into an AgreementRecord instance.

    :param parsed: result of parsing an Agreement transaction header
    :return: a AgreementRecord created from the parsed record
    """
    return AgreementRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                           parsed.agreement_id, parsed.agreement_type, parsed.start_date,
                           parsed.prior_royalty_status, parsed.post_term_collection_status, parsed.works_number,
                           society_agreement_number=parsed.society_agreement_number,
                           international_standard_code=parsed.international_standard_code,
                           sales_manufacture_clause=parsed.sales_manufacture_clause,
                           end_date=parsed.end_date, signature_date=parsed.signature_date,
                           retention_end_date=parsed.retention_end_date,
                           prior_royalty_start_date=parsed.prior_royalty_start_date,
                           post_term_collection_end_date=parsed.post_term_collection_end_date,
                           shares_change=parsed.shares_change, advance_given=parsed.advance_given)