# -*- encoding: utf-8 -*-

import pyparsing as pp


"""
CWR Agreement constraints.
"""


def prior_royalty_status_and_date_coherency(parsed):
    status = parsed.post_term_collection_status
    date = parsed.prior_royalty_start_date

    if status == 'D':
        if not date:
            raise pp.ParseException(str(date), msg='Prior Royalty Start Date required')
    elif date:
        raise pp.ParseException(str(date), msg='Prior Royalty Start Date should not be set')


def post_term_collection_status_and_date_coherency(parsed):
    status = parsed.prior_royalty_status
    date = parsed.post_term_collection_end_date

    if status == 'D':
        if not date:
            raise pp.ParseException(str(date), msg='Post Term Collection End Date required')
    elif date:
        raise pp.ParseException(str(date),
                                msg='Post Term Collection End Date should not be set')


def retention_end_date_after_agreement_end_date(parsed):
    if parsed.retention_end_date:
        if not parsed.end_date:
            raise pp.ParseException('',
                                    msg='Retention End Date requires the Agreement End Date to be set')
        elif parsed.end_date >= parsed.retention_end_date:
            raise pp.ParseException('',
                                    msg='The Retention End Date must be after the Agreement End Date')


def prior_royalty_start_date_before_agreement_end_date(parsed):
    if parsed.prior_royalty_start_date and parsed.prior_royalty_start_date >= parsed.start_date:
        raise pp.ParseException('',
                                msg='The Prior Royalty Start Date must be before the Agreement End Date')


def post_term_collection_end_date_after_end_dates(parsed):
    if parsed.post_term_collection_end_date:
        if parsed.retention_end_date:
            if parsed.post_term_collection_end_date <= parsed.retention_end_date:
                raise pp.ParseException('',
                                        msg='The Post Term Collection End Date must be after the Retention End Date')
        elif parsed.end_date:
            if parsed.post_term_collection_end_date <= parsed.end_date:
                raise pp.ParseException('',
                                        msg='The Post Term Collection End Date must be after the Agreement End Date')
        else:
            raise pp.ParseException('',
                                    msg='The Post Term Collection End Date requires the Agreement End Date or the Retention End Date to be set')


def sales_manufacture_required_by_agreement_type(parsed):
    if parsed.agreement_type in ('OP', 'OS') and len(parsed.sales_manufacture_clause) == 0:
        message = "The Sales/Manufacture Clause is required for the agreement type %s" % (parsed.agreement_type)
        raise pp.ParseException('', msg=message)