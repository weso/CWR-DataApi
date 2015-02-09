# -*- encoding: utf-8 -*-

"""
Society entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Society(object):
    """
    Represents a CWR society.
    """

    def __init__(self, society_id, name, former_name):
        self._society_id = society_id
        self._name = name
        self._former_name = former_name

    @property
    def society_id(self):
        return self._society_id

    @property
    def name(self):
        return self._name

    @property
    def former_name(self):
        return self._former_name
