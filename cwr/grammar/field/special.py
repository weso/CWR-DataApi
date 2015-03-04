# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.other import ISWCCode, IPIBaseNumber, VISAN, AVIKey
from cwr.grammar.field import basic


"""
Grammar for special cases and other fields.

These are miscellany fields and nodes, such as line limiters, or the character encoding field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

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
    ip_id_field = basic.alphanum(9, compulsory)
    ip_id_field = ip_id_field.setName('Interested Party Number Field').setResultsName('ip_id')

    return ip_id_field


def ipi_base_number(compulsory=False):
    """
    IPI Base Number field.

    An IPI Base Number code written on a field follows the Pattern C-NNNNNNNNN-M. This being:
    - C: header, a character.
    - N: numeric value.
    - M: control digit.

    So, for example, an IPI Base Number code field can contain I-000000229-7.

    :return: a parser for the IPI Base Number field
    """

    # Separators are '-'
    separator = pp.Literal('-').suppress()
    separator = separator.setName('IPI Base Number Separator').setResultsName('separator')

    # Header is a digit in uppercase
    header = pp.Literal('I')
    header = header.setName('IPI Base Number Header').setResultsName('header')

    # ID code is composed of 9 numbers
    id_code = pp.Regex('[0-9]{9}')
    id_code = id_code.setName('ID Code').setResultsName('id_code')
    id_code = id_code.setParseAction(lambda c: int(c[0]))

    # Check digit is a single number
    check_digit = pp.Regex('[0-9]')
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')
    check_digit = check_digit.setParseAction(lambda c: int(c[0]))

    # Digit followed separator, 9 numbers, separator and 1 number
    ipi_base_field = header + separator + id_code + separator + check_digit

    # Parse action
    ipi_base_field.setParseAction(lambda c: _to_ipibasecode(c))

    # Name
    ipi_base_field.setName('IPI Base Number Field')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{13}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('IPI Base Number Field')

        ipi_base_field = empty | ipi_base_field
        # Name
        ipi_base_field.setName('ISWC Field')

    # White spaces are not removed
    ipi_base_field.leaveWhitespace()

    ipi_base_field = ipi_base_field.setResultsName('ipi_base')

    return ipi_base_field


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

    :return: a parser for the IPI Name Number field
    """
    ipi_name_number_field = basic.numeric(11, compulsory=compulsory)

    ipi_name_number_field = ipi_name_number_field.setName('IPI Name Number Field').setResultsName('ipi_name')

    return ipi_name_number_field


def iswc(compulsory=False):
    """
    ISWC field.

    A ISWC code written on a field follows the Pattern TNNNNNNNNNC. This being:
    - T: header, it is always T.
    - N: numeric value.
    - C: control digit.

    So, for example, an ISWC code field can contain T0345246801.

    :return: a parser for the ISWC field
    """

    # Header is always T
    header = pp.Literal('T').suppress()
    header = header.setName('ISWC Header').setResultsName('header')

    # ID code is composed of 9 numbers
    id_code = basic.numeric(9)
    id_code = id_code.setName('ID Code').setResultsName('id_code')

    # Check digit is a single number
    check_digit = basic.numeric(1)
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')

    # T followed by 10 numbers
    iswc_field = pp.Combine(header + id_code + check_digit)

    # Parse action
    iswc_field.setParseAction(lambda c: _to_iswccode(c))

    # Name
    iswc_field.setName('ISWC Field').setResultsName('iswc')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{11}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('ISWC Field')

        iswc_field = empty | iswc_field
        # Name
        iswc_field.setName('ISWC Field')

    # White spaces are not removed
    iswc_field.leaveWhitespace()

    return iswc_field


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


def percentage(columns, max=100, compulsory=False):
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

    percentage_field = basic.numeric_float(columns, 3, compulsory)

    percentage_field.addParseAction(lambda v: _assert_is_percentage(v[0], max))

    percentage_field.setName('Percentage Field')

    return percentage_field


def _assert_is_percentage(value, max=100):
    """
    Makes sure the received value is a percentage. Otherwise an exception is thrown.

    :param value: the value to check
    """

    if value < 0 or value > max:
        raise pp.ParseException('', 'The value on a percentage field should be between 0 and 100')


def shares(max=100, compulsory=False):
    """
    Creates the grammar for a shares field.

    Shares are a numeric field composed of five digits, three are for the integer value, and three are for the
    decimal one.

    They range from 00000, for 0%, to 100000, for 100%.

    :return: grammar for the society ID field
    """
    shares_field = percentage(5, max=max, compulsory=compulsory)
    shares_field.setName('Shares Field')

    return shares_field


def blank(columns):
    """
    Creates the grammar for a group of blank spaces.

    These are for constant empty strings which should be ignored.

    :param columns: the number of blank spaces
    :return: grammar for a group of blank spaces
    """
    filler = pp.Regex('[ ]{' + str(columns) + '}')
    filler.leaveWhitespace()
    filler.suppress()

    return filler


def ean_13(compulsory=False):
    ean_13_field = basic.numeric(13, compulsory)

    ean_13_field = ean_13_field.setName('Shares Field').setResultsName('ean_13')

    return ean_13_field


def isrc(compulsory=False):
    country = basic.alphanum(2)
    registrant = basic.alphanum(3)
    year = basic.numeric(2)
    work_id = basic.numeric(5)

    isrc_field = pp.Combine(country + registrant + year + work_id)

    isrc_field = isrc_field.setName('ISRC Field').setResultsName('isrc')

    return isrc_field


def visan(compulsory=False):
    version = basic.numeric(8)
    version = version.setName('Version').setResultsName('version')

    isan = basic.numeric(12)
    isan = isan.setName('ISAN').setResultsName('isan')

    episode = basic.numeric(4)
    episode = episode.setName('Episode').setResultsName('episode')

    check_digit = basic.numeric(1)
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')

    visan_field = pp.Combine(version + isan + episode + check_digit)

    visan_field.setParseAction(lambda v: _to_visan(v[0]))

    visan_field = visan_field.setName('V-ISAN Field').setResultsName('visan')

    return visan_field


def _to_visan(parsed):
    return VISAN(parsed.version, parsed.isan, parsed.episode, parsed.check_digit)


def avi(compulsory=False):
    society_code = basic.numeric(3)
    society_code = society_code.setName('Society Code').setResultsName('society_code')

    av_number = basic.alphanum(15)
    av_number = av_number.setName('Audio-Visual Number').setResultsName('av_number')

    avi_field = pp.Combine(society_code + av_number)

    avi_field.setParseAction(lambda v: _to_avi(v[0]))

    avi_field = avi_field.setName('AVI Field').setResultsName('avi')

    return avi_field


def _to_avi(parsed):
    return AVIKey(parsed.society_code, parsed.av_number)