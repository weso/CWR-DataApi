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
    return (pp.Regex('([\x00-\x60]|[\x7B-\x7F]){' + str(columns) + '}')).leaveWhitespace().setParseAction(
        lambda s: s[0].strip()).setName(
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
boolean_field = (pp.Literal('Y') | pp.Literal('N')).setParseAction(lambda b: _to_boolean(b[0])).setName('Boolean Field')


def _to_boolean(string):
    """
    Transforms a string into a boolean value.

    If a value which is not 'Y' or 'N' is received, a ParseException is thrown

    :param: string: the string to transform
    :return: True if the string is 'Y', False if it is 'N'
    """

    if string == 'Y':
        result = True
    elif string == 'N':
        result = False
    else:
        raise pp.ParseException

    return result


"""
Flag field (F).

Must be 'Y', for yes/true, 'N' for no/false or 'U' for unknown.
"""
flag_field = (pp.Literal('Y') | pp.Literal('N') | pp.Literal('U')).setParseAction(lambda f: _to_flag(f[0])).setName(
    'Flag Field')


def _to_flag(string):
    """
    Transforms a string into a flag value.

    If a value which is not 'Y', 'N' or 'U' is received, a ParseException is thrown

    :param: string: the string to transform
    :return: True if the string is 'Y', False if it is 'N'
    """

    if string not in ('Y', 'N', 'U'):
        raise pp.ParseException

    return string


"""
Date field (D).

Date follows the pattern YYYYMMDD, with the following constraints:
- YYYY: can be any number
- MM: from 01 to 12
- DD: from 01 to 31
"""
date_field = pp.Regex(
    '[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])').leaveWhitespace().setParseAction(
    lambda d: datetime.datetime.strptime(d[0], '%Y%m%d').date()).setName('Date Field')

"""
Time field (T).

Time follows the pattern HHMMSS, with the following constraints:
- HH: from 00 to 23
- MM: from 00 to 59
- SS: from 00 to 59
"""
time_field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]').leaveWhitespace().setParseAction(
    lambda t: datetime.datetime.strptime(t[0], '%H%M%S').time()).setName('Time Field')
