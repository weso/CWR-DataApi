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

    def __init__(self, territory, share):
        self._territory = territory
        self._share = share

    @property
    def share(self):
        """
        The share applied to the territory.

        This is a percentage represented as a float. So it ranges from 0 (0%) to 1 (100%).

        :return: the share
        """
        return self._share

    @property
    def territory(self):
        """
        The Territory to which the share applies.

        :return: the Territory
        """
        return self._territory

