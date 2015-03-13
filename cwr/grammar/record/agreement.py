# -*- coding: utf-8 -*-

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
    compulsory=True) + \
            field_agreement.prior_royalty_start_date + field_table.post_term_collection_status(
    compulsory=True) + field_agreement.post_term_collection_end_date + \
            field_agreement.date_of_signature + field_agreement.number_works + field_table.sm_clause() + \
            field_agreement.sales_change + field_agreement.advance_given + field_agreement.society_assigned_agreement_n + \
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
    return AgreementRecord(record_type=parsed.record_type,
                           transaction_sequence_n=parsed.transaction_sequence_n,
                           record_sequence_n=parsed.record_sequence_n,
                           submitter_agreement_n=parsed.submitter_agreement_n,
                           agreement_type=parsed.agreement_type,
                           agreement_start_date=parsed.agreement_start_date,
                           prior_royalty_status=parsed.prior_royalty_status,
                           post_term_collection_status=parsed.post_term_collection_status,
                           number_of_works=parsed.number_of_works,
                           society_assigned_agreement_n=parsed.society_assigned_agreement_n,
                           international_standard_code=parsed.international_standard_code,
                           sales_manufacture_clause=parsed.sales_manufacture_clause,
                           agreement_end_date=parsed.agreement_end_date,
                           date_of_signature=parsed.date_of_signature,
                           retention_end_date=parsed.retention_end_date,
                           prior_royalty_start_date=parsed.prior_royalty_start_date,
                           post_term_collection_end_date=parsed.post_term_collection_end_date,
                           shares_change=parsed.shares_change,
                           advance_given=parsed.advance_given)