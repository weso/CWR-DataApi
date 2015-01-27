# -*- encoding: utf-8 -*-

"""
Territory entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Territory(object):
    """
    Represents a CWR territory.
    """

    def __init__(self, tis, iso2=None, territory_type=None, name=None, official_name=None):
        self.tis = tis
        self.iso2 = iso2
        self.type = territory_type
        self.name = name
        self.official_name = official_name