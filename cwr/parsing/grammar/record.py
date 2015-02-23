# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage

"""
Grammar for Records.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


# Acquires config data source
data = ParserDataStorage()

# RECORD FIELDS

record_type = pp.oneOf(data.record_types()).setName('Record Type').setResultsName('record_type')