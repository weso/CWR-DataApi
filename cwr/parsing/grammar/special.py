# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage


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
lineEnd = pp.lineEnd.suppress()

# SPECIAL CONSTRAINTS FIELDS

"""
These are fields where special constraints are applied.
"""


def numeric_from(columns, minimum):
    """
    Numeric field with a minimum value.

    This is an integer numeric field where each value should be higher or equal than the minimum

    The field will be transformed into an integer.

    :param columns: number of columns for this field
    :return: a parser for the integer numeric field
    """

    return pp.Word(pp.nums, exact=columns).setParseAction(lambda n: __parse_number_from(n[0], minimum)).setName(
        'Numeric Field (' + str(columns) + ' columns, starting at ' + str(minimum) + ')')


def __parse_number_from(number, minimum):
    """
    Parses a string into an integer, only if it is equal or above a minimum value.

    :param number: the string to parse
    :param minimum: the minimum value
    :return: the parsed number, if it was valid
    """
    result = int(number)
    if result < minimum:
        raise pp.ParseException(0, 0, "number value invalid")

    return result

# RECORD FIELDS

record_type = pp.oneOf(data.record_types()).setResultsName('record_type')

# CONCRETE CASES FIELDS

"""
Characters sets should be one of the CWR list or the Unicode UTF-8 table.

The Unicode UTF-8 codes are those with up to 16 or 21 bits.
"""


def char_code(columns):
    """
    Character set code.

    This is one of the character sets allowed on the file.

    The field will be stripped of heading and trailing spaces.

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

    _character_sets = pp.Regex(char_sets)
    _unicode_1_16b = pp.Regex('U\+0[0-8,A-F]{3}[ ]{' + str(columns - 6) + '}')
    _unicode_2_21b = pp.Regex('U\+0[0-8,A-F]{4}[ ]{' + str(columns - 7) + '}')

    return (_character_sets | _unicode_1_16b | _unicode_2_21b).setParseAction(lambda s: s[0].strip()).setName(
        'Char code Field (' + str(columns) + ' columns)')