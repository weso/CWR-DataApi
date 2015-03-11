# -*- coding: utf-8 -*-

import pyparsing as pp


"""
CWR Publisher constraints.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def no_owner_has_no_shares(publisher):
    """
    Ensures that the Publishers with no rights over the work have no shares.

    The validation fails if:
    - Publisher is not an Acquirer or Original Publisher and has PR, MR or SR shares

    :param publisher: the Publisher to validate
    """
    if publisher.publisher_type in ('AM', 'ES', 'PA', 'SE'):
        shares = 0

        if publisher.pr_society is not None:
            shares += publisher.pr_ownership_share

        if publisher.mr_society is not None:
            shares += publisher.mr_ownership_share

        if publisher.sr_society is not None:
            shares += publisher.sr_ownership_share

        if shares > 0:
            raise pp.ParseException('', msg='Publishers which do not own a work should have shares set for it')


def owner_has_shares(publisher):
    """
    Ensures that if the Publisher is an acquiror it has shares.

    The validation fails if:
    - Publisher is an Acquirer and has no shares

    :param publisher: the Publisher to validate
    """
    if publisher.publisher_type == 'AQ':
        shares = 0

        if publisher.pr_society is not None:
            shares += publisher.pr_ownership_share

        if publisher.mr_society is not None:
            shares += publisher.mr_ownership_share

        if publisher.sr_society is not None:
            shares += publisher.sr_ownership_share

        if shares == 0:
            raise pp.ParseException('', msg='Acquiror should have shares set')


def sequence_above_zero(publisher):
    """
    Ensures that if the Publisher sequence number starts with 1.

    The validation fails if:
    - Publisher sequence number is 0

    :param publisher: the Publisher to validate
    """
    if publisher.publisher_sequence_n == 0:
        raise pp.ParseException('', msg='Publisher sequence number should start at 1')


def controlled_publisher_has_id(publisher):
    """
    Ensures that if the Publisher is controlled by the submitter then it has an id.

    The validation fails if:
    - Publisher record is SPU and Interested Party # is not entered

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'SPU' and publisher.publisher.ip_n is None:
        raise pp.ParseException('', msg='Publishers controlled by the submitter should have an ID')


def controlled_or_known_publisher_has_name(publisher):
    """
    Ensures that if the Publisher is controlled by the submitter or it is known then it has a name.

    The validation fails if:
    - Publisher record is SPU and no has no name
    - Publisher record is OPU, Publisher Unknown Indicator is not 'Y' and no has no name

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'SPU' and (publisher.publisher.publisher_name is None or publisher.publisher.publisher_name == ''):
        raise pp.ParseException('', msg='Publishers controlled by the submitter should have a name')
    elif publisher.record_type == 'OPU' and publisher.publisher_unknown == 'N':
        raise pp.ParseException('', msg='Known Publishers should have a name')


def controlled_has_type(publisher):
    """
    Ensures that if the Publisher is controlled by the submitter it has a type.

    The validation fails if:
    - Publisher record is SPU and no has no publisher type

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'SPU' and publisher.publisher_type is None:
        raise pp.ParseException('', msg='Publishers controlled by the submitter should have a Publisher Type')


def controlled_has_unknown_blank(publisher):
    """
    Ensures that if the Publisher is controlled by the submitter the unknown indicator is blank.

    The validation fails if:
    - Publisher record is SPU and the Publisher Unknown Indicator is not blank

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'SPU' and publisher.publisher_unknown is not None:
        raise pp.ParseException('',
                                msg='Publishers controlled by the submitter should not have the Publisher Unknown Indicator set')


def other_has_unknown_not_blank(publisher):
    """
    Ensures that if the Publisher is not controlled by the submitter the unknown indicator is not blank.

    The validation fails if:
    - Publisher record is OPU and the Publisher Unknown Indicator is blank

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'OPU' and publisher.publisher_unknown is None:
        raise pp.ParseException('',
                                msg='Publishers not controlled by the submitter should have the Publisher Unknown Indicator set')


def other_unknown_has_no_name(publisher):
    """
    Ensures that if the Publisher is not known it has no name.

    The validation fails if:
    - Publisher record is OPU, the Publisher Unknown Indicator is 'Y' and it has a name

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'OPU' and publisher.publisher_unknown == 'Y' and len(publisher.publisher.publisher_name) > 0:
        raise pp.ParseException('', msg='Unknown publishers should not have a name')


def opu_special_agreement(publisher):
    """
    Ensures that not controlled Publisher have the correct agreement code.

    The validation fails if:
    - Publisher record is OPU, the Special Agreements Indicator can only be 'L' or blank

    :param publisher: the Publisher to validate
    """
    if publisher.record_type == 'OPU' and publisher.special_agreements is 'Y':
        raise pp.ParseException('',
                                msg='Not controlled publishers should have "L" or blank as Special Agreements Indicator')