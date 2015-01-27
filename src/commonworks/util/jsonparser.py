# -*- encoding: utf-8 -*-
from commonworks.domain.models.agreement.agreement import Agreement
from commonworks.domain.models.agreement.agreement import Territory
from commonworks.domain.models.agreement.interested_party import InterestedParty
from commonworks.domain.models.agreement.interested_party import IPAAgreement
from commonworks.domain.models.work.publisher import Publisher
from commonworks.domain.models.work.work import Work, AlternativeWorkTitle, EntireWorkTitle, OriginalWorkTitle, \
    RecordingDetails, WorkOrigin, PerformingArtist
from commonworks.domain.models.work.writer import Writer

"""
Offers methods to create model objects from JSON objects.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def parse_agreement(submitter_id, json_item):
    """
    Creates an Agreement from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: an Agreement parsed from the JSON and with the specified id
    """
    agreement = Agreement(submitter_id)

    agreement.submitter_number = json_item['submitter_number']
    agreement.international_standard_number = json_item['international_standard_number']
    agreement.type = json_item['type']
    agreement.start_date = json_item['start_date']
    agreement.end_date = json_item['end_date']
    agreement.retention_end_date = json_item['retention_end_date']
    agreement.prior_royalty_status = json_item['prior_royalty_status']
    agreement.prior_royalty_status_date = json_item['prior_royalty_status_date']
    agreement.post_term_collection_status = json_item['post_term_collection_status']
    agreement.post_term_collection_end_date = json_item['post_term_collection_end_date']
    agreement.signature_date = json_item['signature_date']
    agreement.works_number = json_item['works_number']
    agreement.sales_manufacture_clause = json_item['sales_manufacture_clause']
    agreement.shares_change = json_item['shares_change']
    agreement.advance_given = json_item['advance_given']
    agreement.society_assigned_number = json_item['society_assigned_number']

    agreement.interested_parties = []
    agreement.territories = []

    return agreement


def parse_agreement_territory(json_item):
    """
    Creates a Territory from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a Territory parsed from the JSON
    """
    territory = Territory()

    territory.inclusion_exclusion_indicator = json_item['inclusion_exclusion_indicator']
    territory.tis_numeric_code = json_item['tis_numeric_code']

    return territory


def parse_alternative_work_title(json_item):
    """
    Creates an AlternativeWorkTitle from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an AlternativeWorkTitle parsed from the JSON
    """
    title = AlternativeWorkTitle()

    title.alternate_title = json_item['alternate_title']
    title.title_type = json_item['title_type']

    return title


def parse_entire_work_title(json_item):
    """
    Creates an EntireWorkTitle from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an EntireWorkTitle parsed from the JSON
    """
    title = EntireWorkTitle()

    title.entire_title = json_item['entire_title']
    title.entire_work_iswc = json_item['entire_work_iswc']
    title.language_code = json_item['language_code']
    title.writer_one_last_name = json_item['writer_one_last_name']
    title.writer_one_first_name = json_item['writer_one_first_name']
    title.writer_one_ipi_cae = json_item['writer_one_ipi_cae']
    title.writer_one_ipi_base_number = json_item['writer_one_ipi_base_number']
    title.writer_two_last_name = json_item['writer_two_last_name']
    title.writer_two_first_name = json_item['writer_two_first_name']
    title.writer_two_ipi_cae = json_item['writer_two_ipi_cae']
    title.writer_two_ipi_base_number = json_item['writer_two_ipi_base_number']
    title.work_number = json_item['submitter_id']

    return title


def parse_interested_party(submitter_id, json_item):
    """
    Creates an InterestedParty from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: an InterestedParty parsed from the JSON and with the specified id
    """
    party = InterestedParty(submitter_id)

    party.cae_ipi_id = json_item['cae_ipi_id']
    party.ipi_base_number = json_item['ipi_base_number']
    party.id = json_item['id']
    party.last_name = json_item['last_name']

    party.agreements = []

    return party


def parse_ipa_agreement(agreement_id, json_item):
    """
    Creates an IPAAgreement from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: an IPAAgreement parsed from the JSON and with the specified id
    """
    agreement = IPAAgreement(agreement_id)

    agreement.agreement_id = agreement_id

    agreement.agreement_role_code = json_item['agreement_role_code']
    agreement.pr_society = json_item['pr_society']
    agreement.pr_share = json_item['pr_share']
    agreement.mr_society = json_item['mr_society']
    agreement.mr_share = json_item['mr_share']
    agreement.sr_society = json_item['sr_society']
    agreement.sr_share = json_item['sr_share']

    return agreement


def parse_original_work_title(json_item):
    """
    Creates an OriginalWorkTitle from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: an OriginalWorkTitle parsed from the JSON
    """
    title = OriginalWorkTitle()

    title.original_title = json_item['entire_title']
    title.original_work_iswc = json_item['entire_work_iswc']
    title.language_code = json_item['language_code']
    title.writer_one_last_name = json_item['writer_one_last_name']
    title.writer_one_first_name = json_item['writer_one_first_name']
    title.writer_one_ipi_cae = json_item['writer_one_ipi_cae']
    title.writer_one_ipi_base_number = json_item['writer_one_ipi_base_number']
    title.writer_two_last_name = json_item['writer_two_last_name']
    title.writer_two_first_name = json_item['writer_two_first_name']
    title.writer_two_ipi_cae = json_item['writer_two_ipi_cae']
    title.writer_two_ipi_base_number = json_item['writer_two_ipi_base_number']
    title.work_number = json_item['submitter_id']

    return title


def parse_performing_artist(json_item):
    """
    Creates a PerformingArtist from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a PerformingArtist parsed from the JSON
    """
    artist = PerformingArtist()

    artist.last_name = json_item['last_name']
    artist.first_name = json_item['first_name']
    artist.cae_ipi_name = json_item['cae_ipi_name']
    artist.ipi_base_number = json_item['ipi_base_number']


def parse_publisher(submitter_id, json_item):
    """
    Creates an InterestedParty from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: an InterestedParty parsed from the JSON and with the specified id
    """
    publisher = Publisher(submitter_id)

    publisher.agreement_number = json_item['agreement_number']
    publisher.interested_party_id = json_item['interested_party_id']

    publisher.mongo_agreement_id = None
    publisher.mongo_ipa_id = None

    return publisher


def parse_recording_details(json_item):
    """
    Creates a RecordingDetails from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a RecordingDetails parsed from the JSON
    """
    details = RecordingDetails()

    details.first_release_date = json_item['first_release_date']
    details.first_release_duration = json_item['first_release_duration']
    details.first_album_title = json_item['first_album_title']
    details.first_album_label = json_item['first_album_label']
    details.first_release_catalog_id = json_item['first_release_catalog_id']
    details.ean = json_item['ean']
    details.isrc = json_item['isrc']
    details.recording_format = json_item['recording_format']
    details.recording_technique = json_item['recording_technique']
    details.media_type = json_item['media_type']

    return details


def parse_work(submitter_id, json_item):
    """
    Creates a Work from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: a Work parsed from the JSON and with the specified id
    """
    work = Work(submitter_id)

    work.title = json_item['title']
    work.language_code = json_item['language_code']
    work.work_number = json_item['submitter_id']
    work.iswc = json_item['iswc']
    work.copyright_date = json_item['copyright_date']
    work.copyright_number = json_item['copyright_number']
    work.musical_distribution_category = json_item['musical_distribution_category']
    work.duration = json_item['duration']
    work.recorded_indicator = json_item['recorded_indicator']
    work.text_music_relationship = json_item['text_music_relationship']
    work.composite_type = json_item['composite_type']
    work.version_type = json_item['version_type']
    work.excerpt_type = json_item['excerpt_type']
    work.music_arrangement = json_item['music_arrangement']
    work.lyric_adaptation = json_item['lyric_adaptation']
    work.contact_name = json_item['contact_name']
    work.contact_id = json_item['contact_id']
    work.cwr_work_type = json_item['cwr_work_type']
    work.grand_rights_indicator = json_item['grand_rights_indicator']
    work.composite_component_count = json_item['composite_component_count']
    work.printed_edition_publication_date = json_item['printed_edition_publication_date']
    work.exceptional_clause = json_item['exceptional_clause']
    work.opus_number = json_item['opus_number']
    work.catalogue_number = json_item['catalogue_number']
    work.priority_flag = json_item['priority_flag']

    work._entire_work_title = None
    work._recording_details = None
    work._original_work_title = None
    work._work_origin = None

    work._additional_info = []
    work._alternative_titles = []
    work._components = []
    work._instrumentation_details = []
    work._instrumentation_summaries = []
    work._performing_artists = []
    work._publishers = []
    work._writers = []
    work._origins = []

    return work


def parse_work_origin(json_item):
    """
    Creates a WorkOrigin from the data stored in a JSON object.

    :param json_item: JSON object to parse
    :return: a WorkOrigin parsed from the JSON
    """
    origin = WorkOrigin()

    origin.intended_purpose = json_item['intended_purpose']
    origin.production_title = json_item['production_title']
    origin.cd_identifier = json_item['cd_identifier']
    origin.cut_number = json_item['cut_number']
    origin.library = json_item['library']
    origin.blt = json_item['blt']
    origin.visan_version = json_item['visan_version']
    origin.visan_isan = json_item['visan_isan']
    origin.visan_episode = json_item['visan_episode']
    origin.visan_check_digit = json_item['visan_check_digit']
    origin.production_id = json_item['production_id']
    origin.episode_title = json_item['episode_title']
    origin.episode_id = json_item['episode_id']
    origin.production_year = json_item['production_year']
    origin.avi_key_society = json_item['avi_key_society']
    origin.avi_key_number = json_item['avi_key_number']

    return origin


def parse_writer(submitter_id, json_item):
    """
    Creates a Writer from the data stored in a JSON object, and adds to it the specified submitter ID.

    :param submitter_id: submitter id
    :param json_item: JSON object to parse
    :return: a Writer parsed from the JSON and with the specified id
    """
    writer = Writer(submitter_id)

    writer.interested_party_id = json_item['interested_party_id']
    writer.mongo_ipa_id = None

    writer.first_name = json_item['first_name']
    writer.last_name = json_item['last_name']
    writer.designation_code = json_item['designation_code']
    writer.tax_id_number = json_item['tax_id_number']
    writer.cae_ipi_name_id = json_item['cae_ipi_name_id']
    writer.pr_society = json_item['pr_society']
    writer.pr_share = json_item['pr_share']
    writer.mr_society = json_item['mr_society']
    writer.mr_share = json_item['mr_share']
    writer.sr_society = json_item['sr_society']
    writer.sr_share = json_item['sr_share']
    writer.reversionary_indicator = json_item['reversionary_indicator']
    writer.first_recording_refusal_indicator = json_item['first_recording_refusal_indicator']
    writer.work_for_hire_indicator = json_item['work_for_hire_indicator']
    writer.ipi_base_number = json_item['ipi_base_number']
    writer.personal_number = json_item['personal_number']
    writer.usa_license_indicator = json_item['usa_license_indicator']

    return writer