# -*- encoding: utf-8 -*-

from commonworks.domain.models.entity import Entity


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear'
__version__ = '0.0.0'
__status__ = 'Development'


class Work(Entity):
    """
    Represents a CWR work.
    """

    def __init__(self, submitter_id):
        super(Work, self).__init__(submitter_id)

    def set_entire_work_title(self, json_item):
        self._entire_work_title = EntireWorkTitle(json_item)

    def set_recording_details(self, json_item):
        self._recording_details = RecordingDetails(json_item)

    def set_original_work_title(self, json_item):
        self._original_work_title = OriginalWorkTitle(json_item)

    def set_work_origin(self, json_item):
        self._work_origin = WorkOrigin(json_item)

    def add_alternative_title(self, alternative_title):
        self._alternative_titles.append(alternative_title)

    def add_publisher(self, publisher):
        self._publishers.append(publisher)

    def add_performer(self, performer):
        self._performing_artists.append(performer)

    def add_writer(self, writer):
        self._writers.append(writer)


class AlternativeWorkTitle(object):
    """
    Represents a CWR alternative work title.
    """

    def __init__(self):
        pass


class EntireWorkTitle(object):
    """
    Represents a CWR entire work title.

    If the work is an excerpt this object reflects the entire work from where it comes.
    """

    def __init__(self):
        pass


class OriginalWorkTitle(object):
    """
    Represents a CWR original work title.

    If the work is a version this reflect the original one which is versioned.
    """

    def __init__(self):
        pass


class RecordingDetails(object):
    """
    Represents a CWR recording details.
    """

    def __init__(self):
        pass


class WorkOrigin(object):
    """
    Represents a CWR work origin.
    """

    def __init__(self):
        pass


class PerformingArtist(object):
    """
    Represents a CWR performing artist.
    """

    def __init__(self):
        pass


