# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import ParserDataStorage


"""
Grammar for special cases and other fields.

These are miscellany fields and nodes, such as line limiters, or the character encoding field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

# GENERAL GRAMMAR

lineStart = pp.lineStart.suppress()
lineStart.setName("Start of line")

lineEnd = pp.lineEnd.suppress()
lineEnd.setName("End of line")

# CONCRETE CASES FIELDS

"""
Characters sets should be one of the CWR list or the Unicode UTF-8 table.

The Unicode UTF-8 codes are those with up to 16 or 21 bits.
"""


def char_code(columns):
    """
    Character set code.

    This accepts one of the character sets allowed on the file.

    :param columns: number of columns for this field
    :return: a parser for the character set field
    """
    char_sets = None
    for char_set in data.character_sets():
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
    field = (_character_sets | _unicode_1_16b | _unicode_2_21b)

    # Parse action
    field = field.setParseAction(lambda s: s[0].strip())

    # Name
    field.setName('Char Code Field (' + str(columns) + ' columns)')

    return field


def language_code():
    """
    Language code.

    This accepts one of the language codes allowed by the CWR standard.

    :return: a parser for the language code field
    """

    field = pp.oneOf(data.language_codes())

    # Parse action
    field = field.setParseAction(lambda s: s[0].strip())

    # Name
    field.setName('Language Code Field')

    return field