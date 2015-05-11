# -*- coding: utf-8 -*-

import pyparsing as pp

"""
CWR filename fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def alphanum_variable(min, max, name=None):
    """
    Creates the grammar for an alphanumeric code where the size ranges between two values.

    :param min: minimum size
    :param max: maximum size
    :param name: name for the field
    :return: grammar for an alphanumeric field of a variable size
    """

    if name is None:
        name = 'Alphanumeric Field'

    if min < 0:
        # Can't have negative min
        raise BaseException()
    if max < min:
        # Max can't be lower than min
        raise BaseException()

    field = pp.Word(pp.alphanums, min=min, max=max)

    # Parse action
    field.setParseAction(lambda s: s[0].strip())

    # White spaces are not removed
    field.leaveWhitespace()

    # Name
    field.setName(name)

    return field