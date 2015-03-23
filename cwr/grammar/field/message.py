# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_record_factory = DefaultFieldFactory(_config.load_field_config('record'))

# Original Record Sequence #
sequence_n = _record_factory.get_field('record_sequence_n', compulsory=True)
sequence_n = sequence_n.setName('Original Record Sequence #').setResultsName('sequence_n')
