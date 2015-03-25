# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.agreement import AgreementRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Agreement grammar.
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
Agreement patterns.
"""

# Agreement Pattern
agreement = _factory_record.get_transaction_record('agreement')

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