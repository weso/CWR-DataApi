# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging
import pyparsing as pp


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
    """
    Factory for acquiring record rules.
    """
    __metaclass__ = ABCMeta

    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, record_configs, factory):
        # records already created
        self._records = {}
        # Logger
        self._logger = logging.getLogger(__name__)
        # Configuration for creating the record
        self._record_configs = record_configs
        # Fields factory
        self._factory = factory

    def get_record(self, id):
        return self._lineStart + self._lineEnd

    def _build_record(self, id):
        pass