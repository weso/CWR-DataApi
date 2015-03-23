# -*- coding: utf-8 -*-

from abc import ABCMeta


"""
Common classes for fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FieldBuilder(object):
    """
    Instances of this class generate field rules.

    This serves as an adapter so the different field rules use the same parameters.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def get_field(self, name=None, columns=None, values=None):
        """
        Generates the rules for the field, applying the received parameters.

        :param name: the name of the field
        :param columns: number of columns
        :param values: allowed values for the field
        :return: the rules for the field
        """
        raise NotImplementedError("The get_field method is not implemented")