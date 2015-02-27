# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp


"""
CWR fields grammar.

This stores grammar for parsing the CWR fields.

These fields are:
- Alphanumeric (A). Only allows non lowercase ASCII characters.
- Numeric field (N). Accepts integer or float values (these are handled as two different fields).
- Boolean (B). Accepts 'Y' or 'N'.
- Flag (F). Accepts 'Y', 'N' or 'U'.
- Date (D). Accepts numbers in the pattern YYYYMMDD.
- Time (T). Accepts numbers in the pattern HHMMSS.

Each of these fields is parsed into a value as follows:
- Alphanumeric (A). String with no heading or trailing white spaces.
- Numeric field (N). Integer or float.
- Boolean (B). Boolean.
- Flag (F). String
- Date (D). datetime.date.
- Time (T). datetime.time.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# BASIC FIELDS

"""
Alphanumeric (A) field.

Only non lowercase ASCII values are allowed.

The string contained in this field is parsed into a string with no heading or trailing white spaces.
"""


def alphanum(columns, compulsory=False):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    Alphanumeric fields accept ASCII characters, excluding lowercases.

    This can be a compulsory field, in which case the empty string is disallowed.

    :param columns: number of columns for this field
    :param compulsory: indicates if empty strings are disallowed
    :return: grammar for this Alphanumeric field
    """

    # The regular expression just forbids lowercase characters
    field = pp.Regex('([\x00-\x60]|[\x7B-\x7F]){' + str(columns) + '}')

    # Parse action
    field.setParseAction(lambda s: s[0].strip())

    if compulsory:
        # Compulsory field validation action
        field.addParseAction(lambda s: _check_not_empty(s[0]))

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName('Alphanumeric Field')

    return field


def _check_not_empty(string):
    """
    Checks that the string is not empty.

    If it is empty an exception is raised, stopping the validation.

    This is used for compulsory alphanumeric fields.

    :param string: the field value
    """
    string = string.strip()

    if len(string) == 0:
        raise pp.ParseException(string, "The field should not be empty")


"""
Numeric (N) field, integer type.

Only integers are allowed, and the string from the field will be parsed into an integer.

For the Numeric field allowing float values check the numeric_float method.
"""


def numeric(columns, compulsory=False):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified number of characters.

    This version only allows integers.

    This can be a compulsory field, in which case the zero is disallowed.

    :param columns: number of columns for this field
    :param compulsory: indicates if the zero is disallowed
    :return: grammar for the integer numeric field
    """

    # Only numbers are accepted
    field = pp.Word(pp.nums, exact=columns)

    # Parse action
    field.setParseAction(lambda n: int(n[0]))

    if compulsory:
        # Compulsory field validation action
        field.addParseAction(lambda s: _check_above_value_int(s[0], 0))

    # Name
    field.setName('Numeric Field')

    return field


def _check_above_value_int(string, minimum):
    """
    Checks that the number parsed from the string is above a minimum.

    This is used on compulsory numeric fields.

    If the value is not above the minimum an exception is thrown.

    :param string: the field value
    :param minimum: minimum value
    """
    value = int(string)

    if value <= minimum:
        message = "The Numeric Field value should be above %s" % minimum
        raise pp.ParseException(string, message)


"""
Numeric (N) field, float type.

Only float values are allowed, and the string from the field will be parsed into a float.

For the Numeric field allowing integer values check the numeric method.
"""


def numeric_float(columns, nums_int, compulsory=False):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified number of characters.

    This version only allows floats.

    As nothing in the string itself indicates how many of the characters are for the integer and the decimal sections,
    this should be specified with the nums_int parameter.

    This will indicate the number of characters, starting from the left, to be used for the integer value. All the
    remaining ones will be used for the decimal value.

    :param columns: number of columns for this field
    :param nums_int: characters, counting from the left, for the integer value
    :param compulsory: indicates if the zero is disallowed
    :return: grammar for the float numeric field
    """

    # Basic field
    field = pp.Word(pp.nums, exact=columns)

    # Parse action
    field.setParseAction(lambda n: _to_numeric_float(n[0], nums_int))

    if compulsory:
        # Compulsory field validation action
        field.addParseAction(lambda s: _check_above_value_float(s[0], 0))

    # Name
    field.setName('Numeric Field')

    return field


def _to_numeric_float(number, nums_int):
    """
    Transforms a string into a float.

    The nums_int parameter indicates the number of characters, starting from the left, to be used for the integer value. All the
    remaining ones will be used for the decimal value.

    :param number: string with the number
    :param nums_int: characters, counting from the left, for the integer value
    :return: a float created from the string
    """
    index_end = len(number) - nums_int
    return float(number[:nums_int] + '.' + number[index_end:])


def _check_above_value_float(string, minimum):
    """
    Checks that the number parsed from the string is above a minimum.

    This is used on compulsory numeric fields.

    If the value is not above the minimum an exception is thrown.

    :param string: the field value
    :param minimum: minimum value
    """
    value = float(string)

    if value <= minimum:
        message = "The Numeric Field value should be above %s" % minimum
        raise pp.ParseException(string, message)


"""
Boolean field (B).

Must be 'Y', for yes/true or 'N' for no/false.

This value will be parsed into a boolean type value.
"""


def boolean(compulsory=False):
    """
    Creates the grammar for a Boolean (F) field, accepting only 'Y' or 'N'

    :param compulsory: indicates if the field must be filled
    :return: grammar for the flag field
    """

    # Basic field
    field = pp.Combine(pp.Literal('Y') | pp.Literal('N'))

    # Parse action
    field.setParseAction(lambda b: _to_boolean(b[0]))

    # Name
    field.setName('Boolean Field')

    if not compulsory:
        optional = pp.Literal(' ')

        optional.setParseAction(lambda b: False)

        optional.setName('Boolean Field')

        # White spaces are not removed
        optional.leaveWhitespace()

        field = field | optional

        # Name
        field.setName('Boolean Field')

    return field


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
        raise pp.ParseException(string, msg='Is not a valid boolean value')

    return result


"""
Flag field (F).

Must be 'Y', for yes/true, 'N' for no/false or 'U' for unknown.

This string value will be just returned untouched.
"""


def flag(compulsory=False):
    """
    Creates the grammar for a Flag (F) field, accepting only 'Y', 'N' or 'U'.

    :param compulsory: indicates if the empty flag is disallowed
    :return: grammar for the flag field
    """

    # Basic field
    field = pp.Combine(pp.Word('YNU', exact=1))

    # Parse action
    field.setParseAction(lambda f: _to_flag(f[0]))

    # Name
    field.setName('Flag Field')

    if not compulsory:
        # If it is not compulsory the empty date is accepted
        optional = pp.Literal(' ')
        optional.setParseAction(pp.replaceWith(None))

        # Name
        optional.setName('Flag Field')

        field = field | optional

        # Name
        field.setName('Flag Field')

    field.leaveWhitespace()

    return field


def _to_flag(string):
    """
    Transforms a string into a flag value.

    If a value which is not 'Y', 'N' or 'U' is received, a ParseException is thrown.

    The received string is untouched, so if no exception is thrown the same value that is received will be
    the one returned.

    :param: string: the string to transform
    :return: the received string
    """

    if string not in ('Y', 'N', 'U'):
        raise pp.ParseException(string, msg='Is not a valid flag value')

    return string


"""
Date field (D).

Date follows the pattern YYYYMMDD, with the following constraints:
- YYYY: from 0001 to 9999
- MM: from 01 to 12
- DD: from 01 to 31

This string will be parsed into a datetime.date.
"""


def date(compulsory=False):
    """
    Creates the grammar for a Date (D) field, accepting only numbers in a certain pattern.

    The field can be compulsory, in which case the empty date, composed only of zeros, is disallowed.

    :param compulsory: indicates if the empty date is disallowed
    :return: grammar for the date field
    """

    # Basic field
    # This regex allows values from 00010101 to 99991231
    field = pp.Regex('[0-9][0-9](([0-9][1-9])|([1-9][0-9]))(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])')

    # Parse action
    field.setParseAction(lambda d: datetime.datetime.strptime(d[0], '%Y%m%d').date())

    # Name
    field.setName('Date Field')

    if not compulsory:
        # If it is not compulsory the empty date is accepted
        optional = pp.Regex('[0]{8}')
        optional.setParseAction(pp.replaceWith(None))

        # Name
        optional.setName('Date Field')

        field = field | optional

        # Name
        field.setName('Date Field')

    # White spaces are not removed
    field.leaveWhitespace()

    return field


"""
Time field (T).

Time follows the pattern HHMMSS, with the following constraints:
- HH: from 00 to 23
- MM: from 00 to 59
- SS: from 00 to 59

This string will be parsed into a datetime.time.
"""


def time(compulsory=False):
    """
    Creates the grammar for a Time (D) field, accepting only numbers in a certain pattern.

    :return: grammar for the date field
    """

    # Basic field
    # This regex allows values from 000000 to 235959
    field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]')

    # Parse action
    field.setParseAction(lambda t: datetime.datetime.strptime(t[0], '%H%M%S').time())

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName('Time Field')

    return field
