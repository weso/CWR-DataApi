# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.info import AdditionalRelatedInfoRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Additional Related Information grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory = DefaultFieldFactory(_data, CWRTables())

"""
Patterns.
"""

ari = field_special.lineStart + \
      field_record.record_prefix(_config.record_type('ari')) + \
      _factory.get_field('society_code') + \
      _factory.get_field('work_n') + \
      _factory.get_field('type_of_right') + \
      _factory.get_field('subject_code') + \
      _factory.get_field('note') + \
      field_special.lineEnd

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
                                       parsed.society_code, parsed.type_of_right, parsed.work_n, parsed.subject_code,
                                       parsed.note)