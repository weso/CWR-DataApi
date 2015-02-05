# -*- encoding: utf-8 -*-

import datetime

from commonworks.agreement import AgreementTerritory, Agreement, IPA
from commonworks.work import AlternativeWorkTitle, EntireWorkTitle, OriginalWorkTitle, \
    PerformingArtist, WorkOrigin, RecordingDetails, Work
from commonworks.interested_party import Publisher
from commonworks.society import Society
from commonworks.territory import Territory
from commonworks.value_entity import ValueEntity
from commonworks.interested_party import Writer


"""
Offers classes to create dictionaries from model objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class DictionaryAdapter(object):
    """
    Adapts objects to be added into the dictionary so they are parseable for JSON.
    """

    def __init__(self):
        pass

    @staticmethod
    def adapt(obj):
        if isinstance(obj, datetime.time) or isinstance(obj, datetime.date):
            return obj.isoformat()
        else:
            return obj


class CWRDictionaryEncoder(object):
    """
    Encodes CWR model classes into encodedionaries.
    """

    def __init__(self):
        self._adapter = DictionaryAdapter()

    def encode(self, d):
        if isinstance(d, AgreementTerritory):
            encoded = self.__encode_agreement_territory(d)
        elif isinstance(d, Agreement):
            encoded = self.__encode_agreement(d)
        elif isinstance(d, AlternativeWorkTitle):
            encoded = self.__encode_alternative_work_title(d)
        elif isinstance(d, EntireWorkTitle):
            encoded = self.__encode_entire_work_title(d)
        elif isinstance(d, IPA):
            encoded = self.__encode_ipa(d)
        elif isinstance(d, OriginalWorkTitle):
            encoded = self.__encode_original_work_title(d)
        elif isinstance(d, PerformingArtist):
            encoded = self.__encode_performing_artist(d)
        elif isinstance(d, Publisher):
            encoded = self.__encode_publisher(d)
        elif isinstance(d, RecordingDetails):
            encoded = self.__encode_recording_details(d)
        elif isinstance(d, Society):
            encoded = self.__encode_society(d)
        elif isinstance(d, Territory):
            encoded = self.__encode_territory(d)
        elif isinstance(d, ValueEntity):
            encoded = self.__encode_value_entity(d)
        elif isinstance(d, Work):
            encoded = self.__encode_work(d)
        elif isinstance(d, WorkOrigin):
            encoded = self.__encode_work_origin(d)
        elif isinstance(d, Writer):
            encoded = self.__encode_writer(d)
        else:
            encoded = None

        return encoded

    @staticmethod
    def __encode_agreement_territory(territory):
        """
        Creates a dictionary from an Agreement Territory.

        :param territory: the Agreement Territory to transform into a dictionary
        :return: a dictionary created from the Agreement Territory
        """
        encoded = {}

        encoded['included'] = territory.included
        encoded['tis_numeric_code'] = territory.tis_numeric_code

        return encoded

    def __encode_agreement(self, agreement):
        """
        Creates a dictionary from an Agreement.

        :param agreement: the Agreement to transform into a dictionary
        :return: a dictionary created from the Agreement
        """
        encoded = {}

        encoded['submitter_agreement_number'] = agreement.submitter_agreement_number
        encoded['society_agreement_number'] = agreement.society_agreement_number
        encoded['international_standard_number'] = agreement.international_standard_code
        encoded['agreement_type'] = agreement.agreement_type

        encoded['start_date'] = self._adapter.adapt(agreement.start_date)
        encoded['end_date'] = self._adapter.adapt(agreement.end_date)

        encoded['prior_royalty_status'] = agreement.prior_royalty_status
        encoded['prior_royalty_status_date'] = self._adapter.adapt(agreement.prior_royalty_status_date)

        encoded['post_term_collection_status'] = agreement.post_term_collection_status
        encoded['post_term_collection_end_date'] = self._adapter.adapt(agreement.post_term_collection_end_date)

        encoded['signature_date'] = self._adapter.adapt(agreement.signature_date)
        encoded['works_number'] = agreement.works_number
        encoded['sales_manufacture_clause'] = agreement.sales_manufacture_clause

        encoded['international_standard_code'] = agreement.international_standard_code
        encoded['agreement_type'] = agreement.agreement_type
        encoded['retention_end_date'] = self._adapter.adapt(agreement.retention_end_date)
        encoded['shares_change'] = agreement.shares_change
        encoded['advance_given'] = agreement.advance_given

        return encoded

    @staticmethod
    def __encode_alternative_work_title(title):
        """
        Creates a dictionary from an AlternativeWorkTitle.

        :param title: the AlternativeWorkTitle to transform into a dictionary
        :return: a dictionary created from the AlternativeWorkTitle
        """
        encoded = {}

        encoded['alternative_title'] = title.alternative_title
        encoded['alternative_title_type'] = title.alternative_title_type

        return encoded

    @staticmethod
    def __encode_entire_work_title(title):
        """
        Creates a dictionary from an EntireWorkTitle.

        :param title: the EntireWorkTitle to transform into a dictionary
        :return: a dictionary created from the EntireWorkTitle
        """
        encoded = {}

        encoded['entire_title'] = title.entire_title
        encoded['entire_work_iswc'] = title.entire_work_iswc
        encoded['language_code'] = title.language_code
        encoded['writer_one_first_name'] = title.writer_one_first_name
        encoded['writer_one_last_name'] = title.writer_one_last_name
        encoded['writer_one_ipi_cae'] = title.writer_one_ipi_cae
        encoded['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
        encoded['writer_two_first_name'] = title.writer_two_first_name
        encoded['writer_two_last_name'] = title.writer_two_last_name
        encoded['writer_two_ipi_cae'] = title.writer_two_ipi_cae
        encoded['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number

        return encoded

    @staticmethod
    def __encode_ipa(agreement):
        """
        Creates a dictionary from an IPAAgreement.

        :param agreement: the IPAAgreement to transform into a dictionary
        :return: a dictionary created from the IPAAgreement
        """
        encoded = {}

        encoded['agreement_id'] = agreement.agreement_id
        encoded['agreement_role_code'] = agreement.agreement_role_code
        encoded['interested_party_id'] = agreement.interested_party_id
        encoded['interested_party_name'] = agreement.interested_party_name
        encoded['interested_party_ipi'] = agreement.interested_party_ipi
        encoded['interested_party_writer_name'] = agreement.interested_party_writer_name
        encoded['pr_society'] = agreement.pr_society
        encoded['pr_share'] = agreement.pr_share
        encoded['mr_society'] = agreement.mr_society
        encoded['mr_share'] = agreement.mr_share
        encoded['sr_society'] = agreement.sr_society
        encoded['sr_share'] = agreement.sr_share

        return encoded

    @staticmethod
    def __encode_original_work_title(title):
        """
        Creates a dictionary from an OriginalWorkTitle.

        :param title: the OriginalWorkTitle to transform into a dictionary
        :return: a dictionary created from the OriginalWorkTitle
        """
        encoded = {}

        encoded['entire_title'] = title.entire_title
        encoded['entire_work_iswc'] = title.entire_work_iswc
        encoded['language_code'] = title.language_code
        encoded['writer_one_first_name'] = title.writer_one_first_name
        encoded['writer_one_last_name'] = title.writer_one_last_name
        encoded['writer_one_ipi_cae'] = title.writer_one_ipi_cae
        encoded['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
        encoded['writer_two_first_name'] = title.writer_two_first_name
        encoded['writer_two_last_name'] = title.writer_two_last_name
        encoded['writer_two_ipi_cae'] = title.writer_two_ipi_cae
        encoded['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number

        return encoded

    @staticmethod
    def __encode_performing_artist(artist):
        """
        Creates a dictionary from a PerformingArtist.

        :param artist: the PerformingArtist to transform into a dictionary
        :return: a dictionary created from the PerformingArtist
        """
        encoded = {}

        encoded['first_name'] = artist.first_name
        encoded['last_name'] = artist.last_name
        encoded['cae_ipi_name'] = artist.cae_ipi_name
        encoded['ipi_base_number'] = artist.ipi_base_number

        return encoded

    @staticmethod
    def __encode_publisher(publisher):
        """
        Creates a dictionary from a Publisher.

        :param publisher: the Publisher to transform into a dictionary
        :return: a dictionary created from the Publisher
        """
        encoded = {}

        encoded['name'] = publisher.name
        encoded['ip_id'] = publisher.ip_id
        encoded['ip_name'] = publisher.ip_name
        encoded['ip_base_id'] = publisher.ip_base_id
        encoded['tax_id'] = publisher.tax_id

        return encoded

    def __encode_recording_details(self, details):
        """
        Creates a dictionary from a RecordingDetails.

        :param details: the RecordingDetails to transform into a dictionary
        :return: a dictionary created from the RecordingDetails
        """
        encoded = {}

        encoded['first_release_date'] = self._adapter.adapt(details.first_release_date)
        encoded['first_release_duration'] = details.first_release_duration
        encoded['first_album_title'] = details.first_album_title
        encoded['first_album_label'] = details.first_album_label
        encoded['first_release_catalog_id'] = details.first_release_catalog_id
        encoded['ean'] = details.ean
        encoded['isrc'] = details.isrc
        encoded['recording_format'] = details.recording_format
        encoded['recording_technique'] = details.recording_technique
        encoded['media_type'] = details.media_type

        return encoded

    @staticmethod
    def __encode_society(society):
        """
        Creates a dictionary from a Society.

        :param society: the Society to transform into a dictionary
        :return: a dictionary created from the Society
        """
        encoded = {}

        encoded['name'] = society.name
        encoded['former_name'] = society.former_name

        return encoded

    @staticmethod
    def __encode_territory(territory):
        """
        Creates a dictionary from a Territory.

        :param territory: the Territory to transform into a dictionary
        :return: a dictionary created from the Territory
        """
        encoded = {}

        encoded['tis'] = territory.tis
        encoded['iso2'] = territory.iso2
        encoded['type'] = territory.territory_type
        encoded['name'] = territory.name
        encoded['official_name'] = territory.official_name

        return encoded

    @staticmethod
    def __encode_value_entity(entity):
        """
        Creates a dictionary from a ValueEntity.

        :param entity: the ValueEntity to transform into a dictionary
        :return: a dictionary created from the ValueEntity
        """
        encoded = {}

        encoded['id'] = entity.entity_id
        encoded['name'] = entity.name

        if entity.description is not None:
            encoded['description'] = entity.description

        return encoded

    def __encode_work(self, work):
        """
        Creates a dictionary from a Work.

        :param work: the Work to transform into a dictionary
        :return: a dictionary created from the Work
        """
        encoded = {}

        encoded['work_id'] = work.work_id
        encoded['title'] = work.title
        encoded['language_code'] = work.language_code
        encoded['printed_edition_publication_date'] = self._adapter.adapt(work.printed_edition_publication_date)
        encoded['copyright_number'] = work.copyright_number
        encoded['copyright_date'] = self._adapter.adapt(work.copyright_date)
        encoded['text_music_relationship'] = work.text_music_relationship
        encoded['version_type'] = work.version_type
        encoded['music_arrangement'] = work.music_arrangement
        encoded['lyric_adaptation'] = work.lyric_adaptation
        encoded['excerpt_type'] = work.excerpt_type
        encoded['composite_type'] = work.composite_type
        encoded['composite_component_count'] = work.composite_component_count
        encoded['iswc'] = work.iswc
        encoded['cwr_work_type'] = work.cwr_work_type
        encoded['musical_distribution_category'] = work.musical_distribution_category
        encoded['duration'] = work.duration
        encoded['catalogue_number'] = work.catalogue_number
        encoded['opus_number'] = work.opus_number
        encoded['contact_id'] = work.contact_id
        encoded['contact_name'] = work.contact_name
        encoded['recorded_indicator'] = work.recorded_indicator
        encoded['priority_flag'] = work.priority_flag
        encoded['exceptional_clause'] = work.exceptional_clause
        encoded['grand_rights_indicator'] = work.grand_rights_indicator

        return encoded

    @staticmethod
    def __encode_work_origin(origin):
        """
        Creates a dictionary from a WorkOrigin.

        :param origin: the WorkOrigin to transform into a dictionary
        :return: a dictionary created from the WorkOrigin
        """
        encoded = {}

        encoded['intended_purpose'] = origin.intended_purpose
        encoded['production_title'] = origin.production_title
        encoded['cd_identifier'] = origin.cd_identifier
        encoded['cut_number'] = origin.cut_number
        encoded['library'] = origin.library
        encoded['blt'] = origin.blt
        encoded['visan_version'] = origin.visan_version
        encoded['visan_isan'] = origin.visan_isan
        encoded['visan_episode'] = origin.visan_episode
        encoded['visan_check_digit'] = origin.visan_check_digit
        encoded['production_id'] = origin.production_id
        encoded['episode_title'] = origin.episode_title
        encoded['episode_id'] = origin.episode_id
        encoded['production_year'] = origin.production_year
        encoded['avi_key_society'] = origin.avi_key_society
        encoded['avi_key_number'] = origin.avi_key_number

        return encoded

    @staticmethod
    def __encode_writer(writer):
        """
        Creates a dictionary from a Writer.

        :param writer: the Writer to transform into a dictionary
        :return: a dictionary created from the Writer
        """
        encoded = {}

        encoded['first_name'] = writer.first_name
        encoded['last_name'] = writer.last_name
        encoded['personal_number'] = writer.personal_number
        encoded['ip_id'] = writer.ip_id
        encoded['ip_name'] = writer.ip_name
        encoded['ip_base_id'] = writer.ip_base_id

        return encoded