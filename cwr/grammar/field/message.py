# -*- coding: utf-8 -*-

from cwr.grammar.field import record
from data.accessor import CWRConfiguration


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Original Record Sequence #
sequence_n = record.record_seq_n(compulsory=True)
sequence_n = sequence_n.setName('Original Record Sequence #').setResultsName('sequence_n')
