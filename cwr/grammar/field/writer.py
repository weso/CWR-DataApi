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


# Writer Last Name
writer_last_name = basic.alphanum(_config.field_size('writer', 'last_name'))
writer_last_name = writer_last_name.setName('Writer Last Name').setResultsName('writer_last_name')

# Writer First Name
writer_first_name = basic.alphanum(_config.field_size('writer', 'first_name'))
writer_first_name = writer_first_name.setName('Writer First Name').setResultsName('writer_first_name')

# Writer Unknown Indicator
unknown = basic.flag()
unknown = unknown.setName('Writer Unknown Indicator').setResultsName('writer_unknown')

# Reversionary Indicator
reversionary = basic.flag()
reversionary = reversionary.setName('Reversionary Indicator').setResultsName('reversionary')

# First Recording Refusal Indicator
first_recording_refusal = basic.flag()
first_recording_refusal = first_recording_refusal.setName('First Recording Refusal Indicator').setResultsName(
    'first_recording_refusal')

# Work For Hire Indicator
for_hire = basic.flag()
for_hire = for_hire.setName('Work For Hire Indicator').setResultsName('work_for_hire')

# Personal Number
personal_number = basic.numeric(_config.field_size('writer', 'personal_number'))
personal_number = personal_number.setName('Personal Number').setResultsName('personal_number')
