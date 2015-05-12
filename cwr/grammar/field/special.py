# -*- coding: utf-8 -*-

import datetime

import pyparsing as pp

from cwr.other import ISWCCode, IPIBaseNumber, VISAN, AVIKey
from cwr.grammar.field import basic
from data_commonworks.accessor import CWRConfiguration, CWRTables


"""
Grammar for special cases and other fields.

These are miscellany fields and nodes, such as line limiters, or the character encoding field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# GENERAL GRAMMAR

lineStart = pp.lineStart.suppress()
lineStart.setName("Start of line")

lineEnd = pp.lineEnd.suppress()
lineEnd.setName("End of line")

# CONCRETE CASES FIELDS


def ipi_base_number(name=None):
    """
    IPI Base Number field.

    An IPI Base Number code written on a field follows the Pattern C-NNNNNNNNN-M. This being:
    - C: header, a character.
    - N: numeric value.
    - M: control digit.

    So, for example, an IPI Base Number code field can contain I-000000229-7.

    :param name: name for the field
    :return: a parser for the IPI Base Number field
    """

    if name is None:
        name = 'IPI Base Number Field'

    # Separators are '-'
    separator = pp.Literal('-').suppress()
    separator = separator.setName('IPI Base Number Separator').setResultsName('separator')

    # Header is a digit in uppercase
    header = pp.Literal('I')
    header = header.setName('IPI Base Number Header').setResultsName('header')

    # ID code is composed of 9 numbers
    id_code = basic.numeric(9)
    id_code = id_code.setName('ID Code').setResultsName('id_code')
    id_code = id_code.setParseAction(lambda c: int(c[0]))

    # Check digit is a single number
    check_digit = pp.Regex('[0-9]')
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')
    check_digit = check_digit.setParseAction(lambda c: int(c[0]))

    # Digit followed separator, 9 numbers, separator and 1 number
    field = pp.Group(header + separator + id_code + separator + check_digit)

    # Parse action
    field.setParseAction(lambda c: _to_ipibasecode(c[0]))

    # Name
    field.setName(name)

    field_num = basic.numeric(13)
    field_num.setName(name)

    field = field | field_num

    # White spaces are not removed
    field.leaveWhitespace()

    return field.setResultsName('ipi_base_n')


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


def ipi_name_number(name=None):
    """
    IPI Name Number field.

    An IPI Name Number is composed of eleven digits.

    So, for example, an IPI Name Number code field can contain 00014107338.

    :param name: name for the field
    :return: a parser for the IPI Name Number field
    """

    if name is None:
        name = 'IPI Name Number Field'

    field = basic.numeric(11)

    field.setName(name)

    return field.setResultsName('ipi_name_n')


def iswc(name=None):
    """
    ISWC field.

    A ISWC code written on a field follows the Pattern TNNNNNNNNNC. This being:
    - T: header, it is always T.
    - N: numeric value.
    - C: control digit.

    So, for example, an ISWC code field can contain T0345246801.

    :param name: name for the field
    :return: a parser for the ISWC field
    """

    if name is None:
        name = 'ISWC Field'

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
    field = pp.Group(header + id_code + check_digit)

    # Parse action
    field.setParseAction(lambda c: _to_iswccode(c[0]))

    # Name
    field.setName(name)

    # White spaces are not removed
    field.leaveWhitespace()

    return field.setResultsName('iswc')


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


def percentage(columns, maximum=100, name=None):
    """
    Creates the grammar for a Numeric (N) field storing a percentage and accepting only the specified number of
    characters.

    It is possible to set the maximum allowed value. By default this is 100 (for 100%), and if modified it is
    expected to be reduced, not increased.

    The three first digits will be for the integer value.

    The columns can't be lower than 3.

    :param columns: number of columns for this field
    :param maximum: maximum allowed value
    :param name: name for the field
    :return: grammar for the float numeric field
    """

    if name is None:
        name = 'Percentage Field'

    if columns < 3:
        message = 'The values can not be lower than 3'
        raise pp.ParseException(message)

    field = basic.numeric_float(columns, 3)

    field.addParseAction(lambda v: _assert_is_percentage(v[0], maximum))

    field.setName(name)

    return field


def _assert_is_percentage(value, maximum=100):
    """
    Makes sure the received value is a percentage. Otherwise an exception is thrown.

    :param value: the value to check
    """

    if value < 0 or value > maximum:
        message = 'The value on a percentage field should be between 0 and %s' % maximum
        raise pp.ParseException(message)


def ean_13(name=None):
    """
    Creates the grammar for an EAN 13 code.

    These are the codes on thirteen digits barcodes.

    :param name: name for the field
    :return: grammar for an EAN 13 field
    """

    if name is None:
        name = 'EAN 13 Field'

    field = basic.numeric(13)

    field = field.setName(name)

    return field.setResultsName('ean_13')


def isrc(name=None):
    """
    Creates the grammar for an ISRC code.

    ISRC stands for International Standard Recording Code, which is the standard ISO 3901. This stores information
    identifying a particular recording.

    :param name: name for the field
    :return: grammar for an ISRC field
    """

    config = CWRTables()

    if name is None:
        name = 'ISRC Field'

    separator = pp.Literal('-')
    country = basic.lookup(config.get_data('isrc_country_code'))
    registrant = basic.alphanum(3)
    year = pp.Regex('[0-9]{2}')
    work_id = pp.Regex('[0-9]{2}')

    field = _isrc_short(name) | _isrc_long(name)

    field.setName(name)

    return field.setResultsName('isrc')


def _isrc_short(name=None):
    """
    Creates the grammar for a short ISRC code.

    ISRC stands for International Standard Recording Code, which is the standard ISO 3901. This stores information
    identifying a particular recording.

    This variant contains separator for the parts, and follows the pattern:
    CC-XXX-YY-NN

    Where each code means:
    - CC: country code
    - XXX: registrant
    - YY: year
    - NN: work id

    :param name: name for the field
    :return: grammar for an ISRC field
    """

    config = CWRTables()

    if name is None:
        name = 'ISRC Field'

    separator = pp.Literal('-')
    country = basic.lookup(config.get_data('isrc_country_code'))
    registrant = basic.alphanum(3)
    year = pp.Regex('[0-9]{2}')
    work_id = pp.Regex('[0-9]{2}')

    field = pp.Combine(country + separator + registrant + separator + year + separator + work_id)

    country.setName('ISO-2 Country Code')
    registrant.setName('Registrant')
    year.setName('Year')
    work_id.setName('Work ID')

    field.setName(name)

    return field.setResultsName('isrc')


def _isrc_long(name=None):
    """
    Creates the grammar for a short ISRC code.

    ISRC stands for International Standard Recording Code, which is the standard ISO 3901. This stores information
    identifying a particular recording.

    This variant contain no separator for the parts, and follows the pattern:
    CCXXXYYNNNNN

    Where each code means:
    - CC: country code
    - XXX: registrant
    - YY: year
    - NNNNN: work id

    :param name: name for the field
    :return: grammar for an ISRC field
    """

    config = CWRTables()

    if name is None:
        name = 'ISRC Field'

    separator = pp.Literal('-')
    country = basic.lookup(config.get_data('isrc_country_code'))
    registrant = basic.alphanum(3)
    year = pp.Regex('[0-9]{2}')
    work_id = pp.Regex('[0-9]{5}')

    field = pp.Combine(country + registrant + year + work_id)

    country.setName('ISO-2 Country Code')
    registrant.setName('Registrant')
    year.setName('Year')
    work_id.setName('Work ID')

    field.setName(name)

    return field.setResultsName('isrc')


def visan(name=None):
    """
    Creates the grammar for a V-ISAN code.

    This is a variation on the ISAN (International Standard Audiovisual Number)

    :param name: name for the field
    :return: grammar for an ISRC field
    """

    if name is None:
        name = 'V-ISAN Field'

    version = basic.numeric(8)
    version = version.setName('Version').setResultsName('version')

    isan = basic.numeric(12)
    isan = isan.setName('ISAN').setResultsName('isan')

    episode = basic.numeric(4)
    episode = episode.setName('Episode').setResultsName('episode')

    check_digit = basic.numeric(1)
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')

    field = pp.Group(version + isan + episode + check_digit)

    field.setParseAction(lambda v: _to_visan(v[0]))

    field.setName(name)

    return field.setResultsName('visan')


def _to_visan(parsed):
    """
    Transforms the data from a V-ISAN field into a VISAN instance.

    :param parsed: the data parsed from a V-ISAN field
    :return: a VISAN instance created from the data
    """
    return VISAN(parsed.version, parsed.isan, parsed.episode, parsed.check_digit)


def audio_visual_key(name=None):
    """
    Creates the grammar for an Audio Visual Key code.

    This is a variation on the ISAN (International Standard Audiovisual Number)

    :param name: name for the field
    :return: grammar for an ISRC field
    """

    if name is None:
        name = 'AVI Field'

    society_code = basic.numeric(3)
    society_code = society_code.setName('Society Code').setResultsName('society_code')

    av_number = basic.alphanum(15)
    field_empty = pp.Regex('[ ]{15}')
    field_empty.setParseAction(pp.replaceWith(''))
    av_number = av_number | field_empty
    av_number = av_number.setName('Audio-Visual Number').setResultsName('av_number')

    field = pp.Group(society_code + av_number)

    field.setParseAction(lambda v: _to_avi(v[0]))

    field = field.setName(name)

    return field.setResultsName('audio_visual_key')


def _to_avi(parsed):
    """
    Transforms the data from an AVI field into an AVIKey instance.

    :param parsed: the data parsed from an AVI field
    :return: an AVIKey instance created from the data
    """
    return AVIKey(parsed.society_code, parsed.av_number)


def date_time(name=None):
    """
    Creates the grammar for a date and time field, which is a combination of the Date (D) and Time or Duration field (T)
    .

    This field requires first a Date, and then a Time, without any space in between.

    :param name: name for the field
    :return: grammar for a Date and Time field
    """
    if name is None:
        name = 'Date and Time Field'

    date = basic.date('Date')
    time = basic.time('Time')

    date = date.setResultsName('date')
    time = time.setResultsName('time')

    field = pp.Group(date + time)

    field.setParseAction(lambda d: _combine_date_time(d[0]))

    field.setName(name)

    return field.setResultsName('date_time')


def _combine_date_time(data):
    """
    Combines the received date and time.

    :param data: date and time to combine
    :return: the date and time combined
    """
    return datetime.datetime.combine(data.date, data.time)