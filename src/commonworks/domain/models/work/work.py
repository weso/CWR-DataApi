# -*- encoding: utf-8 -*-

from commonworks.domain.models.entity import Entity


"""
Work entity model classes.
"""

__author__ = 'Borja Garrido Bear'
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
                 exceptional_clause, opus_number, catalogue_number, priority_flag):
        super(Work, self).__init__(submitter_id)

        self.title = title
        self.language_code = language_code
        self.work_number = work_number
        self.iswc = iswc
        self.copyright_date = copyright_date
        self.copyright_number = copyright_number
        self.musical_distribution_category = musical_distribution_category
        self.duration = duration
        self.recorded_indicator = recorded_indicator
        self.text_music_relationship = text_music_relationship
        self.composite_type = composite_type
        self.version_type = version_type
        self.excerpt_type = excerpt_type
        self.music_arrangement = music_arrangement
        self.lyric_adaptation = lyric_adaptation
        self.contact_name = contact_name
        self.contact_id = contact_id
        self.cwr_work_type = cwr_work_type
        self.grand_rights_indicator = grand_rights_indicator
        self.composite_component_count = composite_component_count
        self.printed_edition_publication_date = printed_edition_publication_date
        self.exceptional_clause = exceptional_clause
        self.opus_number = opus_number
        self.catalogue_number = catalogue_number
        self.priority_flag = priority_flag

        self._entire_work_title = None
        self._recording_details = None
        self._original_work_title = None
        self._work_origin = None

        self._alternative_titles = []
        self._publishers = []
        self._performing_artists = []
        self._writers = []

    @property
    def entire_work_title(self):
        return self._entire_work_title

    @property
    def recording_details(self):
        return self._recording_details

    @property
    def original_work_title(self):
        return self._original_work_title

    @property
    def work_origin(self):
        return self._work_origin

    @property
    def alternative_titles(self):
        return self._alternative_titles

    @property
    def publishers(self):
        return self._publishers

    @property
    def performing_artists(self):
        return self._performing_artists

    @property
    def writers(self):
        return self._writers

    def set_entire_work_title(self, entire_work_title):
        self._entire_work_title = entire_work_title

    def set_recording_details(self, recording_details):
        self._recording_details = recording_details

    def set_original_work_title(self, original_work_title):
        self._original_work_title = original_work_title

    def set_work_origin(self, work_origin):
        self._work_origin = work_origin

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

    def __init__(self, alternative_title, alternative_title_type):
        self.alternative_title = alternative_title
        self.alternative_title_type = alternative_title_type


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
        self.entire_title = entire_title
        self.entire_work_iswc = entire_work_iswc
        self.language_code = language_code
        self.writer_one_first_name = writer_one_first_name
        self.writer_one_last_name = writer_one_last_name
        self.writer_one_ipi_cae = writer_one_ipi_cae
        self.writer_one_ipi_base_number = writer_one_ipi_base_number
        self.writer_two_first_name = writer_two_first_name
        self.writer_two_last_name = writer_two_last_name
        self.writer_two_ipi_cae = writer_two_ipi_cae
        self.writer_two_ipi_base_number = writer_two_ipi_base_number
        self.work_number = work_number


class OriginalWorkTitle(object):
    """
    Represents a CWR original work title.

    If the work is a version this reflect the original one which is versioned.
    """

    def __init__(self, entire_title, entire_work_iswc, language_code, writer_one_first_name, writer_one_last_name,
                 writer_one_ipi_cae, writer_one_ipi_base_number, writer_two_first_name,
                 writer_two_last_name, writer_two_ipi_cae,
                 writer_two_ipi_base_number, work_number
    ):
        self.entire_title = entire_title
        self.entire_work_iswc = entire_work_iswc
        self.language_code = language_code
        self.writer_one_first_name = writer_one_first_name
        self.writer_one_last_name = writer_one_last_name
        self.writer_one_ipi_cae = writer_one_ipi_cae
        self.writer_one_ipi_base_number = writer_one_ipi_base_number
        self.writer_two_first_name = writer_two_first_name
        self.writer_two_last_name = writer_two_last_name
        self.writer_two_ipi_cae = writer_two_ipi_cae
        self.writer_two_ipi_base_number = writer_two_ipi_base_number
        self.work_number = work_number


class RecordingDetails(object):
    """
    Represents a CWR recording details.
    """

    def __init__(self, first_release_date, first_release_duration, first_album_title,
                 first_album_label, first_release_catalog_id, ean,
                 isrc, recording_format, recording_technique, media_type):
        self.first_release_date = first_release_date
        self.first_release_duration = first_release_duration
        self.first_album_title = first_album_title
        self.first_album_label = first_album_label
        self.first_release_catalog_id = first_release_catalog_id
        self.ean = ean
        self.isrc = isrc
        self.recording_format = recording_format
        self.recording_technique = recording_technique
        self.media_type = media_type


class WorkOrigin(object):
    """
    Represents a CWR work origin.
    """

    def __init__(self, intended_purpose, production_title, cd_identifier, cut_number,
                 library, blt, visan_version, visan_isan, visan_episode,
                 visan_check_digit, production_id, episode_title,
                 episode_id, production_year, avi_key_society,
                 avi_key_number):
        self.intended_purpose = intended_purpose
        self.production_title = production_title
        self.cd_identifier = cd_identifier
        self.cut_number = cut_number
        self.library = library
        self.blt = blt
        self.visan_version = visan_version
        self.visan_isan = visan_isan
        self.visan_episode = visan_episode
        self.visan_check_digit = visan_check_digit
        self.production_id = production_id
        self.episode_title = episode_title
        self.episode_id = episode_id
        self.production_year = production_year
        self.avi_key_society = avi_key_society
        self.avi_key_number = avi_key_number


class PerformingArtist(object):
    """
    Represents a CWR performing artist.
    """

    def __init__(self, first_name, last_name, cae_ipi_name, ipi_base_number):
        self.first_name = first_name
        self.last_name = last_name
        self.cae_ipi_name = cae_ipi_name
        self.ipi_base_number = ipi_base_number


