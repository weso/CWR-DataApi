# -*- encoding: utf-8 -*-

"""
Value entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


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

    def __init__(self, entity_id, name, description):
        self._entity_id = entity_id
        self._name = name
        self._description = description

    @property
    def description(self):
        """
        Value description. Alphanumeric.

        :return: the value description
        """
        return self._description

    @property
    def value_id(self):
        """
        The value ID.

        :return: ID for the value
        """
        return self._entity_id

    @property
    def name(self):
        """
        The value name.

        :return: value name
        """
        return self._name