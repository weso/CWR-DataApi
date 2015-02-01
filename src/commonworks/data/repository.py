# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
Offers interfaces to create repositories for the CWR model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Repository(object):
    """
    Interface for the mongo pattern.

    A mongo works like mix between a DAO and a collection of persistent entities. Offers CRUD methods, and also
    allows to query the existing entities.

    Querying is done with the 'get' method. It receives a predicate, and all the entities fulfilling it are returned.
    """
    __metaclass__ = ABCMeta

    def add(self, entity):
        pass

    def get(self, predicate):
        pass

    def remove(self, entity):
        pass

    def update(self, entity):
        pass