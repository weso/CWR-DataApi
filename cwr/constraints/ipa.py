# -*- encoding: utf-8 -*-

import pyparsing as pp


"""
CWR IPA constraints.

These are for validating Interested Parties for Agreements.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def acquiror_has_shares(ipa):
    """
    Ensures that the Acquiror IPAs has shares on the Agreement.

    The validation fails if:
    - IPA is set as an acquiror and has no PR, MR or SR shares

    :param ipa: the IPA to validate
    """
    if ipa.agreement_role_code == 'AC':
        shares = 0
        if ipa.pr_society is not None:
            shares += ipa.pr_share
        elif ipa.mr_society is not None:
            shares += ipa.mr_share
        elif ipa.sr_society is not None:
            shares += ipa.sr_share

        if shares == 0:
            raise pp.ParseException('', msg='Acquiror should have shares set')


def shares_have_society(ipa):
    """
    Ensures that for any shares set a society is set.

    The validation fails if:
    - PR shares are set and no PR society is set
    - MR shares are set and no MR society is set
    - SR shares are set and no SR society is set

    :param ipa: the IPA to validate
    """

    if ipa.pr_share > 0 and ipa.pr_society is None:
        raise pp.ParseException('', msg='Shares set for PR but PR society missing')

    if ipa.mr_share > 0 and ipa.mr_society is None:
        raise pp.ParseException('', msg='Shares set for MR but MR society missing')

    if ipa.sr_share > 0 and ipa.sr_society is None:
        raise pp.ParseException('', msg='Shares set for SR but SR society missing')