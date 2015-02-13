# -*- encoding: utf-8 -*-

"""
Table value entity model classes.

These represent the values for the Table Lookup fields.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class MediaTypeValue(object):
    """
    Represents a BIEM/CISAC Media Type table value.
    """

    def __init__(self, code, name, type, duration_max, works_max, fragments_max):
        self._code = code
        self._name = name
        self._type = type
        self._duration_max = duration_max
        self._works_max = works_max
        self._fragments_max = fragments_max

    @property
    def code(self):
        """
        The value code. String.

        :return: code for the value
        """
        return self._code

    @property
    def duration_max(self):
        """
        Maximum duration of the media. Integer.

        :return: the maximum duration of the media
        """
        return self._duration_max

    @property
    def fragments_max(self):
        """
        Maximum number of fragments for the media. Integer.

        :return: the maximum number of fragments for the media
        """
        return self._fragments_max

    @property
    def name(self):
        """
        The value name. String.

        :return: value name
        """
        return self._name

    @property
    def type(self):
        """
        Type of media.

        This is the group under which this media is. For example Vynil, Compact Disc or DVD.

        :return: the type of the media
        """
        return self._type

    @property
    def works_max(self):
        """
        Maximum number of works for the media. Integer.

        :return: the maximum number of works for the media
        """
        return self._works_max


class TableValue(object):
    """
    Represents a CWR table value.

    Most of the values of the Table Lookup type use this object.

    This is a representation of general values such as musical genres, or the roles a party can take in an agreement.

    Some examples are:

    Agreement roles:
    Assignor (AS): The entitled party who is assigning the rights to a musical work within an agreement
    Acquirer (AC): The entitled party who is acquiring the rights to a musical work within an agreement

    Music arrangement:
    New (NEW): New music added to existing music
    Addition (ADM): Music added to a pre-existing text
    Original (ORI): Music used in its original form

    Text-Music relationship:
    Music (MUS): Music only
    Music and Text (MTX): Music and text combined
    Text (TXT): Self explanatory
    """

    def __init__(self, code, name, description=''):
        self._code = code
        self._name = name
        self._description = description

    @property
    def code(self):
        """
        The value code. String.

        :return: code for the value
        """
        return self._code

    @property
    def description(self):
        """
        Value description. String.

        :return: the value description
        """
        return self._description

    @property
    def name(self):
        """
        The value name. String.

        :return: value name
        """
        return self._name


class InstrumentValue(TableValue):
    """
    Represents a Instrument table value.
    """

    def __init__(self, code, name, family, description=''):
        super(InstrumentValue, self).__init__(code, name, description)
        self._family = family

    @property
    def family(self):
        """
        The instrument family.

        :return: the family of the instrument
        """
        return self._family