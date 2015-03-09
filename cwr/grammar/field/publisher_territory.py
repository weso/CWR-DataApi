# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Publisher Territory of Control record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Constant
constant = special.blank(_config.field_size('publisher_territory', 'constant'))

# Shares Change
shares_change = basic.boolean()
shares_change = shares_change.setName('Shares Change').setResultsName('shares_change')

# Sequence #
sequence_n = basic.numeric(_config.field_size('publisher_territory', 'sequence_n'))
sequence_n = sequence_n.setName('Sequence #').setResultsName('sequence_n')
