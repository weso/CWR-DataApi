# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr.grammar.field import basic


"""
CWR fields grammar adapters.

These classes allow the factories to create rules in an homogeneous way.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FieldAdapter(object):
    """
    Instances of this class generate field rules.

    This serves as an adapter so the different field rules use the same parameters.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_field(self, name=None, columns=None, values=None):
        """
        Generates the rules for the field, applying the received parameters.

        :param name: the name of the field
        :param columns: number of columns
        :param values: allowed values for the field
        :return: the rules for the field
        """
        raise NotImplementedError("The get_field method is not implemented")


class AlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding lowercases. If the extended flag is set to
    True, then non-ASCII characters are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(AlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.alphanum(columns, name, True, extended=False)


class ExtendedAlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding lowercases. If the extended flag is set to
    True, then non-ASCII characters are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(ExtendedAlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.alphanum(columns, name, True, extended=True)


class NumericAdapter(FieldAdapter):
    def __init__(self):
        super(NumericAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.numeric(columns, name, True)


class BooleanAdapter(FieldAdapter):
    def __init__(self):
        super(BooleanAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.boolean(name, True)


class FlagAdapter(FieldAdapter):
    def __init__(self):
        super(FlagAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.flag(name, True)


class DateAdapter(FieldAdapter):
    def __init__(self):
        super(DateAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.date(name, True)


class TimeAdapter(FieldAdapter):
    def __init__(self):
        super(TimeAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.time(name, True)


class BlankAdapter(FieldAdapter):
    def __init__(self):
        super(BlankAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.blank(columns, name)


class LookupAdapter(FieldAdapter):
    def __init__(self):
        super(LookupAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.lookup(values, columns, name, True)