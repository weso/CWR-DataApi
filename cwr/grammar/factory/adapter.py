# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr.grammar.field import basic, special, table, filename

"""
CWR fields grammar adapters.

These classes allow the factories to create rules in an homogeneous way,
by setting a basic interface which will wrap around field rules, giving
a basic common method through which rules can be created.

This interface is the FieldAdapter, having only the get_field method, which
will receive a series of parameters, all of them optional, and generate a
field rule from them. The concrete rule will depend on the implementation.

Additionally, it offers the wrap_as_optional method, which allows setting a
field as optional. It is meant to be used with a field created by the adapter,
so it can be overriden for specific fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FieldAdapter(object):
    """
    Interface for adapting field rules creation to the parser factory
    requirements.

    This is meant to receive always the same, or similar, groups of values,
    and then generate a specific field rule
    from them.
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
        :return: the rule for the field
        """
        raise NotImplementedError("The get_field method is not implemented")

    def is_numeric(self):
        return False


class AlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the
    specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding
    lowercases. If the extended flag is set to True, then non-ASCII characters
    are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is
    disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(AlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        field = basic.alphanum(columns, name, extended=False)
        return field



class ExtendedAlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the
    specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding
    lowercases. If the extended flag is set to True, then non-ASCII characters
    are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is
    disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(ExtendedAlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.alphanum(columns, name, extended=True)


class EndAlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an Alphanumeric (A) field, accepting only the
    specified number of characters.

    By default Alphanumeric fields accept only ASCII characters, excluding
    lowercases. If the extended flag is set to True, then non-ASCII characters
    are allowed, but the no ASCII lowercase constraint is kept.

    This can be a compulsory field, in which case the empty string is
    disallowed.

    The text will be stripped of heading and trailing whitespaces.
    """

    def __init__(self):
        super(EndAlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        reg = basic.alphanum(columns, name, extended=True, isLast=True)
        return reg


class NumericAdapter(FieldAdapter):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified
    number of characters.

    This version only allows integers.
    """

    def __init__(self):
        super(NumericAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.numeric(columns, name)


class BooleanAdapter(FieldAdapter):
    """
    Creates the grammar for a Boolean (B) field, accepting only 'Y' or 'N'
    """

    def __init__(self):
        super(BooleanAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.boolean(name)


class FlagAdapter(FieldAdapter):
    """
    Creates the grammar for a Flag (F) field, accepting only 'Y', 'N' or 'U'.
    """

    def __init__(self):
        super(FlagAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.flag(name)


class DateAdapter(FieldAdapter):
    """
    Creates the grammar for a Date (D) field, accepting only numbers in a
    certain pattern.
    """

    def __init__(self):
        super(DateAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.date(name)

    def is_numeric(self):
        return True


class TimeAdapter(FieldAdapter):
    """
    Creates the grammar for a Time (D) field, accepting only numbers in a
    certain pattern.
    """

    def __init__(self):
        super(TimeAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.time(name)


class DateTimeAdapter(FieldAdapter):
    """
    Creates the grammar for a date and time field, which is a combination of
    the Date (D) and Time or Duration field (T)
    .
    """

    def __init__(self):
        super(DateTimeAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.date_time(name)


class BlankAdapter(FieldAdapter):
    """
    Creates the grammar for a blank field.

    These are for constant empty strings which should be ignored, as they are
    used just as fillers.
    """

    def __init__(self):
        super(BlankAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.blank(columns, name)


class LookupAdapter(FieldAdapter):
    """
    Creates the grammar for a Lookup (L) field, accepting only values from a
    list.
    """

    def __init__(self):
        super(LookupAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return basic.lookup(values, name)


class ISWCAdapter(FieldAdapter):
    """
    ISWC field.
    """

    def __init__(self):
        super(ISWCAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.iswc(name)


class IPIBaseNumberAdapter(FieldAdapter):
    """
    IPI Base Number field.
    """

    def __init__(self):
        super(IPIBaseNumberAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ipi_base_number(name)


class IPINameNumberAdapter(FieldAdapter):
    """
    IPI Name Number field.
    """

    def __init__(self):
        super(IPINameNumberAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ipi_name_number(name, )


class PercentageAdapter(FieldAdapter):
    """
    Creates the grammar for a Numeric (N) field storing a percentage and
    accepting only the specified number of
    characters.
    """

    def __init__(self):
        super(PercentageAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            maximum = int(values[0])
        else:
            maximum = 100

        return special.percentage(columns=columns, maximum=maximum, name=name)


class EAN13Adapter(FieldAdapter):
    """
    Creates the grammar for an EAN 13 code.
    """

    def __init__(self):
        super(EAN13Adapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.ean_13(name=name)


class ISRCAdapter(FieldAdapter):
    """
    Creates the grammar for an ISRC code.
    """

    def __init__(self):
        super(ISRCAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.isrc(name=name)


class VISANAdapter(FieldAdapter):
    """
    Creates the grammar for a V-ISAN code.
    """

    def __init__(self):
        super(VISANAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.visan(name=name)


class AudioVisualKeydapter(FieldAdapter):
    """
    Creates the grammar for an Audio Visual Key code.
    """

    def __init__(self):
        super(AudioVisualKeydapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        field = special.audio_visual_key(name=name)
        return field


class CharSetAdapter(FieldAdapter):
    """
    Character set code field.
    """

    def __init__(self):
        super(CharSetAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return table.char_code(columns=columns, name=name)


class VariableAlphanumAdapter(FieldAdapter):
    """
    Creates the grammar for an alphanumeric code where the size ranges between
    two values.
    """

    def __init__(self):
        super(VariableAlphanumAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            min_size = int(values[0])
        else:
            min_size = columns

        return filename.alphanum_variable(min_size=min_size, max_size=columns,
                                          name=name)


class NumericFloatAdapter(FieldAdapter):
    """
    Creates the grammar for a Numeric (N) field, accepting only the specified
    number of characters.
    """

    def __init__(self):
        super(NumericFloatAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        if values is not None and len(values) > 0:
            nums_int = int(values[0])
        else:
            nums_int = columns

        return basic.numeric_float(columns=columns, nums_int=nums_int,
                                   name=name)


class YearAdapter(FieldAdapter):
    """
    Creates the grammar for a year field, accepting only the specified number
    of integers.
    """

    def __init__(self):
        super(YearAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return filename.year(columns=columns, name=name)


class FilenameVersionAdapter(FieldAdapter):
    """
    Creates the grammar for a filename version field, accepting only specific
    delimiters.
    """

    def __init__(self):
        super(FilenameVersionAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return filename.filename_version(values=values, name=name)


class LookupIntAdapter(FieldAdapter):
    """
    Creates the grammar for an integer lookup field, accepting only specific
    values, and transforming them to an integer.
    """

    def __init__(self):
        super(LookupIntAdapter, self).__init__()

    def get_field(self, name=None, columns=None, values=None):
        return special.lookup_int(values=values, name=name)
