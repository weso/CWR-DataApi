# -*- encoding: utf-8 -*-

"""
Territory entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Territory(object):
    """
    Represents a CWR territory.
    """

    def __init__(self, tis, iso2=None, territory_type=None, name=None, official_name=None):
        self._tis = tis
        self._iso2 = iso2
        self._territory_type = territory_type
        self._name = name
        self._official_name = official_name

    @property
    def iso2(self):
        return self._iso2

    @property
    def name(self):
        return self._name

    @property
    def official_name(self):
        return self._official_name

    @property
    def territory_type(self):
        return self._territory_type

    @property
    def tis(self):
        return self._tis


class TerritoryShare(object):
    """
    Represents a Territory and an Interested Party share on it.
    """

    def __init__(self, ip, territory, share, included, shares_change, sequence_n):
        self._ip = ip
        self._territory = territory
        self._share = share
        self._included = included
        self._shares_change = shares_change
        self._sequence_n = sequence_n

    @property
    def included(self):
        """
        Inclusion/ Exclusion Indicator field.

        This indicates if the Territory is included or excluded. If it is True the Territory is included, otherwise
        it is False.

        :return: True if the Territory is included, False otherwise
        """
        return self._included

    @property
    def ip(self):
        """
        Interested Party # field.

        This is your unique number that identifies the Interested Party that has collection rights in this territory.

        :return: the Interested Party ID
        """
        return self._ip

    @property
    def sequence_n(self):
        """
        Sequence # field.

        A number assigned sequentially to each territory record which applies to the immediately preceding interested
        party.

        :return: the sequence number
        """
        return self._sequence_n

    @property
    def share(self):
        """
        The share applied to the territory.

        This is a percentage represented as a float. So it ranges from 0 (0%) to 1 (100%).

        :return: the share
        """
        return self._share

    @property
    def shares_change(self):
        """
        Shares Change field.

        If the shares assigned to the writer(s) have changed as a result of sub publication in this territory or for a
        similar reason this field is True.

        :return: True if the shares have changed, False otherwise
        """
        return self.shares_change

    @property
    def territory(self):
        """
        The Territory to which the share applies.

        :return: the Territory
        """
        return self._territory


class CollectionShare(object):
    """
    Shares applied to a Territory.
    """

    def __init__(self, pr_shares, mr_shares, sr_shares):
        self._pr_shares = pr_shares
        self._mr_shares = mr_shares
        self._sr_shares = sr_shares

    @property
    def mr_shares(self):
        """
        MR Collection Shares field.

        This field records the percentage of mechanical rights royalties that are to be collected.

        :return: the percentage of mechanical rights royalties
        """
        return self._mr_shares

    @property
    def pr_shares(self):
        """
        PR Collection Shares field.

        This field records the percentage of performing rights royalties that are to be collected.

        :return: the percentage of performing rights royalties
        """
        return self._pr_shares

    @property
    def sr_shares(self):
        """
        SR Collection Shares field.

        This field records the percentage of synchronization rights royalties that are to be collected.

        :return: the percentage of synchronization rights royalties
        """
        return self._sr_shares
