# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


"""
Offers base classes to parse data from CWR model instances.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Encoder(object):
    """
    Interface for encoders. These are parsers which transform a a model class into another data.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def encode(self, data):
        """
        Encodes the data, creating an structure from a model object instance.

        :param data: the data to encode
        :return: a data structure created from the received data
        """
        raise NotImplementedError('The encode method must be implemented')
