# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table, record, basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Validation Number
validation = basic.numeric(_config.field_size('message', 'validation'))
validation = validation.setName('Validation Number').setResultsName('validation')

# Message Record Type
record_message = table.record_types()
record_message = record_message.setName('Message Record Type').setResultsName('message_record_type')

# Message Text
message_text = basic.alphanum(_config.field_size('message', 'text'))
message_text = message_text.setName('Message Text').setResultsName('message_text')

# Original Record Sequence #
sequence_n = record.record_seq_n(compulsory=True)
sequence_n = sequence_n.setName('Original Record Sequence #').setResultsName('sequence_n')
