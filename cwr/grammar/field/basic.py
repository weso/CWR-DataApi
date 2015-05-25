# -*- coding: utf-8 -*-

import datetime

import pyparsing as pp
from pyparsing import ParseResults

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

Additionally, other fields used on the CWR files, but not defined as basic fields, are included:
- Blank. A line composed only of whitespaces.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# BASIC FIELDS

"""
Alphanumeric (A) field.

Only non lowercase ASCII values are allowed.

The string contained in this field is parsed into a string with no heading or trailing white spaces.
"""


def alphanum(columns, name=None, extended=False):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding lowercases. If the extended flag is set to
    True, then non-ASCII characters are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is disallowed.

    The text will be stripped of heading and trailing whitespaces.

    :param columns: number of columns for this field
    :param name: name for the field
    :param extended: indicates if this is the exceptional case where non-ASCII are allowed
    :return: grammar for this Alphanumeric field
    """

    if name is None:
        name = 'Alphanumeric Field'

    if columns < 0:
        # Can't be empty or have negative size
        raise BaseException()

    # Checks if non-ASCII characters are allowed
    if not extended:
        # The regular expression just forbids lowercase characters
        field = pp.Regex('([\x00-\x60]|[\x7B-\x7F]){' + str(columns) + '}')
    else:
        # The regular expression forbids lowercase characters but allows non-ASCII characters
        field = pp.Regex('([\x00-\x60]|[\x7B-\x7F]|[^\x00-\x7F]){' + str(columns) + '}')

    # Parse action
    field.setParseAction(lambda s: s[0].strip())

    # Compulsory field validation action
    if columns > 0:
        field.addParseAction(lambda s: _check_not_empty(s[0]))

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName(name)

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
        message = 'The string should not be empty'
        raise pp.ParseException(message)


"""
Numeric (N) field, integer type.

Only integers are allowed, and the string from the field will be parsed into an integer.

For the Numeric field allowing float values check the numeric_float method.
"""


def numeric(columns, name=None):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified number of characters.

    This version only allows integers.

    :param columns: number of columns for this field
    :param name: name for the field
    :return: grammar for the integer numeric field
    """

    if name is None:
        name = 'Numeric Field'

    if columns <= 0:
        # Can't be empty or have negative size
        raise BaseException()

    # Only numbers are accepted
    field = pp.Regex('[0-9]{' + str(columns) + '}')

    # Parse action
    field.setParseAction(lambda n: _to_int(n))
    field.leaveWhitespace()

    # Name
    field.setName(name)

    return field


def _to_int(parsed):
    """
    Transforms the received parsed value into an integer.

    :param parsed: the parsed value
    :return: an integer created from the value
    """
    if len(parsed) > 0:
        return int(parsed[0])
    else:
        return None


"""
Numeric (N) field, float type.

Only float values are allowed, and the string from the field will be parsed into a float.

For the Numeric field allowing integer values check the numeric method.
"""


def numeric_float(columns, nums_int, name=None):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified number of characters.

    This version only allows floats.

    As nothing in the string itself indicates how many of the characters are for the integer and the decimal sections,
    this should be specified with the nums_int parameter.

    This will indicate the number of characters, starting from the left, to be used for the integer value. All the
    remaining ones will be used for the decimal value.

    :param columns: number of columns for this field
    :param name: name for the field
    :param nums_int: characters, counting from the left, for the integer value
    :return: grammar for the float numeric field
    """

    if name is None:
        name = 'Numeric Field'

    if columns <= 0:
        # Can't be empty or have negative size
        raise BaseException('Number of columns should be positive')

    if nums_int < 0:
        # Integer columns can't have negative size
        raise BaseException('Number of integer values should be positive or zero')

    if columns < nums_int:
        # There are more integer numbers than columns
        message = 'The number of columns is %s and should be higher or equal than the integers: %s' % (
            columns, nums_int)
        raise BaseException(message)

    # Basic field
    field = pp.Word(pp.nums, exact=columns)

    # Parse action
    field.setParseAction(lambda n: _to_numeric_float(n[0], nums_int))

    # Compulsory field validation action
    field.addParseAction(lambda s: _check_above_value_float(s[0], 0))

    # Name
    field.setName(name)

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
    return float(number[:nums_int] + '.' + number[-index_end:])


def _check_above_value_float(string, minimum):
    """
    Checks that the number parsed from the string is above a minimum.

    This is used on compulsory numeric fields.

    If the value is not above the minimum an exception is thrown.

    :param string: the field value
    :param minimum: minimum value
    """
    value = float(string)

    if value < minimum:
        message = 'The Numeric Field value should be above %s' % minimum
        raise pp.ParseException(message)


"""
Boolean field (B).

Must be 'Y', for yes/true or 'N' for no/false.

This value will be parsed into a boolean type value.
"""


def boolean(name=None):
    """
    Creates the grammar for a Boolean (B) field, accepting only 'Y' or 'N'

    :param name: name for the field
    :return: grammar for the flag field
    """

    if name is None:
        name = 'Boolean Field'

    # Basic field
    field = pp.Combine(pp.Literal('Y') | pp.Literal('N'))

    # Parse action
    field.setParseAction(lambda b: _to_boolean(b[0]))

    # Name
    field.setName(name)

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


def flag(name=None):
    """
    Creates the grammar for a Flag (F) field, accepting only 'Y', 'N' or 'U'.

    :param name: name for the field
    :return: grammar for the flag field
    """

    if name is None:
        name = 'Flag Field'

    # Basic field
    field = pp.Combine(pp.Word('YNU', exact=1))

    # Parse action
    field.setParseAction(lambda f: _to_flag(f[0]))

    # Name
    field.setName(name)

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


def date(name=None):
    """
    Creates the grammar for a Date (D) field, accepting only numbers in a certain pattern.

    :param name: name for the field
    :return: grammar for the date field
    """

    if name is None:
        name = 'Date Field'

    # Basic field
    # This regex allows values from 00000101 to 99991231
    field = pp.Regex('[0-9][0-9][0-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])')

    # Parse action
    field.setParseAction(lambda d: datetime.datetime.strptime(d[0], '%Y%m%d').date())

    # Name
    field.setName(name)

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


def time(name=None):
    """
    Creates the grammar for a Time or Duration (T) field, accepting only numbers in a certain pattern.

    :param name: name for the field
    :return: grammar for the date field
    """

    if name is None:
        name = 'Time Field'

    # Basic field
    # This regex allows values from 000000 to 235959
    field = pp.Regex('(0[0-9]|1[0-9]|2[0-3])[0-5][0-9][0-5][0-9]')

    # Parse action
    field.setParseAction(lambda t: datetime.datetime.strptime(t[0], '%H%M%S').time())

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName(name)

    return field


"""
Lookup field (L).

This accepts only values from a table or list.
"""


def lookup(values, name=None):
    """
    Creates the grammar for a Lookup (L) field, accepting only values from a list.

    Like in the Alphanumeric field, the result will be stripped of all heading and trailing whitespaces.

    :param values: values allowed
    :param name: name for the field
    :return: grammar for the lookup field
    """
    if name is None:
        name = 'Lookup Field'

    if values is None:
        raise ValueError('The values can no be None')

    # TODO: This should not be needed, it is just a patch. Fix this.
    if isinstance(values, ParseResults):
        values = values.asList()

    # Only the specified values are allowed
    lookup_field = pp.oneOf(values)

    lookup_field.setName(name)

    lookup_field.setParseAction(lambda s: s[0].strip())

    lookup_field.leaveWhitespace()

    return lookup_field


"""
Blank field.

This accepts only a line composed of whitespaces.
"""


def blank(columns=1, name=None):
    """
    Creates the grammar for a blank field.

    These are for constant empty strings which should be ignored, as they are used just as fillers.

    :param columns: number of columns, which is the required number of whitespaces
    :param name: name for the field
    :return: grammar for the blank field
    """
    if name is None:
        name = 'Blank Field'

    field = pp.Regex('[ ]{' + str(columns) + '}')
    field.leaveWhitespace()
    field.suppress()

    field.setName(name)

    return field
