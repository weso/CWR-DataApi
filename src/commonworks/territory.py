# -*- encoding: utf-8 -*-

"""
Territory model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class IPTerritoryOfControl(object):
    """
    Represents a CWR Interested Party Territory of Control.

    This is for the Publisher Territory of Control (SPT) and Writer Territory of Control (SWT) transactions.

    This indicates the relationship between an Agreement and a Territory. More specifically, it indicates if a territory
    is included or excluded from the Agreement.

    For example, if the Agreement covers all the world except for Europe, two AgreementTerritory entities would be used,
    one indicating that the world is included, and another indicating that Europe is excluded.

    It should be noted that a Territory can only be excluded if it is part of another Territory which is already
    included in the Agreement.

    Territories are identified by a four digit numeric codes. These can be found at http://www.cisac.org/.
    """

    def __init__(self, ip_id, included, tis_numeric_code, pr_col_share=None, mr_col_share=None, sr_col_share=None,
                 shares_change=None):
        self._ip_id = ip_id
        self._included = included
        self._tis_numeric_code = tis_numeric_code
        self._pr_col_share = pr_col_share
        self._mr_col_share = mr_col_share
        self._sr_col_share = sr_col_share
        self._shares_change = shares_change

    @property
    def included(self):
        """
        Inclusion/ Exclusion Indicator field.

        A True value indicates this Territory is included. A False value indicates it is excluded.

        :return: True if the Territory is included, False if it is excluded
        """
        return self._included

    @property
    def ip_id(self):
        """
        Interested Party # field.

        Submitting publisher’s unique identifier for this Interested Party.

        :return: the Interested Party id
        """
        return self._ip_id

    @property
    def mr_col_share(self):
        """
        MR Collection Share field.

        Defines the percentage of the total royalty distributed for sales of CDs, Cassette Tapes, etc. in which the work
        is included which will be collected by (paid to) the publisher. It can be a range from 0 to 100.00

        :return: the MR collection share
        """
        return self._mr_col_share

    @property
    def pr_col_share(self):
        """
        PR Collection Share field.

        Defines the percentage of the total royalty distributed for performance of the work which will be collected by
        (paid to) the publisher within the above Territory.  It can be a range from 0 to 50.00.

        :return: the PR collection share
        """
        return self._pr_col_share

    @property
    def shares_change(self):
        """
        Shares change field.

        If the shares for the writer interest change as a result of subpublication in this territory or for a similar
        reason, set this field to "Y"

        :return: True if the shares change, False otherwise
        """
        return self._shares_change

    @property
    def sr_col_share(self):
        """
        SR Collection Share field.

        Defines the percentage of the total royalty distributed for Synchronization rights to the work which will be
        collected by (paid to) the publisher. It can be a range from 0 to 100.00.

        :return: return SR collection share
        """
        return self._sr_col_share

    @property
    def tis_numeric_code(self):
        """
        TIS Numeric Code field.

        This is the ID for the Territory.

        :return: the Territory TIS code
        """
        return self._tis_numeric_code
