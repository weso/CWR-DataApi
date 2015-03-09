# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table
from cwr.grammar.field import agreement as field_agreement
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
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
Agreement patterns.
"""

# Agreement Pattern
agreement = field_special.lineStart + field_record.record_prefix(
    _config.record_type('agreement'),
    compulsory=True) + field_agreement.submitter_agreement_n + field_agreement.is_code + field_table.agreement_type() + \
            field_agreement.agreement_start_date + field_agreement.agreement_end_date + field_agreement.retention_end_date + field_table.prior_royalty_status(
    True) + \
            field_agreement.prior_royalty_start_date + field_table.post_term_collection_status(
    True) + field_agreement.post_term_collection_end_date + \
            field_agreement.date_of_signature + field_agreement.number_works + field_table.sm_clause() + \
            field_agreement.sales_change + field_agreement.advance_given + field_agreement.society_id + \
            field_special.lineEnd

"""
Parsing actions for the patterns.
"""

agreement.setParseAction(lambda a: _to_agreement(a))

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