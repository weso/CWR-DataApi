# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Additional Related Information record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Work #
work_number = basic.alphanum(_config.field_size('ari', 'work_number'))
work_number = work_number.setName('Work #').setResultsName('work_id')

# Note
note = basic.alphanum(_config.field_size('ari', 'note'))
note = note.setName('Note').setResultsName('note')
