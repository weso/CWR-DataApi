# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import record, basic
from cwr.grammar.factory.field import LookupFieldFactory


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = LookupFieldFactory()

# Validation Number
validation = basic.numeric(_config.field_size('message', 'validation'))
validation = validation.setName('Validation Number').setResultsName('validation')

# Message Text
message_text = basic.alphanum(_config.field_size('message', 'text'))
message_text = message_text.setName('Message Text').setResultsName('message_text')

# Original Record Sequence #
sequence_n = record.record_seq_n(compulsory=True)
sequence_n = sequence_n.setName('Original Record Sequence #').setResultsName('sequence_n')
