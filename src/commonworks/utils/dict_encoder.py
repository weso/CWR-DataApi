# -*- encoding: utf-8 -*-

from commonworks.domain.models.agreement.agreement import AgreementTerritory, Agreement
from commonworks.domain.models.work.work import AlternativeWorkTitle, EntireWorkTitle, OriginalWorkTitle, \
    PerformingArtist, WorkOrigin, RecordingDetails, Work
from commonworks.domain.models.agreement.interested_party import InterestedParty, IPAAgreement
from commonworks.domain.models.work.publisher import Publisher
from commonworks.domain.models.special_entities.society import Society
from commonworks.domain.models.special_entities.territory import Territory
from commonworks.domain.models.special_entities.value_entities.value_entity import ValueEntity
from commonworks.domain.models.work.writer import Writer

"""
Offers classes to create dictionaries from model objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class CWRDictionaryEncoder(object):
    """
    Encodes CWR model classes into dictionaries.
    """

    def __init__(self):
        pass

    def encode(self, d):
        if isinstance(d, AgreementTerritory):
            encoded = self.__encode_agreement_territory(d)
        elif isinstance(d, Agreement):
            encoded = self.__encode_agreement(d)
        elif isinstance(d, AlternativeWorkTitle):
            encoded = self.__encode_alternative_work_title(d)
        elif isinstance(d, EntireWorkTitle):
            encoded = self.__encode_entire_work_title(d)
        elif isinstance(d, InterestedParty):
            encoded = self.__encode_interested_party(d)
        elif isinstance(d, IPAAgreement):
            encoded = self.__encode_ipa_agreement(d)
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

    def __encode_agreement_territory(self, territory):
        """
        Creates a dictionary from an Agreement Territory.

        :param territory: the Agreement Territory to transform into a dictionary
        :return: a dictionary created from the Agreement Territory
        """
        dict = {}

        dict['inclusion_exclusion_indicator'] = territory.inclusion_exclusion_indicator
        dict['tis_numeric_code'] = territory.tis_numeric_code

        return dict

    def __encode_agreement(self, agreement):
        """
        Creates a dictionary from an Agreement.

        :param agreement: the Agreement to transform into a dictionary
        :return: a dictionary created from the Agreement
        """
        dict = {}

        dict['_id'] = agreement.creation_id
        dict['submitter_id'] = agreement.submitter_id
        dict['agreement_number'] = agreement.agreement_number
        dict['international_standard_number'] = agreement.international_standard_number
        dict['type'] = agreement.type
        dict['start_date'] = agreement.start_date
        dict['end_date'] = agreement.end_date
        dict['retention_end_date'] = agreement.retention_end_date
        dict['prior_royalty_status'] = agreement.prior_royalty_status
        dict['prior_royalty_status_date'] = agreement.prior_royalty_status_date
        dict['post_term_collection_status'] = agreement.post_term_collection_status
        dict['post_term_collection_end_date'] = agreement.post_term_collection_end_date
        dict['signature_date'] = agreement.signature_date
        dict['works_number'] = agreement.works_number
        dict['sales_manufacture_clause'] = agreement.sales_manufacture_clause
        dict['shares_change'] = agreement.shares_change
        dict['advance_given'] = agreement.advance_given
        dict['society_assigned_number'] = agreement.society_assigned_number

        dict['interested_parties'] = agreement.interested_parties
        dict['territories'] = []

        for territory in agreement.territories:
            dict['territories'].append(self.__encode_agreement_territory(territory))

        return dict

    def __encode_alternative_work_title(self, title):
        """
        Creates a dictionary from an AlternativeWorkTitle.

        :param title: the AlternativeWorkTitle to transform into a dictionary
        :return: a dictionary created from the AlternativeWorkTitle
        """
        dict = {}

        dict['alternative_title'] = title.alternative_title
        dict['alternative_title_type'] = title.alternative_title_type

        return dict

    def __encode_entire_work_title(self, title):
        """
        Creates a dictionary from an EntireWorkTitle.

        :param title: the EntireWorkTitle to transform into a dictionary
        :return: a dictionary created from the EntireWorkTitle
        """
        dict = {}

        dict['entire_title'] = title.entire_title
        dict['entire_work_iswc'] = title.entire_work_iswc
        dict['language_code'] = title.language_code
        dict['writer_one_first_name'] = title.writer_one_first_name
        dict['writer_one_last_name'] = title.writer_one_last_name
        dict['writer_one_ipi_cae'] = title.writer_one_ipi_cae
        dict['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
        dict['writer_two_first_name'] = title.writer_two_first_name
        dict['writer_two_last_name'] = title.writer_two_last_name
        dict['writer_two_ipi_cae'] = title.writer_two_ipi_cae
        dict['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number
        dict['work_number'] = title.work_number

        return dict

    def __encode_interested_party(self, interested_party):
        """
        Creates a dictionary from an InterestedParty.

        :param interested_party: the InterestedParty to transform into a dictionary
        :return: a dictionary created from the InterestedParty
        """
        dict = {}

        dict['_id'] = interested_party.creation_id
        dict['submitter_id'] = interested_party.submitter_id

        dict['cae_ipi_id'] = interested_party.cae_ipi_id
        dict['ipi_base_number'] = interested_party.ipi_base_number
        dict['ipa_number'] = interested_party.ipa_number
        dict['last_name'] = interested_party.last_name

        dict['agreements'] = []

        for agreement in interested_party.agreements:
            dict['agreements'].append(self.__encode_ipa_agreement(agreement))

        return dict

    def __encode_ipa_agreement(self, agreement):
        """
        Creates a dictionary from an IPAAgreement.

        :param agreement: the IPAAgreement to transform into a dictionary
        :return: a dictionary created from the IPAAgreement
        """
        dict = {}

        dict['agreement_id'] = agreement.agreement_id
        dict['agreement_role_code'] = agreement.agreement_role_code
        dict['pr_society'] = agreement.pr_society
        dict['pr_share'] = agreement.pr_share
        dict['mr_society'] = agreement.mr_society
        dict['mr_share'] = agreement.mr_share
        dict['sr_society'] = agreement.sr_society
        dict['sr_share'] = agreement.sr_share

        return dict

    def __encode_original_work_title(self, title):
        """
        Creates a dictionary from an OriginalWorkTitle.

        :param title: the OriginalWorkTitle to transform into a dictionary
        :return: a dictionary created from the OriginalWorkTitle
        """
        dict = {}

        dict['entire_title'] = title.entire_title
        dict['entire_work_iswc'] = title.entire_work_iswc
        dict['language_code'] = title.language_code
        dict['writer_one_first_name'] = title.writer_one_first_name
        dict['writer_one_last_name'] = title.writer_one_last_name
        dict['writer_one_ipi_cae'] = title.writer_one_ipi_cae
        dict['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
        dict['writer_two_first_name'] = title.writer_two_first_name
        dict['writer_two_last_name'] = title.writer_two_last_name
        dict['writer_two_ipi_cae'] = title.writer_two_ipi_cae
        dict['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number
        dict['work_number'] = title.work_number

        return dict

    def __encode_performing_artist(self, artist):
        """
        Creates a dictionary from a PerformingArtist.

        :param artist: the PerformingArtist to transform into a dictionary
        :return: a dictionary created from the PerformingArtist
        """
        dict = {}

        dict['first_name'] = artist.first_name
        dict['last_name'] = artist.last_name
        dict['cae_ipi_name'] = artist.cae_ipi_name
        dict['ipi_base_number'] = artist.ipi_base_number

        return dict

    def __encode_publisher(self, publisher):
        """
        Creates a dictionary from a Publisher.

        :param publisher: the Publisher to transform into a dictionary
        :return: a dictionary created from the Publisher
        """
        dict = {}

        dict['agreement_id'] = publisher.agreement_id
        dict['interested_party'] = publisher.interested_party

        return dict

    def __encode_recording_details(self, details):
        """
        Creates a dictionary from a RecordingDetails.

        :param details: the RecordingDetails to transform into a dictionary
        :return: a dictionary created from the RecordingDetails
        """
        dict = {}

        dict['first_release_date'] = details.first_release_date
        dict['first_release_duration'] = details.first_release_duration
        dict['first_album_title'] = details.first_album_title
        dict['first_album_label'] = details.first_album_label
        dict['first_release_catalog_id'] = details.first_release_catalog_id
        dict['ean'] = details.ean
        dict['isrc'] = details.isrc
        dict['recording_format'] = details.recording_format
        dict['recording_technique'] = details.recording_technique
        dict['media_type'] = details.media_type

        return dict

    def __encode_society(self, society):
        """
        Creates a dictionary from a Society.

        :param society: the Society to transform into a dictionary
        :return: a dictionary created from the Society
        """
        dict = {}

        dict['_id'] = society.society_id
        dict['name'] = society.name
        dict['former_name'] = society.former_name

        return dict

    def __encode_territory(self, territory):
        """
        Creates a dictionary from a Territory.

        :param territory: the Territory to transform into a dictionary
        :return: a dictionary created from the Territory
        """
        dict = {}

        dict['_id'] = territory.tis
        dict['tis'] = territory.tis
        dict['iso2'] = territory.iso2
        dict['type'] = territory.territory_type
        dict['name'] = territory.name
        dict['official_name'] = territory.official_name

        return dict

    def __encode_value_entity(self, entity):
        """
        Creates a dictionary from a ValueEntity.

        :param entity: the ValueEntity to transform into a dictionary
        :return: a dictionary created from the ValueEntity
        """
        dict = {}

        dict['_id'] = entity.entity_id
        dict['id'] = entity.entity_id
        dict['name'] = entity.name

        if entity.description is not None:
            dict['description'] = entity.description

        return dict

    def __encode_work(self, work):
        """
        Creates a dictionary from a Work.

        :param work: the Work to transform into a dictionary
        :return: a dictionary created from the Work
        """
        dict = {}

        dict['_id'] = work.creation_id
        dict['creation_id'] = work.creation_id
        dict['submitter_id'] = work.submitter_id

        dict['title'] = work.title
        dict['language_code'] = work.language_code
        dict['work_number'] = work.work_number
        dict['iswc'] = work.iswc
        dict['copyright_date'] = work.copyright_date
        dict['copyright_number'] = work.copyright_number
        dict['musical_distribution_category'] = work.musical_distribution_category
        dict['duration'] = work.duration
        dict['recorded_indicator'] = work.recorded_indicator
        dict['text_music_relationship'] = work.text_music_relationship
        dict['composite_type'] = work.composite_type
        dict['version_type'] = work.version_type
        dict['excerpt_type'] = work.excerpt_type
        dict['music_arrangement'] = work.music_arrangement
        dict['lyric_adaptation'] = work.lyric_adaptation
        dict['contact_name'] = work.contact_name
        dict['contact_id'] = work.contact_id
        dict['cwr_work_type'] = work.cwr_work_type
        dict['grand_rights_indicator'] = work.grand_rights_indicator
        dict['composite_component_count'] = work.composite_component_count
        dict['printed_edition_publication_date'] = work.printed_edition_publication_date
        dict['exceptional_clause'] = work.exceptional_clause
        dict['opus_number'] = work.opus_number
        dict['catalogue_number'] = work.catalogue_number
        dict['priority_flag'] = work.priority_flag

        if work.entire_work_title is not None:
            dict['entire_work_title'] = self.__encode_entire_work_title(work.entire_work_title)

        if work.recording_details is not None:
            dict['recording_details'] = self.__encode_recording_details(work.recording_details)

        if work.original_work_title is not None:
            dict['original_work_title'] = self.__encode_original_work_title(work.original_work_title)

        if work.work_origin is not None:
            dict['work_origin'] = self.__encode_work_origin(work.work_origin)

        dict['publishers'] = []
        for publisher in work.publishers:
            dict['publishers'].append(self.__encode_publisher(publisher))

        dict['performers'] = []
        for performer in work.performing_artists:
            dict['performers'].append(self.__encode_performing_artist(performer))

        dict['writers'] = []
        for writer in work.writers:
            dict['writers'].append(self.__encode_writer(writer))

        dict['alternative_titles'] = []
        for alt_title in work.alternative_titles:
            dict['alternative_titles'].append(self.__encode_alternative_work_title(alt_title))

        return dict

    def __encode_work_origin(self, origin):
        """
        Creates a dictionary from a WorkOrigin.

        :param origin: the WorkOrigin to transform into a dictionary
        :return: a dictionary created from the WorkOrigin
        """
        dict = {}

        dict['intended_purpose'] = origin.intended_purpose
        dict['production_title'] = origin.production_title
        dict['cd_identifier'] = origin.cd_identifier
        dict['cut_number'] = origin.cut_number
        dict['library'] = origin.library
        dict['blt'] = origin.blt
        dict['visan_version'] = origin.visan_version
        dict['visan_isan'] = origin.visan_isan
        dict['visan_episode'] = origin.visan_episode
        dict['visan_check_digit'] = origin.visan_check_digit
        dict['production_id'] = origin.production_id
        dict['episode_title'] = origin.episode_title
        dict['episode_id'] = origin.episode_id
        dict['production_year'] = origin.production_year
        dict['avi_key_society'] = origin.avi_key_society
        dict['avi_key_number'] = origin.avi_key_number

        return dict

    def __encode_writer(self, writer):
        """
        Creates a dictionary from a Writer.

        :param writer: the Writer to transform into a dictionary
        :return: a dictionary created from the Writer
        """
        dict = {}

        dict['interested_party'] = writer.interested_party

        dict['first_name'] = writer.first_name
        dict['last_name'] = writer.last_name
        dict['designation_code'] = writer.designation_code
        dict['tax_id_number'] = writer.tax_id_number
        dict['cae_ipi_name_id'] = writer.cae_ipi_name_id
        dict['pr_society'] = writer.pr_society
        dict['pr_share'] = writer.pr_share
        dict['mr_society'] = writer.mr_society
        dict['mr_share'] = writer.mr_share
        dict['sr_society'] = writer.sr_society
        dict['sr_share'] = writer.sr_share
        dict['reversionary_indicator'] = writer.reversionary_indicator
        dict['first_recording_refusal_indicator'] = writer.first_recording_refusal_indicator
        dict['work_for_hire_indicator'] = writer.work_for_hire_indicator
        dict['ipi_base_number'] = writer.ipi_base_number
        dict['personal_number'] = writer.personal_number
        dict['usa_license_indicator'] = writer.usa_license_indicator

        return dict