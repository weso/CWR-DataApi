# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import ari as field_ari
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.info import AdditionalRelatedInfoRecord


"""
CWR Additional Related Information grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Patterns.
"""

ari = field_special.lineStart + field_record.record_prefix(_config.record_type('ari'),
                                                           compulsory=True) + field_table.society() + field_ari.work_n + \
      field_table.types_of_right() + field_table.subject_codes() + field_ari.note + field_special.lineEnd

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
                                       parsed.society, parsed.type_of_right, parsed.work_n, parsed.subject_code,
                                       parsed.note)