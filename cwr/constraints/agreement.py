# -*- coding: utf-8 -*-

import pyparsing as pp


"""
CWR Agreement constraints.

These are for validating agreements.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def prior_royalty_status_and_date_coherency(agreement):
    """
    Ensures that the Prior Royalty Date is set only when required. And that in that case it is not empty.

    The validation fails if:
    - The status is not set for 'Date' and a date is set
    - The status is set for 'Date' and no date is set

    :param agreement: the agreement to validate
    """
    status = agreement.post_term_collection_status
    date = agreement.prior_royalty_start_date

    if status == 'D':
        # Date should be set
        if not date:
            # Date is not set
            raise pp.ParseException(str(date), msg='Prior Royalty Start Date required')
    elif date:
        # Date should not be set and date is set
        raise pp.ParseException(str(date), msg='Prior Royalty Start Date should not be set')


def post_term_collection_status_and_date_coherency(agreement):
    """
    Ensures that the Post Term Collection Status is set only when required. And that in that case it is not empty.

    The validation fails if:
    - The status is not set for 'Date' and a date is set
    - The status is set for 'Date' and no date is set

    :param agreement: the agreement to validate
    """
    status = agreement.prior_royalty_status
    date = agreement.post_term_collection_end_date

    if status == 'D':
        # Date should be set
        if not date:
            # Date is not set
            raise pp.ParseException(str(date), msg='Post Term Collection End Date required')
    elif date:
        # Date should not be set and date is set
        raise pp.ParseException(str(date),
                                msg='Post Term Collection End Date should not be set')


def retention_end_date_after_agreement_end_date(agreement):
    """
    Ensures that the Retention End Date is set after the Agreement End Date. And also that if the first is set
    then the second exists.

    This tests assumes the Agreement End Date is valid.

    The validation is performed if:
    - The Retention End Date is set

    The validation fails if:
    - The Agreement End Date is not set
    - The Agreement End Date is after the Retention End Date

    :param agreement: the agreement to validate
    """
    if agreement.retention_end_date:
        # Retention End Date set
        if not agreement.agreement_end_date:
            # Agreement End Date not set
            raise pp.ParseException('',
                                    msg='Retention End Date requires the Agreement End Date to be set')
        elif agreement.agreement_end_date >= agreement.retention_end_date:
            # Agreement End Date after Retention End Date
            raise pp.ParseException('',
                                    msg='The Retention End Date must be after the Agreement End Date')


def prior_royalty_start_date_before_agreement_start_date(agreement):
    """
    Ensures that the Prior Royalty Start Date is set before the Agreement Start Date. And also that if the first is set
    then the second exists.

    This tests assumes the Agreement Start Date is valid.

    As it is a compulsory field, it should always exist.

    The validation is performed if:
    - The Prior Royalty Start Date is set

    The validation fails if:
    - The Prior Royalty Start Date is after the Agreement Start Date

    :param agreement: the agreement to validate
    """
    if agreement.prior_royalty_start_date and agreement.prior_royalty_start_date >= agreement.agreement_start_date:
        # Prior Royalty Start Date after Agreement Start Date
        raise pp.ParseException('',
                                msg='The Prior Royalty Start Date must be before the Agreement Start Date')


def post_term_collection_end_date_after_end_dates(agreement):
    """
    Ensures that the Post Term Collection End DAte is set after the Agreement End Date or Retention End Date. And also that if the first is set
    then the second exists.

    The Retention End Date takes more priority, so it will be used instead of the Agreement End Date if it exists.

    This tests assumes the Agreement End Date and Retention End Date are valid.

    The validation is performed if:
    - The Post Term Collection End Date is set

    The validation fails if:
    - The Retention End Date exists and is after the Post Term Collection End Date
    - The Retention End Date does not exist and the Agreement End Date is after the Post Term Collection End Date
    - The Retention End Date and the Agreement End Date do not exist

    :param agreement: the agreement to validate
    """
    if agreement.post_term_collection_end_date:
        # Post Term Collection End Date set
        if agreement.retention_end_date:
            # Retention End Date exists
            # This takes more priority than the Agreement End Date on the verification
            if agreement.post_term_collection_end_date <= agreement.retention_end_date:
                # Retention End Date is after the Post Term Collection End Date
                raise pp.ParseException('',
                                        msg='The Post Term Collection End Date must be after the Retention End Date')
        elif agreement.agreement_end_date:
            # Agreement End Date exists
            if agreement.post_term_collection_end_date <= agreement.agreement_end_date:
                # Agreement End Date is after the Post Term Collection End Date
                raise pp.ParseException('',
                                        msg='The Post Term Collection End Date must be after the Agreement End Date')
        else:
            # No required date exists
            raise pp.ParseException('',
                                    msg='The Post Term Collection End Date requires the Agreement End Date or the Retention End Date to be set')


def sales_manufacture_required_by_agreement_type(agreement):
    """
    Ensures that the Sales/Manufacture Clause is set if the Agreement Type requires so.

    The validation fails if:
    - The Agreement Type requires the Sales/Manufacture Clause to be set and it is not set

    :param agreement: the agreement to validate
    """
    if agreement.agreement_type in ('OP', 'OS') and not agreement.sales_manufacture_clause:
        message = "The Sales/Manufacture Clause is required for the agreement type %s" % agreement.agreement_type
        raise pp.ParseException('', msg=message)