# -*- encoding: utf-8 -*-

import pyparsing as pp
import datetime

from cwr.parsing.data.accessor import ParserDataStorage


"""
Grammar for CWR files.
This is used along with pyparsing to create a BNF grammar.
This stored basic nodes in the parsing tree, to be reused on the parsers, which will copy them and set up any
parsing action required for them.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source

data = ParserDataStorage()

# GENERAL FIELDS

"""
Date follows the pattern YYYYMMDD, with the following constraints:
- YYYY: can be any number
- MM: from 01 to 12
- DD: from 01 to 31
"""
date_field = pp.Regex('[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])')

"""
Time follows the pattern HHMMSS, with the following constraints:
- HH: from 00 to 24
- MM: from 00 to 59
- SS: from 00 to 59
"""
time_field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]')

"""
Alphanumeric. Only capital letters are allowed.
"""
alphanum_type = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 "

# CONCRETE CASES FIELDS

"""
Characters sets should be one of the CWR list or the Unicode UTF-8 table.

The Unicode UTF-8 codes are those with up to 16 or 21 bits.
"""
char_sets = None
for char_set in data.character_sets():
    regex = '[ ]{' + str(15 - len(char_set)) + '}' + char_set
    if char_sets is None:
        char_sets = regex
    else:
        char_sets += '|' + regex

_character_sets = pp.Regex(char_sets)
_unicode_1_16b = pp.Regex('U\+0[0-8,A-F]{3}[ ]{9}')
_unicode_2_21b = pp.Regex('U\+0[0-8,A-F]{4}[ ]{8}')

char_code = _character_sets | _unicode_1_16b | _unicode_2_21b

# RECORD FIELDS

record_type = pp.oneOf(data.record_types()).setResultsName('record_type')

# METHODS


def to_integer(parsed):
    """
    Transforms a string into an integer.

    :param parsed: result of parsing a number
    :return: an integer created from the input
    """
    return int(parsed[0])


def to_string(parsed):
    """
    Transforms a parsed string into a usable string.

    This just trims the edges, removing unneeded spaces.

    :param parsed: result of parsing an alphanumeric field
    :return: a usable string
    """
    return parsed[0].strip()


def to_date(parsed):
    """
    Transforms a string into a datetime.

    This should be on the format YYYYMMDD.

    :param parsed: result of parsing a date
    :return: a datetime created from the input
    """
    return datetime.datetime.strptime(parsed[0], '%Y%m%d')


def to_time(parsed):
    """
    Transforms a string into a datetime.

    This should be on the format HHMMSS.

    :param parsed: result of parsing a time
    :return: a datetime created from the input
    """
    return datetime.datetime.strptime(parsed[0], '%H%M%S')