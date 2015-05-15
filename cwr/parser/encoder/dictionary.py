# -*- coding: utf-8 -*-

from cwr.acknowledgement import *
from cwr.agreement import *
from cwr.info import *
from cwr.parser.encoder.common import Encoder
from cwr.interested_party import *
from cwr.non_roman_alphabet import *
from cwr.work import *


"""
Classes for transforming instances of the CWR model into dictionaries.

A single monolithic encoder takes care of this process. It will just check the class of the received object and encode
it accordingly.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TransactionRecordDictionaryEncoder(Encoder):
    """
    Encodes CWR model classes into dictionaries.

    It will check the class of the received class, and encode it accordingly.
    """

    def __init__(self):
        super(TransactionRecordDictionaryEncoder, self).__init__()

        self._encoder_iswc = ISWCDictionaryEncoder()
        self._encoder_avk = AVIKeyDictionaryEncoder()
        self._encoder_visan = VISANDictionaryEncoder()

        self._encoder_publisher = PublisherDictionaryEncoder()
        self._encoder_writer = WriterDictionaryEncoder()

        self._encoder_ack = AcknowledgementDictionaryEncoder()
        self._encoder_ari = AdditionalRecordRelatedInfoDictionaryEncoder()
        self._encoder_agr = AgreementDictionaryEncoder()
        self._encoder_agr_ter = AgreementTerritoryDictionaryEncoder()
        self._encoder_alt = AlternateTitleDictionaryEncoder()
        self._encoder_authored = AuthoredWorkDictionaryEncoder()
        self._encoder_com = ComponentDictionaryEncoder(self._encoder_iswc)
        self._encoder_ind = InstrumentationDetailDictionaryEncoder()
        self._encoder_ins = InstrumentationSummaryDictionaryEncoder()
        self._encoder_ipa = InterestedPartyForAgreementDictionaryEncoder()
        self._encoder_itc = IPTerritoryOfControlDictionaryEncoder()
        self._encoder_msg = MessageDictionaryEncoder()
        self._encoder_per = PerformingArtistDictionaryEncoder()
        self._encoder_pub_wr = PublisherForWriterDictionaryEncoder()
        self._encoder_pub_rec = PublisherRecordDictionaryEncoder(self._encoder_publisher)
        self._encoder_red = RecordingDetailDictionaryEncoder()
        self._encoder_work = WorkDictionaryEncoder(self._encoder_iswc)
        self._encoder_work_origin = WorkOriginDictionaryEncoder(self._encoder_avk, self._encoder_visan)
        self._encoder_wri_rec = WriterRecordDictionaryEncoder(self._encoder_writer)

        self._encoder_nat = NonRomanAlphabetTitleDictionaryEncoder()
        self._encoder_now = NonRomanAlphabetOtherWriterDictionaryEncoder()
        self._encoder_npa = NonRomanAlphabetAgreementPartyDictionaryEncoder()
        self._encoder_npn = NonRomanAlphabetPublisherNameDictionaryEncoder()
        self._encoder_npr = NonRomanAlphabetPerformanceDataDictionaryEncoder()
        self._encoder_nra_work = NonRomanAlphabetWorkDictionaryEncoder()
        self._encoder_nwn = NonRomanAlphabetWriterNameDictionaryEncoder()

    def encode(self, object):
        if isinstance(object, AcknowledgementRecord):
            # Acknowledgement
            encoded = self._encoder_ack.encode(object)
        elif isinstance(object, AdditionalRelatedInfoRecord):
            # Additional Related Info
            encoded = self._encoder_ari.encode(object)
        elif isinstance(object, AgreementRecord):
            # Agreement
            encoded = self._encoder_agr.encode(object)
        elif isinstance(object, AgreementTerritoryRecord):
            # Agreement Territory
            encoded = self._encoder_agr_ter.encode(object)
        elif isinstance(object, AlternateTitleRecord):
            # Alternate Title
            encoded = self._encoder_alt.encode(object)
        elif isinstance(object, AuthoredWorkRecord):
            # Authored Work
            encoded = self._encoder_authored.encode(object)
        elif isinstance(object, ComponentRecord):
            # Component
            encoded = self._encoder_com.encode(object)
        elif isinstance(object, InstrumentationDetailRecord):
            # Instrumentation Detail
            encoded = self._encoder_ind.encode(object)
        elif isinstance(object, InstrumentationSummaryRecord):
            # Instrumentation Summary
            encoded = self._encoder_ins.encode(object)
        elif isinstance(object, InterestedPartyForAgreementRecord):
            # Interested Party for Agreement
            encoded = self._encoder_ipa.encode(object)
        elif isinstance(object, IPTerritoryOfControlRecord):
            # Interested Party (Writer/Publisher) Territory of Control
            encoded = self._encoder_itc.encode(object)
        elif isinstance(object, MessageRecord):
            # Message
            encoded = self._encoder_msg.encode(object)
        elif isinstance(object, NonRomanAlphabetTitleRecord):
            # NAT Record
            encoded = self._encoder_nat.encode(object)
        elif isinstance(object, NonRomanAlphabetOtherWriterRecord):
            # NOW Record
            encoded = self._encoder_now.encode(object)
        elif isinstance(object, NonRomanAlphabetAgreementPartyRecord):
            # NPA Record
            encoded = self._encoder_npa.encode(object)
        elif isinstance(object, NonRomanAlphabetPublisherNameRecord):
            # NPN Record
            encoded = self._encoder_npn.encode(object)
        elif isinstance(object, NonRomanAlphabetPerformanceDataRecord):
            # NPR Record
            encoded = self._encoder_npr.encode(object)
        elif isinstance(object, NonRomanAlphabetWorkRecord):
            # NRA Record for Works
            encoded = self._encoder_nra_work.encode(object)
        elif isinstance(object, NonRomanAlphabetWriterNameRecord):
            # NWN Record for Works
            encoded = self._encoder_nwn.encode(object)
        elif isinstance(object, PerformingArtistRecord):
            # Performing Artist
            encoded = self._encoder_per.encode(object)
        elif isinstance(object, Publisher):
            # Publisher IP
            encoded = self._encoder_publisher.encode(object)
        elif isinstance(object, PublisherForWriterRecord):
            # Publisher For Writer
            encoded = self._encoder_pub_wr.encode(object)
        elif isinstance(object, PublisherRecord):
            # Publisher
            encoded = self._encoder_pub_rec.encode(object)
        elif isinstance(object, RecordingDetailRecord):
            # Recording Detail
            encoded = self._encoder_red.encode(object)
        elif isinstance(object, WorkRecord):
            # Work
            encoded = self._encoder_work.encode(object)
        elif isinstance(object, WorkOriginRecord):
            # Work Origin
            encoded = self._encoder_work_origin.encode(object)
        elif isinstance(object, Writer):
            # Writer IP
            encoded = self._encoder_writer.encode(object)
        elif isinstance(object, WriterRecord):
            # Writer
            encoded = self._encoder_wri_rec.encode(object)
        else:
            encoded = None

        return encoded


class MediaTypeDictionaryEncoder(Encoder):
    def __init__(self):
        super(MediaTypeDictionaryEncoder, self).__init__()

    def encode(self, value):
        encoded = {}

        encoded['code'] = value.code
        encoded['name'] = value.name
        encoded['media_type'] = value.media_type
        encoded['duration_max'] = value.duration_max
        encoded['works_max'] = value.works_max
        encoded['fragments_max'] = value.fragments_max

        return encoded


class TableValueDictionaryEncoder(Encoder):
    def __init__(self):
        super(TableValueDictionaryEncoder, self).__init__()

    def encode(self, value):
        encoded = {}

        encoded['code'] = value.code
        encoded['name'] = value.name
        encoded['description'] = value.description

        return encoded


class InstrumentValueDictionaryEncoder(TableValueDictionaryEncoder):
    def __init__(self):
        super(InstrumentValueDictionaryEncoder, self).__init__()

    def encode(self, value):
        encoded = super(InstrumentValueDictionaryEncoder, self).encode(value)

        encoded['family'] = value.family

        return encoded


class ISWCDictionaryEncoder(Encoder):
    def __init__(self):
        super(ISWCDictionaryEncoder, self).__init__()

    def encode(self, iswc):
        encoded = {}

        encoded['id_code'] = iswc.id_code
        encoded['check_digit'] = iswc.check_digit

        return encoded


class IPIBaseDictionaryEncoder(Encoder):
    def __init__(self):
        super(IPIBaseDictionaryEncoder, self).__init__()

    def encode(self, ipi):
        encoded = {}

        encoded['header'] = ipi.header
        encoded['id_code'] = ipi.id_code
        encoded['check_digit'] = ipi.check_digit

        return encoded


class AVIKeyDictionaryEncoder(Encoder):
    def __init__(self):
        super(AVIKeyDictionaryEncoder, self).__init__()

    def encode(self, avi_key):
        encoded = {}

        encoded['society_code'] = avi_key.society_code
        encoded['av_number'] = avi_key.av_number

        return encoded


class VISANDictionaryEncoder(Encoder):
    def __init__(self):
        super(VISANDictionaryEncoder, self).__init__()

    def encode(self, visan):
        encoded = {}

        encoded['version'] = visan.version
        encoded['isan'] = visan.isan
        encoded['episode'] = visan.episode
        encoded['check_digit'] = visan.check_digit

        return encoded


class TransactionHeaderDictionaryEncoder(Encoder):
    def __init__(self):
        super(TransactionHeaderDictionaryEncoder, self).__init__()

    def encode(self, object):
        encoded = {}

        encoded['record_type'] = object.record_type
        encoded['transaction_sequence_n'] = object.transaction_sequence_n
        encoded['record_sequence_n'] = object.record_sequence_n

        return encoded


class AcknowledgementDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(AcknowledgementDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(AcknowledgementDictionaryEncoder, self).encode(record)

        encoded['creation_date_time'] = record.creation_date_time
        encoded['creation_title'] = record.creation_title
        encoded['original_group_id'] = record.original_group_id
        encoded['original_transaction_sequence_n'] = record.original_transaction_sequence_n
        encoded['original_transaction_type'] = record.original_transaction_type
        encoded['processing_date'] = record.processing_date
        encoded['recipient_creation_n'] = record.recipient_creation_n
        encoded['submitter_creation_n'] = record.submitter_creation_n
        encoded['transaction_status'] = record.transaction_status

        return encoded


class AdditionalRecordRelatedInfoDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(AdditionalRecordRelatedInfoDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(AdditionalRecordRelatedInfoDictionaryEncoder, self).encode(record)

        encoded['note'] = record.note
        encoded['society_n'] = record.society_n
        encoded['subject_code'] = record.subject_code
        encoded['type_of_right'] = record.type_of_right
        encoded['work_n'] = record.work_n

        return encoded


class AgreementDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(AgreementDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(AgreementDictionaryEncoder, self).encode(record)

        encoded['advance_given'] = record.advance_given
        encoded['agreement_end_date'] = record.agreement_end_date
        encoded['date_of_signature'] = record.date_of_signature
        encoded['agreement_start_date'] = record.agreement_start_date
        encoded['agreement_type'] = record.agreement_type
        encoded['international_standard_code'] = record.international_standard_code
        encoded['number_of_works'] = record.number_of_works
        encoded['post_term_collection_end_date'] = record.post_term_collection_end_date
        encoded['post_term_collection_status'] = record.post_term_collection_status
        encoded['prior_royalty_start_date'] = record.prior_royalty_start_date
        encoded['prior_royalty_status'] = record.prior_royalty_status
        encoded['retention_end_date'] = record.retention_end_date
        encoded['sales_manufacture_clause'] = record.sales_manufacture_clause
        encoded['shares_change'] = record.shares_change
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['submitter_agreement_n'] = record.submitter_agreement_n

        return encoded


class AgreementTerritoryDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(AgreementTerritoryDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(AgreementTerritoryDictionaryEncoder, self).encode(record)

        encoded['inclusion_exclusion_indicator'] = record.inclusion_exclusion_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code

        return encoded


class AlternateTitleDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(AlternateTitleDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(AlternateTitleDictionaryEncoder, self).encode(record)

        encoded['alternate_title'] = record.alternate_title
        encoded['title_type'] = record.title_type
        encoded['language_code'] = record.language_code

        return encoded


class AuthoredWorkDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self, iswc_encoder=None):
        super(AuthoredWorkDictionaryEncoder, self).__init__()

        if iswc_encoder:
            self._iswc_encoder = iswc_encoder
        else:
            self._iswc_encoder = ISWCDictionaryEncoder()

    def encode(self, record):
        encoded = super(AuthoredWorkDictionaryEncoder, self).encode(record)

        encoded['iswc'] = self._iswc_encoder.encode(record.iswc)
        encoded['language_code'] = record.language_code
        encoded['source'] = record.source
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['title'] = record.title
        encoded['writer_1_first_name'] = record.writer_1_first_name
        encoded['writer_2_first_name'] = record.writer_2_first_name
        encoded['writer_1_ipi_base_n'] = record.writer_1_ipi_base_n
        encoded['writer_2_ipi_base_n'] = record.writer_2_ipi_base_n
        encoded['writer_1_ipi_name_n'] = record.writer_1_ipi_name_n
        encoded['writer_2_ipi_name_n'] = record.writer_2_ipi_name_n
        encoded['writer_1_last_name'] = record.writer_1_last_name
        encoded['writer_2_last_name'] = record.writer_2_last_name

        return encoded


class ComponentDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self, iswc_encoder=None):
        super(ComponentDictionaryEncoder, self).__init__()

        if iswc_encoder:
            self._iswc_encoder = iswc_encoder
        else:
            self._iswc_encoder = ISWCDictionaryEncoder()

    def encode(self, record):
        encoded = super(ComponentDictionaryEncoder, self).encode(record)

        encoded['duration'] = record.duration
        encoded['iswc'] = self._iswc_encoder.encode(record.iswc)
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['title'] = record.title
        encoded['writer_1_first_name'] = record.writer_1_first_name
        encoded['writer_2_first_name'] = record.writer_2_first_name
        encoded['writer_2_ipi_base_n'] = record.writer_2_ipi_base_n
        encoded['writer_2_ipi_name_n'] = record.writer_2_ipi_name_n
        encoded['writer_1_ipi_base_n'] = record.writer_1_ipi_base_n
        encoded['writer_1_ipi_name_n'] = record.writer_1_ipi_name_n
        encoded['writer_1_last_name'] = record.writer_1_last_name
        encoded['writer_2_last_name'] = record.writer_2_last_name

        return encoded


class InstrumentationDetailDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(InstrumentationDetailDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(InstrumentationDetailDictionaryEncoder, self).encode(record)

        encoded['instrument_code'] = record.instrument_code
        encoded['number_players'] = record.number_players

        return encoded


class InstrumentationSummaryDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(InstrumentationSummaryDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(InstrumentationSummaryDictionaryEncoder, self).encode(record)

        encoded['instrumentation_description'] = record.instrumentation_description
        encoded['number_voices'] = record.number_voices
        encoded['standard_instrumentation_type'] = record.standard_instrumentation_type

        return encoded


class PerformingArtistDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(PerformingArtistDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(PerformingArtistDictionaryEncoder, self).encode(record)

        encoded['performing_artist_first_name'] = record.performing_artist_first_name
        encoded['performing_artist_ipi_base_n'] = record.performing_artist_ipi_base_n
        encoded['performing_artist_ipi_name_n'] = record.performing_artist_ipi_name_n
        encoded['performing_artist_last_name'] = record.performing_artist_last_name

        return encoded


class WorkOriginDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self, encoder_avk=None, encoder_visan=None):
        super(WorkOriginDictionaryEncoder, self).__init__()

        if encoder_avk:
            self._encoder_avk = encoder_avk
        else:
            self._encoder_avk = AVIKeyDictionaryEncoder()

        if encoder_visan:
            self._encoder_visan = encoder_visan
        else:
            self._encoder_visan = VISANDictionaryEncoder()

    def encode(self, record):
        encoded = super(WorkOriginDictionaryEncoder, self).encode(record)

        encoded['bltvr'] = record.bltvr
        encoded['cd_identifier'] = record.cd_identifier
        encoded['cut_number'] = record.cut_number
        encoded['episode_n'] = record.episode_n
        encoded['episode_title'] = record.episode_title
        encoded['intended_purpose'] = record.intended_purpose
        encoded['library'] = record.library
        encoded['production_n'] = record.production_n
        encoded['production_title'] = record.production_title
        encoded['year_production'] = record.year_production

        encoded['audio_visual_key'] = self._encoder_avk.encode(record.audio_visual_key)
        encoded['visan'] = self._encoder_visan.encode(record.visan)

        return encoded


class BaseWorkDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self, encoder_iswc=None):
        super(BaseWorkDictionaryEncoder, self).__init__()

        if encoder_iswc:
            self._encoder_iswc = encoder_iswc
        else:
            self._encoder_iswc = ISWCDictionaryEncoder()

    def encode(self, record):
        encoded = super(BaseWorkDictionaryEncoder, self).encode(record)

        encoded['iswc'] = self._encoder_iswc.encode(record.iswc)
        encoded['language_code'] = record.language_code
        encoded['title'] = record.title

        return encoded


class WorkDictionaryEncoder(BaseWorkDictionaryEncoder):
    def __init__(self, encoder_iswc=None):
        super(WorkDictionaryEncoder, self).__init__(encoder_iswc)

    def encode(self, record):
        encoded = super(WorkDictionaryEncoder, self).encode(record)

        encoded['catalogue_number'] = record.catalogue_number
        encoded['composite_component_count'] = record.composite_component_count
        encoded['composite_type'] = record.composite_type
        encoded['contact_id'] = record.contact_id
        encoded['contact_name'] = record.contact_name
        encoded['copyright_date'] = record.copyright_date
        encoded['copyright_number'] = record.copyright_number
        encoded['work_type'] = record.work_type
        encoded['date_publication_printed_edition'] = record.date_publication_printed_edition
        encoded['duration'] = record.duration
        encoded['exceptional_clause'] = record.exceptional_clause
        encoded['excerpt_type'] = record.excerpt_type
        encoded['grand_rights_indicator'] = record.grand_rights_indicator
        encoded['lyric_adaptation'] = record.lyric_adaptation
        encoded['music_arrangement'] = record.music_arrangement
        encoded['musical_work_distribution_category'] = record.musical_work_distribution_category
        encoded['opus_number'] = record.opus_number
        encoded['priority_flag'] = record.priority_flag
        encoded['recorded_indicator'] = record.recorded_indicator
        encoded['submitter_work_n'] = record.submitter_work_n
        encoded['text_music_relationship'] = record.text_music_relationship
        encoded['version_type'] = record.version_type

        return encoded


class PublisherForWriterDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(PublisherForWriterDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(PublisherForWriterDictionaryEncoder, self).encode(record)

        encoded['publisher_ip_n'] = record.publisher_ip_n
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['submitter_agreement_n'] = record.submitter_agreement_n
        encoded['writer_ip_n'] = record.writer_ip_n

        return encoded


class InterestedPartyRecordDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(InterestedPartyRecordDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(InterestedPartyRecordDictionaryEncoder, self).encode(record)

        encoded['first_recording_refusal'] = record.first_recording_refusal
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['mr_society'] = record.mr_society
        encoded['mr_ownership_share'] = record.mr_ownership_share
        encoded['sr_society'] = record.sr_society
        encoded['sr_ownership_share'] = record.sr_ownership_share
        encoded['usa_license'] = record.usa_license

        return encoded


class PublisherRecordDictionaryEncoder(InterestedPartyRecordDictionaryEncoder):
    def __init__(self, encoder_publisher=None):
        super(PublisherRecordDictionaryEncoder, self).__init__()
        if encoder_publisher:
            self._encoder_publisher = encoder_publisher
        else:
            self._encoder_publisher = PublisherDictionaryEncoder()

    def encode(self, record):
        encoded = super(PublisherRecordDictionaryEncoder, self).encode(record)

        encoded['agreement_type'] = record.agreement_type
        encoded['international_standard_code'] = record.international_standard_code
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['publisher_sequence_n'] = record.publisher_sequence_n
        encoded['publisher_type'] = record.publisher_type
        encoded['publisher_unknown'] = record.publisher_unknown
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['special_agreements'] = record.special_agreements
        encoded['submitter_agreement_n'] = record.submitter_agreement_n

        encoded['publisher'] = self._encoder_publisher.encode(record.publisher)

        return encoded


class WriterRecordDictionaryEncoder(InterestedPartyRecordDictionaryEncoder):
    def __init__(self, encoder_writer=None):
        super(WriterRecordDictionaryEncoder, self).__init__()
        if encoder_writer:
            self._encoder_writer = encoder_writer
        else:
            self._encoder_writer = WriterDictionaryEncoder()

    def encode(self, record):
        encoded = super(WriterRecordDictionaryEncoder, self).encode(record)

        encoded['reversionary'] = record.reversionary
        encoded['writer_designation'] = record.writer_designation
        encoded['writer_unknown'] = record.writer_unknown
        encoded['work_for_hire'] = record.work_for_hire

        encoded['writer'] = self._encoder_writer.encode(record.writer)

        return encoded


class NRADictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(NRADictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NRADictionaryEncoder, self).encode(record)

        encoded['language_code'] = record.language_code

        return encoded


class NonRomanAlphabetTitleDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetTitleDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetTitleDictionaryEncoder, self).encode(record)

        encoded['title'] = record.title
        encoded['title_type'] = record.title_type

        return encoded


class NonRomanAlphabetOtherWriterDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetOtherWriterDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetOtherWriterDictionaryEncoder, self).encode(record)

        encoded['position'] = record.position
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_name'] = record.writer_name

        return encoded


class NonRomanAlphabetAgreementPartyDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetAgreementPartyDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetAgreementPartyDictionaryEncoder, self).encode(record)

        encoded['ip_name'] = record.ip_name
        encoded['ip_writer_name'] = record.ip_writer_name
        encoded['ip_n'] = record.ip_n

        return encoded


class NonRomanAlphabetPublisherNameDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetPublisherNameDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetPublisherNameDictionaryEncoder, self).encode(record)

        encoded['ip_n'] = record.ip_n
        encoded['publisher_name'] = record.publisher_name
        encoded['publisher_sequence_n'] = record.publisher_sequence_n

        return encoded


class NonRomanAlphabetWorkDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetWorkDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetWorkDictionaryEncoder, self).encode(record)

        encoded['title'] = record.title

        return encoded


class NonRomanAlphabetWriterNameDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetWriterNameDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetWriterNameDictionaryEncoder, self).encode(record)

        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name
        encoded['ip_n'] = record.ip_n

        return encoded


class NonRomanAlphabetPerformanceDataDictionaryEncoder(NRADictionaryEncoder):
    def __init__(self):
        super(NonRomanAlphabetPerformanceDataDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(NonRomanAlphabetPerformanceDataDictionaryEncoder, self).encode(record)

        encoded['performance_dialect'] = record.performance_dialect
        encoded['performance_language'] = record.performance_language
        encoded['performing_artist_first_name'] = record.performing_artist_first_name
        encoded['performing_artist_ipi_base_n'] = record.performing_artist_ipi_base_n
        encoded['performing_artist_ipi_name_n'] = record.performing_artist_ipi_name_n
        encoded['performing_artist_name'] = record.performing_artist_name

        return encoded


class IPTerritoryOfControlDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(IPTerritoryOfControlDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(IPTerritoryOfControlDictionaryEncoder, self).encode(record)

        encoded['ip_n'] = record.ip_n
        encoded['ie_indicator'] = record.inclusion_exclusion_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code
        encoded['sequence_n'] = record.sequence_n
        encoded['pr_collection_share'] = record.pr_collection_share
        encoded['mr_collection_share'] = record.mr_collection_share
        encoded['sr_collection_share'] = record.sr_collection_share
        encoded['shares_change'] = record.shares_change

        return encoded


class MessageDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(MessageDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(MessageDictionaryEncoder, self).encode(record)

        encoded['message_level'] = record.message_level
        encoded['message_record_type'] = record.message_record_type
        encoded['message_text'] = record.message_text
        encoded['message_type'] = record.message_type
        encoded['original_record_sequence_n'] = record.original_record_sequence_n
        encoded['validation_n'] = record.validation_n

        return encoded


class InterestedPartyForAgreementDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(InterestedPartyForAgreementDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(InterestedPartyForAgreementDictionaryEncoder, self).encode(record)

        encoded['agreement_role_code'] = record.agreement_role_code
        encoded['ip_last_name'] = record.ip_last_name
        encoded['ip_n'] = record.ip_n
        encoded['ip_writer_first_name'] = record.ip_writer_first_name
        encoded['ipi_name_n'] = record.ipi_name_n
        encoded['ipi_base_n'] = record.ipi_base_n
        encoded['mr_society'] = record.mr_society
        encoded['mr_share'] = record.mr_share
        encoded['pr_society'] = record.pr_society
        encoded['pr_share'] = record.pr_share
        encoded['sr_society'] = record.sr_society
        encoded['sr_share'] = record.sr_share

        return encoded


class RecordingDetailDictionaryEncoder(TransactionHeaderDictionaryEncoder):
    def __init__(self):
        super(RecordingDetailDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(RecordingDetailDictionaryEncoder, self).encode(record)

        encoded['ean'] = record.ean
        encoded['first_album_label'] = record.first_album_label
        encoded['first_album_title'] = record.first_album_title
        encoded['first_release_catalog_n'] = record.first_release_catalog_n
        encoded['first_release_date'] = record.first_release_date
        encoded['first_release_duration'] = record.first_release_duration
        encoded['isrc'] = record.isrc
        encoded['media_type'] = record.media_type
        encoded['recording_format'] = record.recording_format
        encoded['recording_technique'] = record.recording_technique

        return encoded


class GroupDictionaryEncoder(Encoder):
    def __init__(self, header_encoder=None, trailer_encoder=None, trans_encoder=None):
        super(GroupDictionaryEncoder, self).__init__()

        if header_encoder:
            self._header_encoder = header_encoder
        else:
            self._header_encoder = GroupHeaderDictionaryEncoder()

        if trailer_encoder:
            self._trailer_encoder = trailer_encoder
        else:
            self._trailer_encoder = GroupTrailerDictionaryEncoder()

        if trans_encoder:
            self._trans_encoder = trans_encoder
        else:
            self._trans_encoder = TransactionRecordDictionaryEncoder()

    def encode(self, record):
        encoded = {}

        encoded['group_header'] = self._header_encoder.encode(record.group_header)
        encoded['group_trailer'] = self._trailer_encoder.encode(record.group_trailer)

        transactions = []
        for trs in record.transactions:
            transaction = []
            for tr in trs:
                transaction.append(self._trans_encoder.encode(tr))
            transactions.append(transaction)

        encoded['transactions'] = transactions

        return encoded


class GroupHeaderDictionaryEncoder(Encoder):
    def __init__(self):
        super(GroupHeaderDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = {}

        encoded['batch_request_id'] = record.batch_request_id
        encoded['group_id'] = record.group_id
        encoded['record_type'] = record.record_type
        encoded['transaction_type'] = record.transaction_type
        encoded['version_number'] = record.version_number

        return encoded


class GroupTrailerDictionaryEncoder(Encoder):
    def __init__(self):
        super(GroupTrailerDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = {}

        encoded['group_id'] = record.group_id
        encoded['record_count'] = record.record_count
        encoded['record_type'] = record.record_type
        encoded['transaction_count'] = record.transaction_count

        return encoded


class InterestedPartyDictionaryEncoder(Encoder):
    def __init__(self):
        super(InterestedPartyDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = {}

        encoded['ip_n'] = record.ip_n
        encoded['ipi_base_n'] = record.ipi_base_n
        encoded['ipi_name_n'] = record.ipi_name_n
        encoded['tax_id'] = record.tax_id

        return encoded


class PublisherDictionaryEncoder(InterestedPartyDictionaryEncoder):
    def __init__(self):
        super(PublisherDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(PublisherDictionaryEncoder, self).encode(record)

        encoded['publisher_name'] = record.publisher_name

        return encoded


class WriterDictionaryEncoder(InterestedPartyDictionaryEncoder):
    def __init__(self):
        super(WriterDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = super(WriterDictionaryEncoder, self).encode(record)

        encoded['personal_number'] = record.personal_number
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name

        return encoded


class TransmissionDictionaryEncoder(Encoder):
    def __init__(self, header_encoder=None, trailer_encoder=None, groups_encoder=None):
        super(TransmissionDictionaryEncoder, self).__init__()

        if header_encoder:
            self._header_encoder = header_encoder
        else:
            self._header_encoder = TransmissionHeaderDictionaryEncoder()

        if trailer_encoder:
            self._trailer_encoder = trailer_encoder
        else:
            self._trailer_encoder = TransmissionTrailerDictionaryEncoder()

        if groups_encoder:
            self._groups_encoder = groups_encoder
        else:
            self._groups_encoder = GroupDictionaryEncoder()

    def encode(self, record):
        encoded = {}

        encoded['header'] = self._header_encoder.encode(record.header)
        encoded['trailer'] = self._trailer_encoder.encode(record.trailer)

        groups = []
        for grp in record.groups:
            groups.append(self._groups_encoder.encode(grp))

        encoded['groups'] = groups

        return encoded


class TransmissionHeaderDictionaryEncoder(Encoder):
    def __init__(self):
        super(TransmissionHeaderDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['sender_id'] = record.sender_id
        encoded['sender_name'] = record.sender_name
        encoded['sender_type'] = record.sender_type
        encoded['creation_date_time'] = record.creation_date_time
        encoded['transmission_date'] = record.transmission_date
        encoded['edi_standard'] = record.edi_standard
        encoded['character_set'] = record.character_set

        return encoded


class TransmissionTrailerDictionaryEncoder(Encoder):
    def __init__(self):
        super(TransmissionTrailerDictionaryEncoder, self).__init__()

    def encode(self, record):
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['group_count'] = record.group_count
        encoded['transaction_count'] = record.transaction_count
        encoded['record_count'] = record.record_count

        return encoded


class FileTagDictionaryEncoder(Encoder):
    def __init__(self):
        super(FileTagDictionaryEncoder, self).__init__()

    def encode(self, tag):
        encoded = {}

        encoded['year'] = tag.year
        encoded['sequence_n'] = tag.sequence_n
        encoded['sender'] = tag.sender
        encoded['receiver'] = tag.receiver
        encoded['version'] = tag.version

        return encoded


class FileDictionaryDictionaryEncoder(Encoder):
    def __init__(self, encoder_tag=None, encoder_trans=None):
        super(FileDictionaryDictionaryEncoder, self).__init__()

        if encoder_tag:
            self._encoder_tag = encoder_tag
        else:
            self._encoder_tag = FileTagDictionaryEncoder()

        if encoder_trans:
            self._encoder_trans = encoder_trans
        else:
            self._encoder_trans = TransmissionDictionaryEncoder()

    def encode(self, value):
        encoded = {}

        encoded['tag'] = self._encoder_tag.encode(value.tag)
        encoded['transmission'] = self._encoder_trans.encode(value.transmission)

        return encoded