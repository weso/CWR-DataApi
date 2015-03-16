# -*- coding: utf-8 -*-

import datetime

from cwr.agreement import AgreementRecord, AgreementInterestedParty
from cwr.interested_party import Publisher, Writer
from cwr.table_value import TableValue
from cwr.work import AlternateTitleRecord, AuthoredWorkRecord, \
    PerformingArtistRecord, WorkRecord, WorkOriginRecord, RecordingDetailRecord


"""
Offers classes to create dictionaries from model objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
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
        if isinstance(d, AgreementRecord):
            encoded = self.__encode_agreement(d)
        elif isinstance(d, AlternateTitleRecord):
            encoded = self.__encode_alternative_work_title(d)
        elif isinstance(d, AuthoredWorkRecord):
            encoded = self.__encode_authored_work(d)
        elif isinstance(d, AgreementInterestedParty):
            encoded = self.__encode_ipa(d)
        elif isinstance(d, PerformingArtistRecord):
            encoded = self.__encode_performing_artist(d)
        elif isinstance(d, Publisher):
            encoded = self.__encode_publisher(d)
        elif isinstance(d, RecordingDetailRecord):
            encoded = self.__encode_recording_details(d)
        elif isinstance(d, TableValue):
            encoded = self.__encode_value_entity(d)
        elif isinstance(d, WorkRecord):
            encoded = self.__encode_work(d)
        elif isinstance(d, WorkOriginRecord):
            encoded = self.__encode_work_origin(d)
        elif isinstance(d, Writer):
            encoded = self.__encode_writer(d)
        else:
            encoded = None

        return encoded

    def __encode_agreement(self, agreement):
        """
        Creates a dictionary from an Agreement.

        :param agreement: the Agreement to transform into a dictionary
        :return: a dictionary created from the Agreement
        """
        encoded = {}

        encoded['agreement_id'] = agreement.submitter_agreement_n
        encoded['society_agreement_number'] = agreement.society_assigned_agreement_n
        encoded['international_standard_number'] = agreement.international_standard_code
        encoded['agreement_type'] = agreement.agreement_type

        encoded['start_date'] = self._adapter.adapt(agreement.agreement_start_date)
        encoded['end_date'] = self._adapter.adapt(agreement.agreement_end_date)

        encoded['prior_royalty_status'] = agreement.prior_royalty_status
        encoded['prior_royalty_start_date'] = self._adapter.adapt(agreement.prior_royalty_start_date)

        encoded['post_term_collection_status'] = agreement.post_term_collection_status
        encoded['post_term_collection_end_date'] = self._adapter.adapt(agreement.post_term_collection_end_date)

        encoded['signature_date'] = self._adapter.adapt(agreement.date_of_signature)
        encoded['works_number'] = agreement.number_of_works
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

        encoded['alternate_title'] = title.alternate_title
        encoded['title_type'] = title.title_type
        encoded['language'] = title.language_code

        return encoded

    @staticmethod
    def __encode_authored_work(work):
        """
        Creates a dictionary from an AuthoredWork.

        :param work: the AuthoredWork to transform into a dictionary
        :return: a dictionary created from the AuthoredWork
        """
        encoded = {}

        encoded['work_id'] = work.submitter_work_n
        encoded['title'] = work.creation_title
        encoded['language_code'] = work.language_code
        encoded['source'] = work.source
        encoded['first_name_1'] = work.writer_1_first_name
        encoded['ipi_base_1'] = work.writer_1_ipi_base
        encoded['ipi_name_1'] = work.writer_1_ipi_name
        encoded['first_name_2'] = work.writer_2_first_name
        encoded['ipi_base_2'] = work.writer_2_ipi_base
        encoded['ipi_name_2'] = work.writer_2_ipi_name
        encoded['last_name_1'] = work.writer_1_last_name
        encoded['last_name_2'] = work.writer_2_last_name
        encoded['iswc'] = work.iswc

        return encoded

    @staticmethod
    def __encode_ipa(agreement):
        """
        Creates a dictionary from an IPAAgreement.

        :param agreement: the IPAAgreement to transform into a dictionary
        :return: a dictionary created from the IPAAgreement
        """
        encoded = {}

        encoded['agreement_role_code'] = agreement.agreement_role_code
        encoded['ip_id'] = agreement.ip_n
        encoded['ip_last_name'] = agreement.ip_last_name
        encoded['ip_ipi'] = agreement.ipi_base_n
        encoded['ipi_name'] = agreement.ipi_name_n
        encoded['ip_writer_name'] = agreement.ip_writer_first_name
        encoded['pr_society'] = agreement.pr_society
        encoded['pr_share'] = agreement.pr_share
        encoded['mr_society'] = agreement.mr_society
        encoded['mr_share'] = agreement.mr_share
        encoded['sr_society'] = agreement.sr_society
        encoded['sr_share'] = agreement.sr_share

        return encoded

    @staticmethod
    def __encode_performing_artist(artist):
        """
        Creates a dictionary from a PerformingArtist.

        :param artist: the PerformingArtist to transform into a dictionary
        :return: a dictionary created from the PerformingArtist
        """
        encoded = {}

        encoded['first_name'] = artist.writer_first_name
        encoded['last_name'] = artist.ip_last_name
        encoded['ipi_name'] = artist.ipi_name_n
        encoded['ipi_base_number'] = artist.performing_artist_ipi_base_n

        return encoded

    @staticmethod
    def __encode_publisher(publisher):
        """
        Creates a dictionary from a Publisher.

        :param publisher: the Publisher to transform into a dictionary
        :return: a dictionary created from the Publisher
        """
        encoded = {}

        encoded['name'] = publisher.publisher_name
        encoded['ip_id'] = publisher.ip_n
        encoded['ipi_base_id'] = publisher.ipi_base_n
        encoded['ipi_name'] = publisher.ipi_name_n
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
        encoded['first_release_catalog_id'] = details.first_release_catalog_n
        encoded['ean'] = details.ean
        encoded['isrc'] = details.isrc
        encoded['recording_format'] = details.recording_format
        encoded['recording_technique'] = details.recording_technique
        encoded['media_type'] = details.media_type

        return encoded

    @staticmethod
    def __encode_value_entity(entity):
        """
        Creates a dictionary from a ValueEntity.

        :param entity: the ValueEntity to transform into a dictionary
        :return: a dictionary created from the ValueEntity
        """
        encoded = {}

        encoded['id'] = entity.instrument_code
        encoded['name'] = entity.publisher_name

        if entity.instrumentation_description is not None:
            encoded['description'] = entity.instrumentation_description

        return encoded

    def __encode_work(self, work):
        """
        Creates a dictionary from a Work.

        :param work: the Work to transform into a dictionary
        :return: a dictionary created from the Work
        """
        encoded = {}

        encoded['work_id'] = work.submitter_work_n
        encoded['title'] = work.creation_title
        encoded['language_code'] = work.language_code
        encoded['printed_edition_publication_date'] = self._adapter.adapt(work.date_publication_printed_edition)
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
        encoded['musical_distribution_category'] = work.musical_work_distribution_category
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
        encoded['bltvr'] = origin.bltvr
        encoded['visan_version'] = origin.visan_version
        encoded['visan_isan'] = origin.visan_isan
        encoded['visan_episode'] = origin.visan_episode
        encoded['visan_check_digit'] = origin.visan_check_digit
        encoded['production_id'] = origin.production_n
        encoded['episode_title'] = origin.episode_title
        encoded['episode_id'] = origin.episode_n
        encoded['production_year'] = origin.year_production
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

        encoded['first_name'] = writer.writer_first_name
        encoded['last_name'] = writer.ip_last_name
        encoded['personal_number'] = writer.personal_number
        encoded['ip_id'] = writer.ip_n
        encoded['ip_name'] = writer.ip_name
        encoded['ip_base_id'] = writer.ip_base_id

        return encoded