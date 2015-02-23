# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp


"""
CWR fields grammar.

This stores grammar for parsing the CWR fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# BASIC FIELDS

"""
Alphanumeric (A).

Only capital letters are allowed.
"""


def alphanum(columns):
    """
    Alphanumeric field.

    This is an alphanumeric CWR field, accepting only ASCII characters in upper case.

    The field will be stripped of heading and trailing spaces.

    :param columns: number of columns for this field
    :return: a parser for the Alphanumeric field
    """
    return pp.Regex('([\x00-\x60]|[\x7B-\x7F]){' + str(columns) + '}').setParseAction(lambda s: s[0].strip()).setName(
        'Alphanumeric Field (' + str(columns) + ' columns)')


"""
Numeric field (N) integer.

Only integers.
"""


def numeric(columns):
    """
    Numeric field.

    This is an integer numeric field.

    The field will be transformed into an integer.

    :param columns: number of columns for this field
    :return: a parser for the integer numeric field
    """
    return pp.Word(pp.nums, exact=columns).setParseAction(lambda n: int(n[0])).setName(
        'Numeric Field (' + str(columns) + ' columns)')


"""
Numeric field (N) float.

Float numeric value.
"""


def numeric_float(columns, nums_int):
    """
    Numeric field.

    This is a float numeric field.

    The field will be transformed into an float.

    :param columns: number of columns for this field
    :param nums_int: columns for the integer value
    :return: a parser for the integer numeric field
    """
    return pp.Word(pp.nums, exact=columns).setParseAction(lambda n: _to_numeric_float(n[0], nums_int)).setName(
        'Numeric Field float (' + str(columns) + ' columns)')


def _to_numeric_float(number, nums_int):
    """
    Transforms a string into a float.

    :param number: string with the number
    :param nums_int: columns for the integer value
    :return: a parser for the integer numeric field
    """
    index_end = len(number) - nums_int
    return float(number[:nums_int] + '.' + number[index_end:])


"""
Boolean field (B).

Must be 'Y', for yes/true or 'N' for no/false.
"""
boolean_field = pp.Literal('Y') | pp.Literal('N')

"""
Flag field (F).

Must be 'Y', for yes/true, 'N' for no/false or 'U' for unknown.
"""
flag_field = boolean_field | pp.Literal('U')

"""
Date field (D).

Date follows the pattern YYYYMMDD, with the following constraints:
- YYYY: can be any number
- MM: from 01 to 12
- DD: from 01 to 31
"""
date_field = pp.Regex('[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])').setParseAction(
    lambda d: datetime.datetime.strptime(d[0], '%Y%m%d').date()).setName('Date Field')

"""
Time field (T).

Time follows the pattern HHMMSS, with the following constraints:
- HH: from 00 to 23
- MM: from 00 to 59
- SS: from 00 to 59
"""
time_field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]').setParseAction(
    lambda t: datetime.datetime.strptime(t[0], '%H%M%S').time()).setName('Time Field')

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
