# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Writer Territory of Control record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Shares Change
shares_change = basic.boolean()
shares_change = shares_change.setName('Shares Change').setResultsName('shares_change')

# Sequence #
sequence_n = basic.numeric(_config.field_size('writer_territory', 'sequence_n'))
sequence_n = sequence_n.setName('Sequence #').setResultsName('sequence_n')