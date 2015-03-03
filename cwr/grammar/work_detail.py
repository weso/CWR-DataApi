# -*- encoding: utf-8 -*-

from data.accessor import CWRTables, CWRConfiguration
from cwr.grammar import field, field_special, record, field_table, work
from cwr.work import AlternateTitleRecord, AuthoredWorkRecord


"""
CWR Work detail grammar.

This is for the following records:
- Alternate Title (ALT)
- Entire Work Title for Excerpts (EWT)
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
EWT fields.
"""

# Entire Work Title
entire_work_title = field.alphanum(_config.field_size('entire_work_title', 'entire_work_title'))
entire_work_title = entire_work_title.setName('Entire Work Title').setResultsName(
    'entire_work_title')

# Writer 1 Last Name
writer_1_last_name = field.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_1_last_name = writer_1_last_name.setName('Writer 1 Last Name').setResultsName(
    'writer_1_last_name')

# Writer 1 First Name
writer_1_first_name = field.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_1_first_name = writer_1_first_name.setName('Writer 1 Last Name').setResultsName(
    'writer_1_first_name')

# Source
source = field.alphanum(_config.field_size('entire_work_title', 'source'))
source = source.setName('Source').setResultsName('source')

# Writer 1 IPI Name #
writer_1_ipi_name = field_special.ipi_name_number()
writer_1_ipi_name = writer_1_ipi_name.setName('Writer 1 IPI Name #').setResultsName('writer_1_ipi_name')

# Writer 1 IPI Base #
writer_1_ipi_base = field_special.ipi_base_number()
writer_1_ipi_base = writer_1_ipi_base.setName('Writer 1 IPI Base #').setResultsName('writer_1_ipi_base')

# Writer 2 Last Name
writer_2_last_name = field.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_2_last_name = writer_2_last_name.setName('Writer 2 Last Name').setResultsName(
    'writer_2_last_name')

# Writer 2 First Name
writer_2_first_name = field.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_2_first_name = writer_2_first_name.setName('Writer 2 Last Name').setResultsName('writer_2_first_name')

# Writer 2 IPI Name #
writer_2_ipi_name = field_special.ipi_name_number()
writer_2_ipi_name = writer_2_ipi_name.setName('Writer 1 IPI Name #').setResultsName('writer_2_ipi_name')

# Writer 2 IPI Base #
writer_2_ipi_base = field_special.ipi_base_number()
writer_2_ipi_base = writer_2_ipi_base.setName('Writer 1 IPI Base #').setResultsName('writer_2_ipi_base')

"""
Patterns.
"""

alternate = field_special.lineStart + record.record_prefix(_config.record_type('alternate_title')) + \
            alternate_title + field_table.title_type() + field_table.language() + field_special.lineEnd

entire_title = field_special.lineStart + record.record_prefix(_config.record_type('entire_work_title')) + \
               entire_work_title + field_special.iswc() + field_table.language() + writer_1_last_name + \
               writer_1_first_name + source + writer_1_ipi_name + \
               writer_1_ipi_base + writer_2_last_name + \
               writer_2_first_name + work.work_id + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

alternate.setParseAction(lambda p: _to_alternate_title(p))

entire_title.setParseAction(lambda p: _to_entire_title(p))

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


def _to_entire_title(parsed):
    """
    Transforms the final parsing result into an AuthoredWorkRecord instance.

    :param parsed: result of parsing an Entire Title record
    :return: a AuthoredWorkRecord created from the parsed record
    """
    return AuthoredWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                              parsed.title, parsed.work_id, parsed.first_name_1, parsed.last_name_1,
                              parsed.first_name_2, parsed.last_name_2, parsed.ipi_base_1,
                              parsed.ipi_name_1, parsed.ipi_base_2, parsed.ipi_name_2,
                              parsed.source, parsed.language_code, parsed.iswc)