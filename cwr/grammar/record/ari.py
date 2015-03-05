# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table, special, record, basic
from cwr.info import AdditionalRelatedInfoRecord


"""
CWR Additional Related Information grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
ARI fields.
"""

# Work #
work_number = basic.alphanum(_config.field_size('ari', 'work_number'))
work_number = work_number.setName('Work #').setResultsName('work_id')

# Note
note = basic.alphanum(_config.field_size('ari', 'note'))
note = note.setName('Note').setResultsName('note')

"""
Patterns.
"""

ari = special.lineStart + record.record_prefix(_config.record_type('ari')) + table.society() + work_number + \
      table.types_of_right() + table.subject_codes() + note + special.lineEnd

"""
Parsing actions for the patterns.
"""

ari.setParseAction(lambda p: _to_ari(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_ari(parsed):
    """
    Transforms the final parsing result into an AdditionalRelatedInfoRecord instance.

    :param parsed: result of parsing an Additional Related Information record
    :return: a AdditionalRelatedInfoRecord created from the parsed record
    """
    return AdditionalRelatedInfoRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                       parsed.society, parsed.type_of_right, parsed.work_id, parsed.subject_code,
                                       parsed.note)