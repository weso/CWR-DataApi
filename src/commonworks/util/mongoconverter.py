# -*- encoding: utf-8 -*-

"""
Offers methods to create Mongo dictionaries from model objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__version__ = '0.0.0'
__status__ = 'Development'


def agreement_territory_to_mongo_dict(territory):
    """
    Creates a Mongo dictionary from an Agreement Territory.

    :param territory: the Agreement Territory to transform into a dictionary
    :return: a dictionary created from the Agreement Territory
    """
    terrioty_dict = {}

    terrioty_dict['inclusion_exclusion_indicator'] = territory.inclusion_exclusion_indicator
    terrioty_dict['tis_numeric_code'] = territory.tis_numeric_code

    return terrioty_dict


def agreement_to_mongo_dict(agreement):
    """
    Creates a Mongo dictionary from an Agreement.

    :param agreement: the Agreement to transform into a dictionary
    :return: a dictionary created from the Agreement
    """
    agreement_dict = {}

    agreement_dict['_id'] = agreement.creation_id
    agreement_dict['submitter_id'] = agreement.submitter_id
    agreement_dict['agreement_number'] = agreement.submitter_number
    agreement_dict['international_standard_number'] = agreement.international_standard_number
    agreement_dict['type'] = agreement.type
    agreement_dict['start_date'] = agreement.start_date
    agreement_dict['end_date'] = agreement.end_date
    agreement_dict['retention_end_data'] = agreement.retention_end_date
    agreement_dict['prior_royalty_status'] = agreement.prior_royalty_status
    agreement_dict['prior_royalty_status_date'] = agreement.prior_royalty_status_date
    agreement_dict['post_term_collection_status'] = agreement.post_term_collection_status
    agreement_dict['post_term_collection_end_date'] = agreement.post_term_collection_end_date
    agreement_dict['signature_date'] = agreement.signature_date
    agreement_dict['works_number'] = agreement.works_number
    agreement_dict['sales_manufacture_clause'] = agreement.sales_manufacture_clause
    agreement_dict['shares_change'] = agreement.shares_change
    agreement_dict['advance_given'] = agreement.advance_given
    agreement_dict['society_assigned_number'] = agreement.society_assigned_number

    agreement_dict['interested_parties'] = agreement.interested_parties
    agreement_dict['territories'] = []

    for territory in agreement.territories:
        agreement_dict['territories'].append(territory.to_mongo_dict())

    return agreement_dict


def alternative_work_title_to_mongo_dict(title):
    """
    Creates a Mongo dictionary from an AlternativeWorkTitle.

    :param title: the AlternativeWorkTitle to transform into a dictionary
    :return: a dictionary created from the AlternativeWorkTitle
    """
    alternative_title_dict = {}

    alternative_title_dict['title'] = title.alternate_title
    alternative_title_dict['type'] = title.title_type

    return alternative_title_dict


def entire_work_title_to_mongo_dict(title):
    """
    Creates a Mongo dictionary from an EntireWorkTitle.

    :param title: the EntireWorkTitle to transform into a dictionary
    :return: a dictionary created from the EntireWorkTitle
    """
    entire_title_dict = {}

    entire_title_dict['entire_title'] = title.entire_title
    entire_title_dict['entire_work_iswc'] = title.entire_work_iswc
    entire_title_dict['language_code'] = title.language_code
    entire_title_dict['writer_one_last_name'] = title.writer_one_last_name
    entire_title_dict['writer_one_first_name'] = title.writer_one_first_name
    entire_title_dict['writer_one_ipi_cae'] = title.writer_one_ipi_cae
    entire_title_dict['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
    entire_title_dict['writer_two_last_name'] = title.writer_two_last_name
    entire_title_dict['writer_two_first_name'] = title.writer_two_first_name
    entire_title_dict['writer_two_ipi_cae'] = title.writer_two_ipi_cae
    entire_title_dict['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number
    entire_title_dict['work_number'] = title.work_number

    return entire_title_dict


def interested_party_to_mongo_dict(interested_party):
    """
    Creates a Mongo dictionary from an InterestedParty.

    :param interested_party: the InterestedParty to transform into a dictionary
    :return: a dictionary created from the InterestedParty
    """
    ipa_dict = {}

    ipa_dict['_id'] = interested_party.creation_id
    ipa_dict['submitter_id'] = interested_party.submitter_id

    ipa_dict['cae_ipi_id'] = interested_party.cae_ipi_id
    ipa_dict['ipi_base_number'] = interested_party.ipi_base_number
    ipa_dict['ipa_number'] = interested_party.id
    ipa_dict['last_name'] = interested_party.last_name

    ipa_dict['agreements'] = []

    for agreement in interested_party.agreements:
        ipa_dict['agreements'].append(agreement.to_mongo_dict())

    return ipa_dict


def ipa_agreement_to_mongo_dict(agreement):
    """
    Creates a Mongo dictionary from an IPAAgreement.

    :param agreement: the IPAAgreement to transform into a dictionary
    :return: a dictionary created from the IPAAgreement
    """
    agr_dict = {}

    agr_dict['agreement_id'] = agreement.agreement_id
    agr_dict['role_code'] = agreement.agreement_role_code
    agr_dict['pr_society'] = agreement.pr_society
    agr_dict['pr_share'] = agreement.pr_share
    agr_dict['mr_society'] = agreement.mr_society
    agr_dict['mr_share'] = agreement.mr_share
    agr_dict['sr_society'] = agreement.sr_society
    agr_dict['sr_share'] = agreement.sr_share

    return agr_dict


def original_work_title_to_mongo_dict(title):
    """
    Creates a Mongo dictionary from an OriginalWorkTitle.

    :param title: the OriginalWorkTitle to transform into a dictionary
    :return: a dictionary created from the OriginalWorkTitle
    """
    original_title_dict = {}

    original_title_dict['entire_title'] = title.original_title
    original_title_dict['entire_work_iswc'] = title.original_work_iswc
    original_title_dict['language_code'] = title.language_code
    original_title_dict['writer_one_last_name'] = title.writer_one_last_name
    original_title_dict['writer_one_first_name'] = title.writer_one_first_name
    original_title_dict['writer_one_ipi_cae'] = title.writer_one_ipi_cae
    original_title_dict['writer_one_ipi_base_number'] = title.writer_one_ipi_base_number
    original_title_dict['writer_two_last_name'] = title.writer_two_last_name
    original_title_dict['writer_two_first_name'] = title.writer_two_first_name
    original_title_dict['writer_two_ipi_cae'] = title.writer_two_ipi_cae
    original_title_dict['writer_two_ipi_base_number'] = title.writer_two_ipi_base_number
    original_title_dict['work_number'] = title.work_number

    return original_title_dict


def performing_artist_to_mongo_dict(artist):
    """
    Creates a Mongo dictionary from a PerformingArtist.

    :param title: the PerformingArtist to transform into a dictionary
    :return: a dictionary created from the PerformingArtist
    """
    artist_dict = {}

    artist_dict['last_name'] = artist.last_name
    artist_dict['first_name'] = artist.first_name
    artist_dict['cae_ipi_name'] = artist.cae_ipi_name
    artist_dict['ipi_base_number'] = artist.ipi_base_number

    return artist_dict


def publisher_to_mongo_dict(publisher):
    """
    Creates a Mongo dictionary from a Publisher.

    :param publisher: the Publisher to transform into a dictionary
    :return: a dictionary created from the Publisher
    """
    publisher_dict = {}

    publisher_dict['agreement_id'] = publisher.mongo_agreement_id
    publisher_dict['interested_party'] = publisher.mongo_ipa_id

    return publisher_dict


def recording_details_to_mongo_dict(details):
    """
    Creates a Mongo dictionary from a RecordingDetails.

    :param title: the RecordingDetails to transform into a dictionary
    :return: a dictionary created from the RecordingDetails
    """
    recording_details_dict = {}

    recording_details_dict['first_release_date'] = details.first_release_date
    recording_details_dict['first_release_duration'] = details.first_release_duration
    recording_details_dict['first_album_title'] = details.first_album_title
    recording_details_dict['first_album_label'] = details.first_album_label
    recording_details_dict['first_release_catalog_id'] = details.first_release_catalog_id
    recording_details_dict['ean'] = details.ean
    recording_details_dict['isrc'] = details.isrc
    recording_details_dict['recording_format'] = details.recording_format
    recording_details_dict['recording_technique'] = details.recording_technique
    recording_details_dict['media_type'] = details.media_type

    return recording_details_dict


def society_to_mongo_dict(society):
    """
    Creates a Mongo dictionary from a Society.

    :param society: the Society to transform into a dictionary
    :return: a dictionary created from the Society
    """
    society_dict = {}

    society_dict['_id'] = society.id
    society_dict['name'] = society.name
    society_dict['former_name'] = society.former_name

    return society_dict


def territory_to_mongo_dict(territory):
    """
    Creates a Mongo dictionary from a Territory.

    :param territory: the Territory to transform into a dictionary
    :return: a dictionary created from the Territory
    """
    territory_dict = {}

    territory_dict['_id'] = territory.tis
    territory_dict['iso2'] = territory.iso2
    territory_dict['type'] = territory.type
    territory_dict['name'] = territory.name
    territory_dict['official_name'] = territory.official_name

    return territory_dict


def value_entity_to_mongo_dict(entity):
    """
    Creates a Mongo dictionary from a ValueEntity.

    :param entity: the ValueEntity to transform into a dictionary
    :return: a dictionary created from the ValueEntity
    """
    value_dict = {}

    value_dict['_id'] = entity.id
    value_dict['name'] = entity.name

    if entity.description is not None:
        value_dict['description'] = entity.description

    return value_dict


def work_to_mongo_dict(work):
    """
    Creates a Mongo dictionary from a Work.

    :param title: the Work to transform into a dictionary
    :return: a dictionary created from the Work
    """
    work_dict = {}

    work_dict['_id'] = work.creation_id
    work_dict['submitter_id'] = work.submitter_id

    work_dict['title'] = work.title
    work_dict['language_code'] = work.language_code
    work_dict['work_number'] = work.work_number
    work_dict['iswc'] = work.iswc
    work_dict['copyright_date'] = work.copyright_date
    work_dict['copyright_number'] = work.copyright_number
    work_dict['musical_distribution_category'] = work.musical_distribution_category
    work_dict['duration'] = work.duration
    work_dict['recorded_indicator'] = work.recorded_indicator
    work_dict['text_music_relationship'] = work.text_music_relationship
    work_dict['composite_type'] = work.composite_type
    work_dict['version_type'] = work.version_type
    work_dict['excerpt_type'] = work.excerpt_type
    work_dict['music_arrangement'] = work.music_arrangement
    work_dict['lyric_adaptation'] = work.lyric_adaptation
    work_dict['contact_name'] = work.contact_name
    work_dict['contact_id'] = work.contact_id
    work_dict['cwr_work_type'] = work.cwr_work_type
    work_dict['grand_rights_indicator'] = work.grand_rights_indicator
    work_dict['composite_component_count'] = work.composite_component_count
    work_dict['printed_edition_publication_date'] = work.printed_edition_publication_date
    work_dict['exceptional_clause'] = work.exceptional_clause
    work_dict['opus_number'] = work.opus_number
    work_dict['catalogue_number'] = work.catalogue_number
    work_dict['priority_flag'] = work.priority_flag

    if work._entire_work_title is not None:
        work_dict['entire_work_title'] = work._entire_work_title.to_mongo_dict()

    if work._recording_details is not None:
        work_dict['recording_details'] = work._recording_details.to_mongo_dict()

    if work._original_work_title is not None:
        work_dict['original_work_title'] = work._original_work_title.to_mongo_dict()

    if work._work_origin is not None:
        work_dict['work_origin'] = work._work_origin.to_mongo_dict()

    work_dict['publishers'] = []
    for publisher in work._publishers:
        work_dict['publishers'].append(publisher.to_mongo_dict())

    work_dict['performers'] = []
    for performer in work._performing_artists:
        work_dict['performers'].append(performer.to_mongo_dict())

    work_dict['writers'] = []
    for writer in work._writers:
        work_dict['writers'].append(writer.to_mongo_dict())

    work_dict['alternative_titles'] = []
    for alt_title in work._alternative_titles:
        work_dict['alternative_titles'].append(alt_title.to_mongo_dict())

    return work_dict


def work_origin_to_mongo_dict(origin):
    """
    Creates a Mongo dictionary from a WorkOrigin.

    :param title: the WorkOrigin to transform into a dictionary
    :return: a dictionary created from the WorkOrigin
    """
    origin_dict = {}

    origin_dict['intended_purpose'] = origin.intended_purpose
    origin_dict['production_title'] = origin.production_title
    origin_dict['cd_identifier'] = origin.cd_identifier
    origin_dict['cut_number'] = origin.cut_number
    origin_dict['library'] = origin.library
    origin_dict['blt'] = origin.blt
    origin_dict['visan_version'] = origin.visan_version
    origin_dict['visan_isan'] = origin.visan_isan
    origin_dict['visan_episode'] = origin.visan_episode
    origin_dict['visan_check_digit'] = origin.visan_check_digit
    origin_dict['production_id'] = origin.production_id
    origin_dict['episode_title'] = origin.episode_title
    origin_dict['episode_id'] = origin.episode_id
    origin_dict['production_year'] = origin.production_year
    origin_dict['avi_key_society'] = origin.avi_key_society
    origin_dict['avi_key_number'] = origin.avi_key_number

    return origin_dict


def writer_to_mongo_dict(writer):
    """
    Creates a Mongo dictionary from a Writer.

    :param title: the Writer to transform into a dictionary
    :return: a dictionary created from the Writer
    """
    writer_dict = {}

    writer_dict['interested_party'] = writer.mongo_ipa_id

    writer_dict['first_name'] = writer.first_name
    writer_dict['last_name'] = writer.last_name
    writer_dict['designation_code'] = writer.designation_code
    writer_dict['tax_id_number'] = writer.tax_id_number
    writer_dict['cae_ipi_name_id'] = writer.cae_ipi_name_id
    writer_dict['pr_society'] = writer.pr_society
    writer_dict['pr_share'] = writer.pr_share
    writer_dict['mr_society'] = writer.mr_society
    writer_dict['mr_share'] = writer.mr_share
    writer_dict['sr_society'] = writer.sr_society
    writer_dict['sr_share'] = writer.sr_share
    writer_dict['reversionary_indicator'] = writer.reversionary_indicator
    writer_dict['first_recording_refusal_indicator'] = writer.first_recording_refusal_indicator
    writer_dict['work_for_hire_indicator'] = writer.work_for_hire_indicator
    writer_dict['ipi_base_number'] = writer.ipi_base_number
    writer_dict['personal_number'] = writer.personal_number
    writer_dict['usa_license_indicator'] = writer.usa_license_indicator

    return writer_dict