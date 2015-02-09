# -*- encoding: utf-8 -*-
from commonworks.agreement import Agreement, AgreementTerritory, IPA
from commonworks.interested_party import Publisher, Writer
from commonworks.work import Work, AlternateTitle, AuthoredWork, \
    RecordingDetails, WorkOrigin, PerformingArtist

"""
Offers methods to create model objects from JSON objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def parse_agreement(json_item):
    """
    Creates an Agreement from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an Agreement parsed from the JSON and with the specified id
    """
    # TODO Optional fields may be missing on the JSON
    agreement = Agreement(json_item['submitter_agreement_number'],
                          json_item['society_agreement_number'],
                          json_item['agreement_type'],
                          json_item['start_date'],
                          json_item['end_date'],
                          json_item['prior_royalty_status'],
                          json_item['post_term_collection_status'],
                          json_item['signature_date'],
                          json_item['works_number'],
                          json_item['sales_manufacture_clause'],
                          json_item['international_standard_code'],
                          json_item['retention_end_date'],
                          json_item['prior_royalty_status_date'],
                          json_item['post_term_collection_end_date'],
                          json_item['shares_change'],
                          json_item['advance_given'])

    return agreement


def parse_agreement_territory(json_item):
    """
    Creates a Territory from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a Territory parsed from the JSON
    """
    territory = AgreementTerritory(json_item['included'],
                                   json_item['tis_numeric_code'])

    return territory


def parse_alternative_work_title(json_item):
    """
    Creates an AlternativeWorkTitle from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an AlternativeWorkTitle parsed from the JSON
    """
    title = AlternateTitle(json_item['alternate_title'],
                           json_item['title_type'],
                           json_item['language'])

    return title


def parse_authored_work(json_item):
    """
    Creates an AuthoredWork from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an AuthoredWork parsed from the JSON
    """
    title = AuthoredWork(json_item['work_id'],
                         json_item['title'],
                         json_item['language_code'],
                         json_item['source'],
                         json_item['first_name_1'],
                         json_item['ip_base_1'],
                         json_item['ip_name_1'],
                         json_item['first_name_2'],
                         json_item['ip_base_2'],
                         json_item['ip_name_2'],
                         json_item['last_name_1'],
                         json_item['last_name_2'],
                         json_item['iswc'])

    return title


def parse_ipa(json_item):
    """
    Creates an IPA from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an IPA parsed from the JSON
    """
    agreement = IPA(json_item['agreement_id'], json_item['interested_party_id'], json_item['interested_party_name'],
                    json_item['agreement_role_code'], json_item['interested_party_writer_name'],
                    json_item['interested_party_ipi'], json_item['pr_society'], json_item['pr_share'],
                    json_item['mr_society'], json_item['mr_share'], json_item['sr_society'],
                    json_item['sr_share'])

    return agreement


def parse_performing_artist(json_item):
    """
    Creates a PerformingArtist from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a PerformingArtist parsed from the JSON
    """
    artist = PerformingArtist(json_item['first_name'],
                              json_item['last_name'],
                              json_item['cae_ipi_name'],
                              json_item['ipi_base_number'])

    return artist


def parse_publisher(json_item):
    """
    Creates an InterestedParty from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: an InterestedParty parsed from the JSON and with the specified id
    """
    publisher = Publisher(json_item['name'],
                          json_item['ip_id'],
                          json_item['ip_name'],
                          json_item['ip_base_id'],
                          json_item['tax_id'])

    return publisher


def parse_recording_details(json_item):
    """
    Creates a RecordingDetails from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a RecordingDetails parsed from the JSON
    """
    details = RecordingDetails(json_item['first_release_date'],
                               json_item['first_release_duration'],
                               json_item['first_album_title'],
                               json_item['first_album_label'],
                               json_item['first_release_catalog_id'],
                               json_item['ean'],
                               json_item['isrc'],
                               json_item['recording_format'],
                               json_item['recording_technique'],
                               json_item['media_type'])

    return details


def parse_work(json_item):
    """
    Creates a Work from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: a Work parsed from the JSON and with the specified id
    """
    work = Work(json_item['work_id'], json_item['title'], json_item['language_code'],
                json_item['printed_edition_publication_date'], json_item['copyright_number'],
                json_item['copyright_date'], json_item['text_music_relationship'], json_item['version_type'],
                json_item['music_arrangement'], json_item['lyric_adaptation'], json_item['excerpt_type'],
                json_item['composite_type'], json_item['composite_component_count'], json_item['iswc'],
                json_item['cwr_work_type'], json_item['musical_distribution_category'],
                json_item['duration'], json_item['catalogue_number'], json_item['opus_number'],
                json_item['contact_id'], json_item['contact_name'], json_item['recorded_indicator'],
                json_item['priority_flag'], json_item['exceptional_clause'],
                json_item['grand_rights_indicator'])

    return work


def parse_work_origin(json_item):
    """
    Creates a WorkOrigin from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a WorkOrigin parsed from the JSON
    """
    origin = WorkOrigin(json_item['intended_purpose'],
                        json_item['production_title'],
                        json_item['cd_identifier'],
                        json_item['cut_number'],
                        json_item['library'],
                        json_item['blt'],
                        json_item['visan_version'],
                        json_item['visan_isan'],
                        json_item['visan_episode'],
                        json_item['visan_check_digit'],
                        json_item['production_id'],
                        json_item['episode_title'],
                        json_item['episode_id'],
                        json_item['production_year'],
                        json_item['avi_key_society'],
                        json_item['avi_key_number'])

    return origin


def parse_writer(json_item):
    """
    Creates a Writer from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param json_item: JSON object to parse
    :return: a Writer parsed from the JSON and with the specified id
    """
    writer = Writer(json_item['first_name'],
                    json_item['personal_number'], json_item['ip_id'],
                    json_item['ip_name'], json_item['ip_base_id'],
                    json_item['last_name'])

    return writer