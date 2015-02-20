# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage


"""
Grammar for CWR files.
This is used along with pyparsing to create a BNF grammar.
This stored basic nodes in the parsing tree, to be reused on the parsers, which will copy them and set up any
parsing action required for them.
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

# GENERAL FIELDS

"""
Date follows the pattern YYYYMMDD, with the following constraints:
- YYYY: can be any number
- MM: from 01 to 12
- DD: from 01 to 31
"""
date_field = pp.Regex('[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])').setParseAction(
    lambda d: datetime.datetime.strptime(d[0], '%Y%m%d'))

"""
Time follows the pattern HHMMSS, with the following constraints:
- HH: from 00 to 23
- MM: from 00 to 59
- SS: from 00 to 59
"""
time_field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]').setParseAction(
    lambda t: datetime.datetime.strptime(t[0], '%H%M%S'))

"""
Alphanumeric. Only capital letters are allowed.
"""


def alphanum(columns):
    """
    Alphanumeric field.

    This is an alphanumeric CWR field, accepting only ASCII characters in upper case.

    The field will be stripped of heading and trailing spaces.

    :param columns: number of columns for this field
    :return: a parser for the Alphanumeric field
    """
    return pp.Regex('([\x00-\x60]|[\x7B-\x7F]){' + str(columns) + '}').setParseAction(lambda s: s[0].strip())


"""
Numeric field. Only integers.
"""


def numeric(columns):
    """
    Numeric field.

    This is an integer numeric field.

    The field will be transformed into an integer.

    :param columns: number of columns for this field
    :return: a parser for the integer numeric field
    """
    return pp.Word(pp.nums, exact=columns).setParseAction(lambda n: int(n[0]))

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

    return (_character_sets | _unicode_1_16b | _unicode_2_21b).setParseAction(lambda s: s[0].strip())

# RECORD FIELDS

record_type = pp.oneOf(data.record_types()).setResultsName('record_type')