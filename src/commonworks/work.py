# -*- encoding: utf-8 -*-

from commonworks.entity import Entity


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Work(Entity):
    """
    Represents a CWR work.
    """

    def __init__(self, submitter_id, title, language_code, work_number, iswc, copyright_date,
                 copyright_number, musical_distribution_category, duration,
                 recorded_indicator, text_music_relationship,
                 composite_type, version_type, excerpt_type, music_arrangement,
                 lyric_adaptation, contact_name,
                 contact_id, cwr_work_type, grand_rights_indicator,
                 composite_component_count, printed_edition_publication_date,
                 exceptional_clause, opus_number, catalogue_number, priority_flag,
                 entire_work_title=None, recording_details=None,
                 original_work_title=None,
                 work_origin=None, alternative_titles=None, publishers=None,
                 performing_artists=None, writers=None, additional_info=None,
                 components=None, instrumentation_details=None,
                 instrumentation_summaries=None, origins=None):
        super(Work, self).__init__(submitter_id)

        self._title = title
        self._language_code = language_code
        self._work_number = work_number
        self._iswc = iswc
        self._copyright_date = copyright_date
        self._copyright_number = copyright_number
        self._musical_distribution_category = musical_distribution_category
        self._duration = duration
        self._recorded_indicator = recorded_indicator
        self._text_music_relationship = text_music_relationship
        self._composite_type = composite_type
        self._version_type = version_type
        self._excerpt_type = excerpt_type
        self._music_arrangement = music_arrangement
        self._lyric_adaptation = lyric_adaptation
        self._contact_name = contact_name
        self._contact_id = contact_id
        self._cwr_work_type = cwr_work_type
        self._grand_rights_indicator = grand_rights_indicator
        self._composite_component_count = composite_component_count
        self._printed_edition_publication_date = printed_edition_publication_date
        self._exceptional_clause = exceptional_clause
        self._opus_number = opus_number
        self._catalogue_number = catalogue_number
        self._priority_flag = priority_flag

        self._entire_work_title = entire_work_title
        self._recording_details = recording_details
        self._original_work_title = original_work_title
        self._work_origin = work_origin

        if alternative_titles is None:
            self._alternative_titles = []
        else:
            self._alternative_titles = alternative_titles

        if publishers is None:
            self._publishers = []
        else:
            self._publishers = publishers

        if performing_artists is None:
            self._performing_artists = []
        else:
            self._performing_artists = performing_artists

        if writers is None:
            self._writers = []
        else:
            self._writers = writers

        if additional_info is None:
            self._additional_info = []
        else:
            self._additional_info = additional_info

        if components is None:
            self._components = []
        else:
            self._components = components

        if instrumentation_details is None:
            self._instrumentation_details = []
        else:
            self._instrumentation_details = instrumentation_details

        if instrumentation_summaries is None:
            self._instrumentation_summaries = []
        else:
            self._instrumentation_summaries = instrumentation_summaries

        if origins is None:
            self._origins = []
        else:
            self._origins = origins

    def add_alternative_title(self, alternative_title):
        self._alternative_titles.append(alternative_title)

    def add_publisher(self, publisher):
        self._publishers.append(publisher)

    def add_performer(self, performer):
        self._performing_artists.append(performer)

    def add_writer(self, writer):
        self._writers.append(writer)

    def remove_alternative_title(self, alternative_title):
        self._alternative_titles.remove(alternative_title)

    def remove_publisher(self, publisher):
        self._publishers.remove(publisher)

    def remove_performer(self, performer):
        self._performing_artists.remove(performer)

    def remove_writer(self, writer):
        self._writers.remove(writer)

    @property
    def alternative_titles(self):
        return self._alternative_titles

    @property
    def catalogue_number(self):
        return self._catalogue_number

    @property
    def composite_component_count(self):
        return self._composite_component_count

    @property
    def composite_type(self):
        return self._composite_type

    @property
    def contact_id(self):
        return self._contact_id

    @property
    def contact_name(self):
        return self._contact_name

    @property
    def copyright_date(self):
        return self._copyright_date

    @property
    def copyright_number(self):
        return self._copyright_number

    @property
    def cwr_work_type(self):
        return self._cwr_work_type

    @property
    def duration(self):
        return self._duration

    @property
    def entire_work_title(self):
        return self._entire_work_title

    @property
    def exceptional_clause(self):
        return self._exceptional_clause

    @property
    def grand_rights_indicator(self):
        return self._grand_rights_indicator

    @property
    def excerpt_type(self):
        return self._excerpt_type

    @property
    def iswc(self):
        return self._iswc

    @property
    def language_code(self):
        return self._language_code

    @property
    def lyric_adaptation(self):
        return self._lyric_adaptation

    @property
    def music_arrangement(self):
        return self._music_arrangement

    @property
    def musical_distribution_category(self):
        return self._musical_distribution_category

    @property
    def opus_number(self):
        return self._opus_number

    @property
    def original_work_title(self):
        return self._original_work_title

    @property
    def performing_artists(self):
        return self._performing_artists

    @property
    def printed_edition_publication_date(self):
        return self._printed_edition_publication_date

    @property
    def priority_flag(self):
        return self._priority_flag

    @property
    def publishers(self):
        return self._publishers

    @property
    def recorded_indicator(self):
        return self._recorded_indicator

    @property
    def recording_details(self):
        return self._recording_details

    @property
    def text_music_relationship(self):
        return self._text_music_relationship

    @property
    def title(self):
        return self._title

    @property
    def version_type(self):
        return self._version_type

    @property
    def work_number(self):
        return self._work_number

    @property
    def work_origin(self):
        return self._work_origin

    @property
    def writers(self):
        return self._writers


class AlternativeWorkTitle(object):
    """
    Represents a CWR alternative work title.
    """

    def __init__(self, alternative_title, alternative_title_type):
        self._alternative_title = alternative_title
        self._alternative_title_type = alternative_title_type

    @property
    def alternative_title(self):
        return self._alternative_title

    @property
    def alternative_title_type(self):
        return self._alternative_title_type


class EntireWorkTitle(object):
    """
    Represents a CWR entire work title.

    If the work is an excerpt this object reflects the entire work from where it comes.
    """

    def __init__(self, entire_title, entire_work_iswc, language_code
                 , writer_one_first_name, writer_one_last_name,
                 writer_one_ipi_cae, writer_one_ipi_base_number,
                 writer_two_first_name, writer_two_last_name, writer_two_ipi_cae, writer_two_ipi_base_number,
                 work_number):
        self._entire_title = entire_title
        self._entire_work_iswc = entire_work_iswc
        self._language_code = language_code
        self._writer_one_first_name = writer_one_first_name
        self._writer_one_last_name = writer_one_last_name
        self._writer_one_ipi_cae = writer_one_ipi_cae
        self._writer_one_ipi_base_number = writer_one_ipi_base_number
        self._writer_two_first_name = writer_two_first_name
        self._writer_two_last_name = writer_two_last_name
        self._writer_two_ipi_cae = writer_two_ipi_cae
        self._writer_two_ipi_base_number = writer_two_ipi_base_number
        self._work_number = work_number

    @property
    def entire_title(self):
        return self._entire_title

    @property
    def entire_work_iswc(self):
        return self._entire_work_iswc

    @property
    def language_code(self):
        return self._language_code

    @property
    def work_number(self):
        return self._work_number

    @property
    def writer_one_first_name(self):
        return self._writer_one_first_name

    @property
    def writer_one_ipi_base_number(self):
        return self._writer_one_ipi_base_number

    @property
    def writer_one_ipi_cae(self):
        return self._writer_one_ipi_cae

    @property
    def writer_one_last_name(self):
        return self._writer_one_last_name

    @property
    def writer_two_first_name(self):
        return self._writer_two_first_name

    @property
    def writer_two_ipi_base_number(self):
        return self._writer_two_ipi_base_number

    @property
    def writer_two_ipi_cae(self):
        return self._writer_two_ipi_cae

    @property
    def writer_two_last_name(self):
        return self._writer_two_last_name


class OriginalWorkTitle(object):
    """
    Represents a CWR original work title.

    If the work is a version this reflect the original one which is versioned.
    """

    def __init__(self, entire_title, entire_work_iswc, language_code, writer_one_first_name, writer_one_last_name,
                 writer_one_ipi_cae, writer_one_ipi_base_number, writer_two_first_name,
                 writer_two_last_name, writer_two_ipi_cae,
                 writer_two_ipi_base_number, work_number):
        self._entire_title = entire_title
        self._entire_work_iswc = entire_work_iswc
        self._language_code = language_code
        self._writer_one_first_name = writer_one_first_name
        self._writer_one_last_name = writer_one_last_name
        self._writer_one_ipi_cae = writer_one_ipi_cae
        self._writer_one_ipi_base_number = writer_one_ipi_base_number
        self._writer_two_first_name = writer_two_first_name
        self._writer_two_last_name = writer_two_last_name
        self._writer_two_ipi_cae = writer_two_ipi_cae
        self._writer_two_ipi_base_number = writer_two_ipi_base_number
        self._work_number = work_number

    @property
    def entire_title(self):
        return self._entire_title

    @property
    def entire_work_iswc(self):
        return self._entire_work_iswc

    @property
    def language_code(self):
        return self._language_code

    @property
    def work_number(self):
        return self._work_number

    @property
    def writer_one_first_name(self):
        return self._writer_one_first_name

    @property
    def writer_one_ipi_base_number(self):
        return self._writer_one_ipi_base_number

    @property
    def writer_one_ipi_cae(self):
        return self._writer_one_ipi_cae

    @property
    def writer_one_last_name(self):
        return self._writer_one_last_name

    @property
    def writer_two_first_name(self):
        return self._writer_two_first_name

    @property
    def writer_two_ipi_base_number(self):
        return self._writer_two_ipi_base_number

    @property
    def writer_two_ipi_cae(self):
        return self._writer_two_ipi_cae

    @property
    def writer_two_last_name(self):
        return self._writer_two_last_name


class RecordingDetails(object):
    """
    Represents a CWR recording details.
    """

    def __init__(self, first_release_date, first_release_duration, first_album_title,
                 first_album_label, first_release_catalog_id, ean,
                 isrc, recording_format, recording_technique, media_type):
        self._first_release_date = first_release_date
        self._first_release_duration = first_release_duration
        self._first_album_title = first_album_title
        self._first_album_label = first_album_label
        self._first_release_catalog_id = first_release_catalog_id
        self._ean = ean
        self._isrc = isrc
        self._recording_format = recording_format
        self._recording_technique = recording_technique
        self._media_type = media_type

    @property
    def ean(self):
        return self._ean

    @property
    def first_album_label(self):
        return self._first_album_label

    @property
    def first_album_title(self):
        return self._first_album_title

    @property
    def first_release_catalog_id(self):
        return self._first_release_catalog_id

    @property
    def first_release_date(self):
        return self._first_release_date

    @property
    def first_release_duration(self):
        return self._first_release_duration

    @property
    def isrc(self):
        return self._isrc

    @property
    def media_type(self):
        return self._media_type

    @property
    def recording_format(self):
        return self._recording_format

    @property
    def recording_technique(self):
        return self._recording_technique


class WorkOrigin(object):
    """
    Represents a CWR work origin.
    """

    def __init__(self, intended_purpose, production_title, cd_identifier, cut_number,
                 library, blt, visan_version, visan_isan, visan_episode,
                 visan_check_digit, production_id, episode_title,
                 episode_id, production_year, avi_key_society,
                 avi_key_number):
        self._intended_purpose = intended_purpose
        self._production_title = production_title
        self._cd_identifier = cd_identifier
        self._cut_number = cut_number
        self._library = library
        self._blt = blt
        self._visan_version = visan_version
        self._visan_isan = visan_isan
        self._visan_episode = visan_episode
        self._visan_check_digit = visan_check_digit
        self._production_id = production_id
        self._episode_title = episode_title
        self._episode_id = episode_id
        self._production_year = production_year
        self._avi_key_society = avi_key_society
        self._avi_key_number = avi_key_number

    @property
    def avi_key_number(self):
        return self._avi_key_number

    @property
    def avi_key_society(self):
        return self._avi_key_society

    @property
    def blt(self):
        return self._blt

    @property
    def cd_identifier(self):
        return self._cd_identifier

    @property
    def cut_number(self):
        return self._cut_number

    @property
    def episode_id(self):
        return self._episode_id

    @property
    def episode_title(self):
        return self._episode_title

    @property
    def intended_purpose(self):
        return self._intended_purpose

    @property
    def library(self):
        return self._library

    @property
    def production_id(self):
        return self._production_id

    @property
    def production_title(self):
        return self._production_title

    @property
    def production_year(self):
        return self._production_year

    @property
    def visan_check_digit(self):
        return self._visan_check_digit

    @property
    def visan_episode(self):
        return self._visan_episode

    @property
    def visan_isan(self):
        return self._visan_isan

    @property
    def visan_version(self):
        return self._visan_version


class PerformingArtist(object):
    """
    Represents a CWR performing artist.
    """

    def __init__(self, first_name, last_name, cae_ipi_name, ipi_base_number):
        self._first_name = first_name
        self._last_name = last_name
        self._cae_ipi_name = cae_ipi_name
        self._ipi_base_number = ipi_base_number

    @property
    def cae_ipi_name(self):
        return self._cae_ipi_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def ipi_base_number(self):
        return self._ipi_base_number

    @property
    def last_name(self):
        return self._last_name


