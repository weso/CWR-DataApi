# -*- coding: utf-8 -*-

from cwr.grammar.factory.common import FieldBuilder
from cwr.grammar.field import basic


"""
CWR fields grammar builders.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class AlphanumBuilder(FieldBuilder):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding lowercases. If the extended flag is set to
    True, then non-ASCII characters are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(AlphanumBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.alphanum(columns, name, True, extended=False)


class ExtendedAlphanumBuilder(FieldBuilder):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding lowercases. If the extended flag is set to
    True, then non-ASCII characters are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(ExtendedAlphanumBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.alphanum(columns, name, True, extended=True)


class NumericBuilder(FieldBuilder):
    def __init__(self):
        super(NumericBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.numeric(columns, name, True)


class BooleanBuilder(FieldBuilder):
    def __init__(self):
        super(BooleanBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.boolean(name, True)


class FlagBuilder(FieldBuilder):
    def __init__(self):
        super(FlagBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.flag(name, True)


class DateBuilder(FieldBuilder):
    def __init__(self):
        super(DateBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.date(name, True)


class TimeBuilder(FieldBuilder):
    def __init__(self):
        super(TimeBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.time(name, True)


class BlankBuilder(FieldBuilder):
    def __init__(self):
        super(BlankBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.blank(columns, name)


class LookupBuilder(FieldBuilder):
    def __init__(self):
        super(LookupBuilder, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.lookup(values, columns, name, True)