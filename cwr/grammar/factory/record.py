# -*- coding: utf-8 -*-

from abc import abstractmethod

from cwr.parser.decoder.dictionary import *


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class RecordFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_record(self, id):
        raise NotImplementedError("The get_record method is not implemented")