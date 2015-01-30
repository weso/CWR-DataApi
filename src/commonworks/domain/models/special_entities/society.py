# -*- encoding: utf-8 -*-

"""
Society entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Society(object):
    """
    Represents a CWR society.
    """

    def __init__(self, id, name, former_name):
        self.id = id
        self.name = name
        self.former_name = former_name
