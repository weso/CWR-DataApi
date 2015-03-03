# -*- encoding: utf-8 -*-

from data.accessor import CWRTables, CWRConfiguration
from cwr.grammar import field, field_special, record, field_table
from cwr.work import AlternateTitleRecord


"""
CWR Work detail grammar.

This is for the following records:
- Alternate Title (ALT)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
ALT fields.
"""

# Alternate Title
alternate_title = field.alphanum(_config.field_size('alternate_title', 'alternate_title'))
alternate_title = alternate_title.setName('Alternate Title').setResultsName(
    'alternate_title')

"""
Patterns.
"""

alternate = field_special.lineStart + record.record_prefix(_config.record_type('alternate_title')) + \
            alternate_title + field_table.title_type() + field_table.language() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

alternate.setParseAction(lambda p: _to_alternate_title(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_alternate_title(parsed):
    """
    Transforms the final parsing result into an AlternateTitleRecord instance.

    :param parsed: result of parsing an Alternate Title record
    :return: a AlternateTitleRecord created from the parsed record
    """
    return AlternateTitleRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                parsed.alternate_title, parsed.title_type, parsed.language)