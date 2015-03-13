# -*- coding: utf-8 -*-

import pyparsing as pp


"""
CWR Acknowledgement constraints.

These are for validating agreements.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def title_when_record_requires(acknowledgement):
    """
    Ensures that the Creation Title is set if the Original Transaction Type requires it.

    The validation fails if:
    - The Original Transaction Type requires the Creation Title to be set but it is empty

    :param acknowledgement: the agreement to validate
    """

    if acknowledgement.original_transaction_type in ('NWR', 'REV') and len(acknowledgement.creation_title) == 0:
        # The Transaction is of a type which requires the title
        # And
        # No title has been set
        message = 'When the Transaction Type is %s the Creation Title must be set' % acknowledgement.original_transaction_type
        raise pp.ParseException('', msg=message)
