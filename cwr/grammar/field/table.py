# -*- coding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables


"""
Grammar rules for concrete CWR Table/List Lookup fields.

These fields all apply the same kind of constraint: all the values not contained in a defined collection are rejected.

The only exception is when the field is set as optional. Then an empty string composed of whitespaces is allowed.

Additionally, the usual constraints of the Alphanumeric field (non lowercase ASCII) apply.

All the values are read from the lists contained in the library, through the CWRTables class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Fields.
"""


def char_code(columns, name=None, compulsory=False):
    """
    Character set code field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Character set code field rules
    """
    if name is None:
        name = 'Char Code Field (' + str(columns) + ' columns)'

    if columns <= 0:
        raise BaseException()

    char_sets = None
    for char_set in _tables.get_data('character_set'):
        regex = '[ ]{' + str(15 - len(char_set)) + '}' + char_set
        if char_sets is None:
            char_sets = regex
        else:
            char_sets += '|' + regex

    # Accepted sets
    _character_sets = pp.Regex(char_sets)
    _unicode_1_16b = pp.Regex('U\+0[0-8,A-F]{3}[ ]{' + str(columns - 6) + '}')
    _unicode_2_21b = pp.Regex('U\+0[0-8,A-F]{4}[ ]{' + str(columns - 7) + '}')

    # Basic field
    char_code_field = (_character_sets | _unicode_1_16b | _unicode_2_21b)

    # Parse action
    char_code_field = char_code_field.setParseAction(lambda s: s[0].strip())

    # Name
    char_code_field.setName(name)

    if not compulsory:
        char_code_field_empty = pp.Regex('[ ]{' + str(columns) + '}')
        char_code_field_empty.setName(name)

        char_code_field_empty.leaveWhitespace()

        char_code_field_empty.setParseAction(pp.replaceWith(None))

        char_code_field = char_code_field | char_code_field_empty

        char_code_field.setName(name)

    return char_code_field
