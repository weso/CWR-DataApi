from abc import ABCMeta
from commonworks.domain.models.entity import Entity

__author__ = 'borja'


class Work(Entity):

    def __init__(self, submitter_id, json_item):
        super(Work, self).__init__(submitter_id)

        self.title = json_item['title']
        self.language_code = json_item['language_code']
        self.work_number = json_item['submitter_id']
        self.iswc = json_item['iswc']
        self.copyright_date = json_item['copyright_date']
        self.copyright_number = json_item['copyright_number']
        self.musical_distribution_category = json_item['musical_distribution_category']
        self.duration = json_item['duration']
        self.recorded_indicator = json_item['recorded_indicator']
        self.text_music_relationship = json_item['text_music_relationship']
        self.composite_type = json_item['composite_type']
        self.version_type = json_item['version_type']
        self.excerpt_type = json_item['excerpt_type']
        self.music_arrangement = json_item['music_arrangement']
        self.lyric_adaptation = json_item['lyric_adaptation']
        self.contact_name = json_item['contact_name']
        self.contact_id = json_item['contact_id']
        self.cwr_work_type = json_item['cwr_work_type']
        self.grand_rights_indicator = json_item['grand_rights_indicator']
        self.composite_component_count = json_item['composite_component_count']
        self.printed_edition_publication_date = json_item['printed_edition_publication_date']
        self.exceptional_clause = json_item['exceptional_clause']
        self.opus_number = json_item['opus_number']
        self.catalogue_number = json_item['catalogue_number']
        self.priority_flag = json_item['priority_flag']

        self._entire_work_title = None
        self._recording_details = None
        self._original_work_title = None
        self._work_origin = None

        self._additional_info = []
        self._alternative_titles = []
        self._components = []
        self._instrumentation_details = []
        self._instrumentation_summaries = []
        self._performing_artists = []
        self._publishers = []
        self._writers = []
        self._origins = []

    def to_mongo_dict(self):
        work_dict = {}

        work_dict['_id'] = self.creation_id
        work_dict['submitter_id'] = self.submitter_id

        work_dict['title'] = self.title
        work_dict['language_code'] = self.language_code
        work_dict['work_number'] = self.work_number
        work_dict['iswc'] = self.iswc
        work_dict['copyright_date'] = self.copyright_date
        work_dict['copyright_number'] = self.copyright_number
        work_dict['musical_distribution_category'] = self.musical_distribution_category
        work_dict['duration'] = self.duration
        work_dict['recorded_indicator'] = self.recorded_indicator
        work_dict['text_music_relationship'] = self.text_music_relationship
        work_dict['composite_type'] = self.composite_type
        work_dict['version_type'] = self.version_type
        work_dict['excerpt_type'] = self.excerpt_type
        work_dict['music_arrangement'] = self.music_arrangement
        work_dict['lyric_adaptation'] = self.lyric_adaptation
        work_dict['contact_name'] = self.contact_name
        work_dict['contact_id'] = self.contact_id
        work_dict['cwr_work_type'] = self.cwr_work_type
        work_dict['grand_rights_indicator'] = self.grand_rights_indicator
        work_dict['composite_component_count'] = self.composite_component_count
        work_dict['printed_edition_publication_date'] = self.printed_edition_publication_date
        work_dict['exceptional_clause'] = self.exceptional_clause
        work_dict['opus_number'] = self.opus_number
        work_dict['catalogue_number'] = self.catalogue_number
        work_dict['priority_flag'] = self.priority_flag

        if self._entire_work_title is not None:
            work_dict['entire_work_title'] = self._entire_work_title.to_mongo_dict()

        if self._recording_details is not None:
            work_dict['recording_details'] = self._recording_details.to_mongo_dict()

        if self._original_work_title is not None:
            work_dict['original_work_title'] = self._original_work_title.to_mongo_dict()

        if self._work_origin is not None:
            work_dict['work_origin'] = self._work_origin.to_mongo_dict()

        work_dict['publishers'] = []
        for publisher in self._publishers:
            work_dict['publishers'].append(publisher.to_mongo_dict())

        work_dict['performers'] = []
        for performer in self._performing_artists:
            work_dict['performers'].append(performer.to_mongo_dict())

        work_dict['writers'] = []
        for writer in self._writers:
            work_dict['writers'].append(writer.to_mongo_dict())

        work_dict['alternative_titles'] = []
        for alt_title in self._alternative_titles:
            work_dict['alternative_titles'].append(alt_title.to_mongo_dict())

        return work_dict

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
    def __init__(self, json_item):
        self.alternate_title = json_item['alternate_title']
        self.title_type = json_item['title_type']

    def to_mongo_dict(self):
        alternative_title_dict = {}

        alternative_title_dict['title'] = self.alternate_title
        alternative_title_dict['type'] = self.title_type

        return alternative_title_dict

class EntireWorkTitle(object):
    """If the work is an excerpt this object reflects the entire work from where it comes"""
    def __init__(self, json_item):
        self.entire_title = json_item['entire_title']
        self.entire_work_iswc = json_item['entire_work_iswc']
        self.language_code = json_item['language_code']
        self.writer_one_last_name = json_item['writer_one_last_name']
        self.writer_one_first_name = json_item['writer_one_first_name']
        self.writer_one_ipi_cae = json_item['writer_one_ipi_cae']
        self.writer_one_ipi_base_number = json_item['writer_one_ipi_base_number']
        self.writer_two_last_name = json_item['writer_two_last_name']
        self.writer_two_first_name = json_item['writer_two_first_name']
        self.writer_two_ipi_cae = json_item['writer_two_ipi_cae']
        self.writer_two_ipi_base_number = json_item['writer_two_ipi_base_number']
        self.work_number = json_item['submitter_id']

    def to_mongo_dict(self):
        entire_title_dict = {}

        entire_title_dict['entire_title'] = self.entire_title
        entire_title_dict['entire_work_iswc'] = self.entire_work_iswc
        entire_title_dict['language_code'] = self.language_code
        entire_title_dict['writer_one_last_name'] = self.writer_one_last_name
        entire_title_dict['writer_one_first_name'] = self.writer_one_first_name
        entire_title_dict['writer_one_ipi_cae'] = self.writer_one_ipi_cae
        entire_title_dict['writer_one_ipi_base_number'] = self.writer_one_ipi_base_number
        entire_title_dict['writer_two_last_name'] = self.writer_two_last_name
        entire_title_dict['writer_two_first_name'] = self.writer_two_first_name
        entire_title_dict['writer_two_ipi_cae'] = self.writer_two_ipi_cae
        entire_title_dict['writer_two_ipi_base_number'] = self.writer_two_ipi_base_number
        entire_title_dict['work_number'] = self.work_number

        return entire_title_dict


class OriginalWorkTitle(object):
    """If the work is a version this reflect the original one which is versioned"""
    def __init__(self, json_item):
        self.original_title = json_item['entire_title']
        self.original_work_iswc = json_item['entire_work_iswc']
        self.language_code = json_item['language_code']
        self.writer_one_last_name = json_item['writer_one_last_name']
        self.writer_one_first_name = json_item['writer_one_first_name']
        self.writer_one_ipi_cae = json_item['writer_one_ipi_cae']
        self.writer_one_ipi_base_number = json_item['writer_one_ipi_base_number']
        self.writer_two_last_name = json_item['writer_two_last_name']
        self.writer_two_first_name = json_item['writer_two_first_name']
        self.writer_two_ipi_cae = json_item['writer_two_ipi_cae']
        self.writer_two_ipi_base_number = json_item['writer_two_ipi_base_number']
        self.work_number = json_item['submitter_id']

    def to_mongo_dict(self):
        original_title_dict = {}

        original_title_dict['entire_title'] = self.original_title
        original_title_dict['entire_work_iswc'] = self.original_work_iswc
        original_title_dict['language_code'] = self.language_code
        original_title_dict['writer_one_last_name'] = self.writer_one_last_name
        original_title_dict['writer_one_first_name'] = self.writer_one_first_name
        original_title_dict['writer_one_ipi_cae'] = self.writer_one_ipi_cae
        original_title_dict['writer_one_ipi_base_number'] = self.writer_one_ipi_base_number
        original_title_dict['writer_two_last_name'] = self.writer_two_last_name
        original_title_dict['writer_two_first_name'] = self.writer_two_first_name
        original_title_dict['writer_two_ipi_cae'] = self.writer_two_ipi_cae
        original_title_dict['writer_two_ipi_base_number'] = self.writer_two_ipi_base_number
        original_title_dict['work_number'] = self.work_number

        return original_title_dict


class RecordingDetails(object):
    def __init__(self, json_item):
        self.first_release_date = json_item['first_release_date']
        self.first_release_duration = json_item['first_release_duration']
        self.first_album_title = json_item['first_album_title']
        self.first_album_label = json_item['first_album_label']
        self.first_release_catalog_id = json_item['first_release_catalog_id']
        self.ean = json_item['ean']
        self.isrc = json_item['isrc']
        self.recording_format = json_item['recording_format']
        self.recording_technique = json_item['recording_technique']
        self.media_type = json_item['media_type']

    def to_mongo_dict(self):
        recording_details_dict = {}

        recording_details_dict['first_release_date'] = self.first_release_date
        recording_details_dict['first_release_duration'] = self.first_release_duration
        recording_details_dict['first_album_title'] = self.first_album_title
        recording_details_dict['first_album_label'] = self.first_album_label
        recording_details_dict['first_release_catalog_id'] = self.first_release_catalog_id
        recording_details_dict['ean'] = self.ean
        recording_details_dict['isrc'] = self.isrc
        recording_details_dict['recording_format'] = self.recording_format
        recording_details_dict['recording_technique'] = self.recording_technique
        recording_details_dict['media_type'] = self.media_type

        return recording_details_dict


class WorkOrigin(object):
    def __init__(self, json_item):
        self.intended_purpose = json_item['intended_purpose']
        self.production_title = json_item['production_title']
        self.cd_identifier = json_item['cd_identifier']
        self.cut_number = json_item['cut_number']
        self.library = json_item['library']
        self.blt = json_item['blt']
        self.visan_version = json_item['visan_version']
        self.visan_isan = json_item['visan_isan']
        self.visan_episode = json_item['visan_episode']
        self.visan_check_digit = json_item['visan_check_digit']
        self.production_id = json_item['production_id']
        self.episode_title = json_item['episode_title']
        self.episode_id = json_item['episode_id']
        self.production_year = json_item['production_year']
        self.avi_key_society = json_item['avi_key_society']
        self.avi_key_number = json_item['avi_key_number']

    def to_mongo_dict(self):
        origin_dict = {}

        origin_dict['intended_purpose'] = self.intended_purpose
        origin_dict['production_title'] = self.production_title
        origin_dict['cd_identifier'] = self.cd_identifier
        origin_dict['cut_number'] = self.cut_number
        origin_dict['library'] = self.library
        origin_dict['blt'] = self.blt
        origin_dict['visan_version'] = self.visan_version
        origin_dict['visan_isan'] = self.visan_isan
        origin_dict['visan_episode'] = self.visan_episode
        origin_dict['visan_check_digit'] = self.visan_check_digit
        origin_dict['production_id'] = self.production_id
        origin_dict['episode_title'] = self.episode_title
        origin_dict['episode_id'] = self.episode_id
        origin_dict['production_year'] = self.production_year
        origin_dict['avi_key_society'] = self.avi_key_society
        origin_dict['avi_key_number'] = self.avi_key_number

        return origin_dict


class PerformingArtist(object):
    def __init__(self, json_item):
        self.last_name = json_item['last_name']
        self.first_name = json_item['first_name']
        self.cae_ipi_name = json_item['cae_ipi_name']
        self.ipi_base_number = json_item['ipi_base_number']

    def to_mongo_dict(self):
        artist_dict = {}

        artist_dict['last_name'] = self.last_name
        artist_dict['first_name'] = self.first_name
        artist_dict['cae_ipi_name'] = self.cae_ipi_name
        artist_dict['ipi_base_number'] = self.ipi_base_number

        return artist_dict


class Repository(object):
    __metaclass__ = ABCMeta

    def find_work_by_id(self, work_id):
        pass

    def find_works_by_submitter(self, submitter_id):
        pass

    def find_works_by_submitter_id(self, submitter_id, work_number):
        pass

    def insert_work(self, work):
        pass