# -*- encoding: utf-8 -*-

"""
Value entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class ValueEntity(object):
    """
    Represents a CWR value entity.

    This is a representation of general values such as musical genres, or the roles a party can take in an agreement.
    """
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class AgreementRole(ValueEntity):
    """
    Represents the role a party takes on an agreement.

    Some examples of it are:
    Assignor (AS): The entitled party who is assigning the rights to a musical work within an agreement
    Acquirer (AC): The entitled party who is acquiring the rights to a musical work within an agreement
    """
    def __init__(self, id, name, description):
        super(AgreementRole, self).__init__(id, name, description)


class AgreementType(ValueEntity):
    """
    Identifies a concrete type of agreement.

    Some examples of it are:
    Original Specific (OS): Agreement between the songwriter and original publisher covering a list of specific work(s)
    Subpublishing Specific (PS): Agreement between two publishers covering a list of specific work(s)
    Subpublishing General (PG): Agreement between two publishers covering all works in a catalogue
    """
    def __init__(self, id, name, description):
        super(AgreementType, self).__init__(id, name, description)


class CompositeType(ValueEntity):
    """
    Represents a composite work made from several other works.

    Some examples of it are:
    Composite of Samples (COS): A composite work containing new material and one or more samples of pre-existing recorded works
    Potpourri (POT): A composite work with the addition of original material which have been combined to form a new work, that has been published and printed
    """
    def __init__(self, id, name, description):
        super(CompositeType, self).__init__(id, name, description)


class DistributionCategory(ValueEntity):
    """
    Represents a musical distribution genre.

    This is the genre under which the music is sold.

    Some examples of it are:
    Jazz (JAZ): Music originating in black America from the early 20th century, incorporating strands of Euro-American and African music and frequently containing improvisation
    Popular (POP): The musical mainstream, usually song-based and melody-orientated, created for mass consumption
    """
    def __init__(self, id, name, description):
        super(DistributionCategory, self).__init__(id, name, description)


class ExcerptType(ValueEntity):
    """
    Identifies a musical passage.

    Some examples of it are:
    Movement (MOV): A principal division of a musical work
    Unspecified Excerpt (UEX): A work that is known to be an excerpt from another work, however the type of excerpt is unknown
    """
    def __init__(self, id, name, description):
        super(ExcerptType, self).__init__(id, name, description)


class LyricAdaptation(ValueEntity):
    """
    Identifies the way in which a work's lyrics has been modified.

    Some examples of it are:
    New (NEW): New lyrics added to the existing lyrics
    Translation (TRA): Lyrics translated into another language
    None (NON): No lyrics have been included in the work
    """
    def __init__(self, id, name, description):
        super(LyricAdaptation, self).__init__(id, name, description)


class MusicArrangement(ValueEntity):
    """
    Identifies the way in which a work's structure has been modified.

    Some examples of it are:
    New (NEW): New music added to existing music
    Addition (ADM): Music added to a pre-existing text
    Original (ORI): Music used in its original form
    """
    def __init__(self, id, name, description):
        super(MusicArrangement, self).__init__(id, name, description)


class TextMusicRelationship(ValueEntity):
    """
    Indicates which kind of text and musical contents the work includes.

    Some examples of it are:
    Music (MUS): Music only
    Music and Text (MTX): Music and text combined
    Text (TXT): Self explanatory
    """
    def __init__(self, id, name, description):
        super(TextMusicRelationship, self).__init__(id, name, description)


class VersionType(ValueEntity):
    """
    Indicates if the work is versioned in any way.

    Some examples of it are:
    Modified version of a musical work (MOD): A work resulting from the modification of a musical work
    Original work (ORI): The first established form of a work
    """
    def __init__(self, id, name, description):
        super(VersionType, self).__init__(id, name, description)


class WorkType(ValueEntity):
    """
    Represents a broad musical genre.

    Some examples of it are:
    Jazz Music (JZ)
    New Age (NA)
    Opera (OP)
    """
    def __init__(self, id, name):
        super(WorkType, self).__init__(id, name, None)