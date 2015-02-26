# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRTables
from cwr.other import ISWCCode


"""
Grammar for special cases and other fields.

These are miscellany fields and nodes, such as line limiters, or the character encoding field.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()

# GENERAL GRAMMAR

lineStart = pp.lineStart.suppress()
lineStart.setName("Start of line")

lineEnd = pp.lineEnd.suppress()
lineEnd.setName("End of line")

# CONCRETE CASES FIELDS

"""
Characters sets should be one of the CWR list or the Unicode UTF-8 table.

The Unicode UTF-8 codes are those with up to 16 or 21 bits.
"""


def char_code(columns):
    """
    Character set code.

    This accepts one of the character sets allowed on the file.

    :param columns: number of columns for this field
    :return: a parser for the character set field
    """
    char_sets = None
    for char_set in _tables.character_sets():
        regex = '[ ]{' + str(15 - len(char_set)) + '}' + char_set
        if char_sets is None:
            char_sets = regex
        else:
            char_sets += '|' + regex

    # Accepted sets
    _character_sets = pp.Regex(char_sets)
    _unicode_1_16b = pp.Regex('U\+0[0-8,A-F]{3}[ ]{' + str(columns - 6) + '}')
    _unicode_2_21b = pp.Regex('U\+0[0-8,A-F]{4}[ ]{' + str(columns - 7) + '}')

    # Basic field
    field = (_character_sets | _unicode_1_16b | _unicode_2_21b)

    # Parse action
    field = field.setParseAction(lambda s: s[0].strip())

    # Name
    field.setName('Char Code Field (' + str(columns) + ' columns)')

    return field


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
    id_code = pp.Regex('[0-9]{9}')
    id_code = id_code.setName('ID Code').setResultsName('id_code')
    id_code = id_code.setParseAction(lambda c: int(c[0]))

    # Check digit is a single number
    check_digit = pp.Regex('[0-9]')
    check_digit = check_digit.setName('Check Digit').setResultsName('check_digit')
    check_digit = check_digit.setParseAction(lambda c: int(c[0]))

    # T followed by 10 numbers
    iswc = pp.Combine(header + id_code + check_digit)

    # Parse action
    iswc.setParseAction(lambda c: _to_iswccode(c))

    # Name
    iswc.setName('ISWC Field')

    if not compulsory:
        # If it is not compulsory then it can be set as empty
        empty = pp.Regex('[ ]{11}')
        empty.setParseAction(pp.replaceWith(None))
        empty.setName('ISWC Field')

        iswc = empty | iswc
        # Name
        iswc.setName('ISWC Field')

    # White spaces are not removed
    iswc.leaveWhitespace()

    return iswc


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