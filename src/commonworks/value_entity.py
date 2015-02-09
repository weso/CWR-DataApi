# -*- encoding: utf-8 -*-

"""
Value entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class ValueEntity(object):
    """
    Represents a CWR value entity.

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
        return self._description

    @property
    def entity_id(self):
        return self._entity_id

    @property
    def name(self):
        return self._name