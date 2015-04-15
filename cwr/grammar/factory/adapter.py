# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

import pyparsing as pp

from cwr.grammar.field import basic, special, table, filename

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

    def wrap_as_optional(self, field, name, columns):
        """
        Adds a wrapper rule to the field to accept empty strings.

        This empty string should be of the same size as the columns parameter. One smaller or bigger will be rejected.

        This wrapper will return None if the field is empty.

        :param field: the field to wrap
        :param name: name of the field
        :param columns: number of columns it takes
        :return: the field with an additional rule to allow empty strings
        """
        # Regular expression accepting as many whitespaces as columns
        field_empty = pp.Regex('[ ]{' + str(columns) + '}')

        field_empty.setName(name)

        # Whitespaces are not removed
        field_empty.leaveWhitespace()

        # None is returned by this rule
        field_empty.setParseAction(pp.replaceWith(None))

        field_empty = field_empty.setResultsName(field.resultsName)

        field = field | field_empty

        field.setName(name)

        field.leaveWhitespace()

        return field


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
        return basic.alphanum(columns, name, extended=False)


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
        return basic.alphanum(columns, name, extended=True)


class NumericAdapter(FieldAdapter):
    def __init__(self):
        super(NumericAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.numeric(columns, name)


class BooleanAdapter(FieldAdapter):
    def __init__(self):
        super(BooleanAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.boolean(name)


class FlagAdapter(FieldAdapter):
    def __init__(self):
        super(FlagAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.flag(name)


class DateAdapter(FieldAdapter):
    def __init__(self):
        super(DateAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.date(name)

    def wrap_as_optional(self, field, name, columns):
        """
        Adds a wrapper rule to the field to accept empty strings.

        This empty string should be of the same size as the columns parameter. One smaller or bigger will be rejected.

        This wrapper will return None if the field is empty.

        :param field: the field to wrap
        :param name: name of the field
        :param columns: number of columns it takes
        :return: the field with an additional rule to allow empty strings
        """
        # Regular expression accepting as many whitespaces as columns
        field_empty = pp.Regex('[0]{8}|[ ]{' + str(columns) + '}')

        field_empty.setName(name)

        # Whitespaces are not removed
        field_empty.leaveWhitespace()

        # None is returned by this rule
        field_empty.setParseAction(pp.replaceWith(None))

        field_empty = field_empty.setResultsName(field.resultsName)

        field = field | field_empty

        field.setName(name)

        field.leaveWhitespace()

        return field


class TimeAdapter(FieldAdapter):
    def __init__(self):
        super(TimeAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.time(name)


class DateTimeAdapter(FieldAdapter):
    def __init__(self):
        super(DateTimeAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.date_time(name)


class BlankAdapter(FieldAdapter):
    def __init__(self):
        super(BlankAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.blank(columns, name)


class LookupAdapter(FieldAdapter):
    def __init__(self):
        super(LookupAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.lookup(values, columns, name)


class ISWCAdapter(FieldAdapter):
    def __init__(self):
        super(ISWCAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.iswc(name)


class IPIBaseNumberAdapter(FieldAdapter):
    def __init__(self):
        super(IPIBaseNumberAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ipi_base_number(name)


class IPINameNumberAdapter(FieldAdapter):
    def __init__(self):
        super(IPINameNumberAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ipi_name_number(name, )


class PercentageAdapter(FieldAdapter):
    def __init__(self):
        super(PercentageAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            maximum = int(values[0])
        else:
            maximum = 100

        return special.percentage(columns=columns, maximum=maximum, name=name)


class EAN13Adapter(FieldAdapter):
    def __init__(self):
        super(EAN13Adapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ean_13(name=name)


class ISRCAdapter(FieldAdapter):
    def __init__(self):
        super(ISRCAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.isrc(name=name)


class VISANAdapter(FieldAdapter):
    def __init__(self):
        super(VISANAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.visan(name=name)


class AudioVisualKeydapter(FieldAdapter):
    def __init__(self):
        super(AudioVisualKeydapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.audio_visual_key(name=name)


class CharSetAdapter(FieldAdapter):
    def __init__(self):
        super(CharSetAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return table.char_code(columns=columns, name=name)


class VariableAlphanumAdapter(FieldAdapter):
    def __init__(self):
        super(VariableAlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            min = int(values[0])
        else:
            min = columns

        return filename.alphanum_variable(min=min, max=columns, name=name)


class NumericFloatAdapter(FieldAdapter):
    def __init__(self):
        super(NumericFloatAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            nums_int = int(values[0])
        else:
            nums_int = columns

        return basic.numeric_float(columns=columns, nums_int=nums_int, name=name)