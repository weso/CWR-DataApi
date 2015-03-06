# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.other import ISWCCode, IPIBaseNumber, VISAN, AVIKey
from cwr.grammar.field import basic
from data.accessor import CWRConfiguration


"""
Grammar for special cases and other fields.

These are miscellany fields and nodes, such as line limiters, or the character encoding field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# GENERAL GRAMMAR

lineStart = pp.lineStart.suppress()
lineStart.setName("Start of line")

lineEnd = pp.lineEnd.suppress()
lineEnd.setName("End of line")

# CONCRETE CASES FIELDS


def ip_id(compulsory=False):
    """
    IP Number field.

    On the CWR standard an Interested Party can have an alphanumeric ID of up to 9 digits.

    :return: a parser for the IP Number field
    """
    field = basic.alphanum(_config.field_size('special', 'ip_id'), compulsory)
    field = field.setName('Interested Party Number Field').setResultsName('ip_id')

    return field


def ipi_base_number(compulsory=False):
    """
    IPI Base Number field.

    An IPI Base Number code written on a field follows the Pattern C-NNNNNNNNN-M. This being:
    - C: header, a character.
    - N: numeric value.
    - M: control digit.

    So, for example, an IPI Base Number code field can contain I-000000229-7.

    :param compulsory: indicates if the empty string is disallowed
    :return: a parser for the IPI Base Number field
    """

    # Separators are '-'
    separator = pp.Literal('-').suppress()
    separator = separator.setName('IPI Base Number Separator').setResultsName('separator')

    # Header is a digit in uppercase
    header = pp.Literal('I')
    header = header.setName('IPI Base Number Header').setResultsName('header')

    # ID code is composed of 9 numbers
    id_code = basic.numeric(9, compulsory=True)
    id_code = id_code.setName('ID Code').setResultsName('id_code')
    id_code = id_code.setParseAction(lambda c: int(c[0]))

    # Check digit is a single number
    check_digit = pp.Regex('[0-9]')
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')
    check_digit = check_digit.setParseAction(lambda c: int(c[0]))

    # Digit followed separator, 9 numbers, separator and 1 number
    field = header + separator + id_code + separator + check_digit

    # Parse action
    field.setParseAction(lambda c: _to_ipibasecode(c))

    # Name
    field.setName('IPI Base Number Field')

    field_num = basic.numeric(13, compulsory=compulsory)
    field_num.setName('IPI Base Number Field')

    field = field | field_num

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{13}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('IPI Base Number Field')

        field = empty | field
        # Name
        field.setName('ISWC Field')

    # White spaces are not removed
    field.leaveWhitespace()

    field = field.setResultsName('ipi_base')

    return field


def _to_ipibasecode(code):
    """
    Transforms the result of parsing an IPI Base Number code string into a IPIBaseNumber instance.

    :param code: the parsed code
    :return: a IPIBaseNumber instance
    """

    if code:
        return IPIBaseNumber(code.header, code.id_code, code.check_digit)
    else:
        return code


def ipi_name_number(compulsory=False):
    """
    IPI Name Number field.

    An IPI Name Number is composed of eleven digits.

    So, for example, an IPI Name Number code field can contain 00014107338.

    :param compulsory: indicates if the empty string is disallowed
    :return: a parser for the IPI Name Number field
    """
    field = basic.numeric(11, compulsory=compulsory)

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{11}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('IPI Base Number Field')

        field = empty | field
        # Name
        field.setName('IPI Name Number Field')

    field = field.setName('IPI Name Number Field').setResultsName('ipi_name')

    return field


def iswc(compulsory=False):
    """
    ISWC field.

    A ISWC code written on a field follows the Pattern TNNNNNNNNNC. This being:
    - T: header, it is always T.
    - N: numeric value.
    - C: control digit.

    So, for example, an ISWC code field can contain T0345246801.

    :param compulsory: indicates if the empty string is disallowed
    :return: a parser for the ISWC field
    """

    # Header is always T
    header = pp.Literal('T').suppress()
    header = header.setName('ISWC Header').setResultsName('header')

    # ID code is composed of 9 numbers
    id_code = basic.numeric(9, compulsory=True)
    id_code = id_code.setName('ID Code').setResultsName('id_code')

    # Check digit is a single number
    check_digit = basic.numeric(1, compulsory=True)
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')

    # T followed by 10 numbers
    field = pp.Combine(header + id_code + check_digit)

    # Parse action
    field.setParseAction(lambda c: _to_iswccode(c))

    # Name
    field.setName('ISWC Field').setResultsName('iswc')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{11}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('ISWC Field')

        field = empty | field
        # Name
        field.setName('ISWC Field')

    # White spaces are not removed
    field.leaveWhitespace()

    return field


def _to_iswccode(code):
    """
    Transforms the result of parsing a ISWC code string into a ISWCCode instance.

    :param code: the parsed code
    :return: a ISWCCode instance
    """
    if code:
        return ISWCCode(code.id_code, code.check_digit)
    else:
        return code


def percentage(columns, maximum=100, compulsory=False):
    """
    Creates the grammar for a Numeric (N) field storing a percentage and accepting only the specified number of
    characters.

    The three first digits will be for the integer value.

    The columns can't be lower than 3.

    :param columns: number of columns for this field
    :param compulsory: indicates if the zero is disallowed
    :return: grammar for the float numeric field
    """

    if columns < 3:
        raise BaseException()

    field = basic.numeric_float(columns, 3, compulsory)

    field.addParseAction(lambda v: _assert_is_percentage(v[0], maximum))

    field.setName('Percentage Field')

    return field


def _assert_is_percentage(value, maximum=100):
    """
    Makes sure the received value is a percentage. Otherwise an exception is thrown.

    :param value: the value to check
    """

    if value < 0 or value > maximum:
        raise pp.ParseException('', 'The value on a percentage field should be between 0 and 100')


def shares(maximum=100, compulsory=False):
    """
    Creates the grammar for a shares field.

    Shares are a numeric field composed of five digits, three are for the integer value, and three are for the
    decimal one.

    They range from 00000, for 0%, to 100000, for 100%.

    :param maximum: the maximum value for the shares
    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for the society ID field
    """
    field = percentage(_config.field_size('special', 'shares'), maximum=maximum, compulsory=compulsory)
    field.setName('Shares Field')

    return field


def blank(columns):
    """
    Creates the grammar for a group of blank spaces.

    These are for constant empty strings which should be ignored, as they are used just as fillers.

    :param columns: the number of blank spaces
    :return: grammar for a group of blank spaces
    """
    field = pp.Regex('[ ]{' + str(columns) + '}')
    field.leaveWhitespace()
    field.suppress()

    return field


def ean_13(compulsory=False):
    """
    Creates the grammar for an EAN 13 code.

    These are the codes on thirteen digits barcodes.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for an EAN 13 field
    """
    field = basic.numeric(13, compulsory)

    field = field.setName('Shares Field')

    return field.setResultsName('ean_13')


def isrc(compulsory=False):
    """
    Creates the grammar for an ISRC code.

    ISRC stands for International Standard Recording Code, which is the standard ISO 3901. This stores information
    identifying a particular recording.

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for an ISRC field
    """
    separator = pp.Literal('-')
    country = basic.alphanum(2)
    registrant = basic.alphanum(3)
    year = pp.Regex('[0-9]{2}')
    work_id = pp.Regex('[0-9]{2}')

    field = pp.Combine(country + separator + registrant + separator + year + separator + work_id)

    field = field.setName('ISRC Field').setResultsName('isrc')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{12}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('ISRC Field')
        empty.leaveWhitespace()

        field = empty | field
        # Name
        field.setName('ISRC Field')

    return field


def visan(compulsory=False):
    """
    Creates the grammar for a V-ISAN code.

    This is a variation on the ISAN (International Standard Audiovisual Number)

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for an ISRC field
    """
    version = basic.numeric(8)
    version = version.setName('Version').setResultsName('version')

    isan = basic.numeric(12)
    isan = isan.setName('ISAN').setResultsName('isan')

    episode = basic.numeric(4)
    episode = episode.setName('Episode').setResultsName('episode')

    check_digit = basic.numeric(1)
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')

    field = pp.Combine(version + isan + episode + check_digit)

    field.setParseAction(lambda v: _to_visan(v[0]))

    field = field.setName('V-ISAN Field').setResultsName('visan')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{25}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('V-ISAN Field')

        field = empty | field
        # Name
        field.setName('V-ISAN Field')

    return field


def _to_visan(parsed):
    """
    Transforms the data from a V-ISAN field into a VISAN instance.

    :param parsed: the data parsed from a V-ISAN field
    :return: a VISAN instance created from the data
    """
    return VISAN(parsed.version, parsed.isan, parsed.episode, parsed.check_digit)


def avi(compulsory=False):
    """
    Creates the grammar for an AVI code.

    This is a variation on the ISAN (International Standard Audiovisual Number)

    :param compulsory: indicates if the empty string is disallowed
    :return: grammar for an ISRC field
    """
    society_code = basic.numeric(3)
    society_code = society_code.setName('Society Code').setResultsName('society_code')

    av_number = basic.alphanum(15)
    av_number = av_number.setName('Audio-Visual Number').setResultsName('av_number')

    field = pp.Combine(society_code + av_number)

    field.setParseAction(lambda v: _to_avi(v[0]))

    field = field.setName('AVI Field').setResultsName('avi')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{18}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('AVI Field')

        field = empty | field
        # Name
        field.setName('AVI Field')

    return field


def _to_avi(parsed):
    """
    Transforms the data from an AVI field into an AVIKey instance.

    :param parsed: the data parsed from an AVI field
    :return: an AVIKey instance created from the data
    """
    return AVIKey(parsed.society_code, parsed.av_number)