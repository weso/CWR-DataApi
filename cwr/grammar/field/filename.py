# -*- coding: utf-8 -*-

import pyparsing as pp

from cwr.grammar.field.basic import numeric, lookup
from config_cwr.accessor import CWRConfiguration

"""
CWR filename fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def alphanum_variable(min_size, max_size, name=None):
    """
    Creates the grammar for an alphanumeric code where the size ranges between
    two values.

    :param min_size: minimum size
    :param max_size: maximum size
    :param name: name for the field
    :return: grammar for an alphanumeric field of a variable size
    """

    if name is None:
        name = 'Alphanumeric Field'

    if min_size < 0:
        # Can't have negative min
        raise BaseException()
    if max_size < min_size:
        # Max can't be lower than min
        raise BaseException()

    field = pp.Word(pp.alphanums, min=min_size, max=max_size)

    # Parse action
    field.setParseAction(lambda s: s[0].strip())

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName(name)

    return field


def year(columns, name=None):
    """
    Creates the grammar for a field containing a year.

    :param columns: the number of columns for the year
    :param name: the name of the field
    :return:
    """

    if columns < 0:
        # Can't have negative size
        raise BaseException()

    field = numeric(columns, name)

    # Parse action
    field.addParseAction(_to_year)

    return field


def filename_version(values, name=None):
    field = lookup(values, name)

    default_version = CWRConfiguration().default_version()

    # Parse action
    field.addParseAction(lambda n: default_version)

    return field


def _to_year(parsed):
    """
    Transforms the parsed two digits integer into a valid year value.

    :param parsed: the parsed value
    """
    return 2000 + parsed[0]
