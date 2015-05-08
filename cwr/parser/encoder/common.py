# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


"""
Base classes for implementing encoder parsers.

An encoder parser receives an instance of a model class and returns a data structure.

For example, it may receive a CWRFile instance and return a JSON.

All encoders are expected to implement the Encoder interface. This offers a single method which receives the class to
encode, and returns an equivalent data structure.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Encoder(object):
    """
    Interface for implementing encoder parsers. These parser receive a class from the domain model and return a data
    structure.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def encode(self, instance):
        """
        Encodes the data, creating a structure from an instance from the domain model.

        :param instance: the instance to encode
        :return: a data structure created from the received data
        """
        raise NotImplementedError('The encode method must be implemented')
