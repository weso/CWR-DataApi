# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# First Recording Refusal Indicator
# TODO: The writer record uses this same field
first_recording_refusal = basic.lookup(('Y', 'N'), columns=1)
first_recording_refusal = first_recording_refusal.setName('First Recording Refusal Indicator').setResultsName(
    'first_recording_refusal')
