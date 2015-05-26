# -*- coding: utf-8 -*-

from cwr.acknowledgement import *
from cwr.agreement import *
from cwr.group import *
from cwr.info import *
from cwr.parser.decoder.common import Decoder
from cwr.interested_party import *
from cwr.non_roman_alphabet import *
from cwr.transmission import *
from cwr.work import *
from cwr.file import *
from cwr.other import *
from cwr.table_value import *

"""
Classes for transforming dictionaries into instances of the CWR model.

There is a decoder for each of the model classes, and all of them expect a dictionary having at least one key for each
field, having the same name as the field, which will refer to a valid value.

As said, the values on the dictionary should be valid values, for example if an integer is expected, then the dictionary
contains an integer. The values contained in the dictionary entries should not need to be parsed.

These decoders are useful for handling JSON transmissions or Mongo databases.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class TransactionRecordDictionaryDecoder(Decoder):
    def __init__(self):
        super(TransactionRecordDictionaryDecoder, self).__init__()
        self._decoders = {}

        self._decoders['ACK'] = AcknowledgementDictionaryDecoder()
        self._decoders['AGR'] = AgreementDictionaryDecoder()
        self._decoders['TER'] = AgreementTerritoryDictionaryDecoder()
        self._decoders['ARI'] = AdditionalRelatedInformationDictionaryDecoder()
        self._decoders['ALT'] = AlternateTitleDictionaryDecoder()
        self._decoders['EWT'] = AuthoredWorkDictionaryDecoder()
        self._decoders['VER'] = AuthoredWorkDictionaryDecoder()
        self._decoders['COM'] = ComponentDictionaryDecoder()
        self._decoders['IPA'] = InterestedPartyForAgreementDictionaryDecoder()
        self._decoders['SPT'] = IPTerritoryOfControlDictionaryDecoder()
        self._decoders['SWT'] = IPTerritoryOfControlDictionaryDecoder()
        self._decoders['IND'] = InstrumentationDetailDictionaryDecoder()
        self._decoders['INS'] = InstrumentationSummaryDictionaryDecoder()
        self._decoders['MSG'] = MessageDictionaryDecoder()
        self._decoders['PER'] = PerformingArtistDictionaryDecoder()
        self._decoders['PWR'] = PublisherForWriterDictionaryDecoder()
        self._decoders['REC'] = RecordingDetailDictionaryDecoder()
        self._decoders['EXC'] = WorkDictionaryDecoder()
        self._decoders['ISW'] = WorkDictionaryDecoder()
        self._decoders['NWR'] = WorkDictionaryDecoder()
        self._decoders['REV'] = WorkDictionaryDecoder()
        self._decoders['ORN'] = WorkOriginDictionaryDecoder()
        self._decoders['SWR'] = WriterRecordDictionaryDecoder()
        self._decoders['OWR'] = WriterRecordDictionaryDecoder()
        self._decoders['OWR'] = WriterRecordDictionaryDecoder()
        self._decoders['NPA'] = NonRomanAlphabetAgreementPartyDictionaryDecoder()
        self._decoders['NOW'] = NonRomanAlphabetOtherWriterDictionaryDecoder()
        self._decoders['NPR'] = NonRomanAlphabetPerformanceDataDictionaryDecoder()
        self._decoders['NPN'] = NonRomanAlphabetPublisherNameDictionaryDecoder()
        self._decoders['NAT'] = NonRomanAlphabetTitleDictionaryDecoder()
        self._decoders['NET'] = NonRomanAlphabetWorkDictionaryDecoder()
        self._decoders['NCT'] = NonRomanAlphabetWorkDictionaryDecoder()
        self._decoders['NVT'] = NonRomanAlphabetWorkDictionaryDecoder()
        self._decoders['NWN'] = NonRomanAlphabetWriterNameDictionaryDecoder()
        self._decoders['SPU'] = PublisherRecordDictionaryDecoder()
        self._decoders['OPU'] = PublisherRecordDictionaryDecoder()

    def decode(self, data):
        return self._decoders[data['record_type']].decode(data)


class AcknowledgementDictionaryDecoder(Decoder):
    def __init__(self):
        super(AcknowledgementDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AcknowledgementRecord(record_type=data['record_type'],
                                     transaction_sequence_n=data['transaction_sequence_n'],
                                     record_sequence_n=data['record_sequence_n'],
                                     original_group_id=data['original_group_id'],
                                     original_transaction_sequence_n=data['original_transaction_sequence_n'],
                                     original_transaction_type=data['original_transaction_type'],
                                     transaction_status=data['transaction_status'],
                                     creation_date_time=data['creation_date_time'],
                                     processing_date=data['processing_date'],
                                     creation_title=data['creation_title'],
                                     submitter_creation_n=data['submitter_creation_n'],
                                     recipient_creation_n=data['recipient_creation_n'])


class AgreementDictionaryDecoder(Decoder):
    def __init__(self):
        super(AgreementDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AgreementRecord(record_type=data['record_type'],
                               transaction_sequence_n=data['transaction_sequence_n'],
                               record_sequence_n=data['record_sequence_n'],
                               submitter_agreement_n=data['submitter_agreement_n'],
                               agreement_type=data['agreement_type'],
                               agreement_start_date=data['agreement_start_date'],
                               prior_royalty_status=data['prior_royalty_status'],
                               post_term_collection_status=data['post_term_collection_status'],
                               number_of_works=data['number_of_works'],
                               society_assigned_agreement_n=data['society_assigned_agreement_n'],
                               international_standard_code=data['international_standard_code'],
                               sales_manufacture_clause=data['sales_manufacture_clause'],
                               agreement_end_date=data['agreement_end_date'],
                               date_of_signature=data['date_of_signature'],
                               retention_end_date=data['retention_end_date'],
                               prior_royalty_start_date=data['prior_royalty_start_date'],
                               post_term_collection_end_date=data['post_term_collection_end_date'],
                               shares_change=data['shares_change'],
                               advance_given=data['advance_given'])


class AgreementTerritoryDictionaryDecoder(Decoder):
    def __init__(self):
        super(AgreementTerritoryDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AgreementTerritoryRecord(record_type=data['record_type'],
                                        transaction_sequence_n=data['transaction_sequence_n'],
                                        record_sequence_n=data['record_sequence_n'],
                                        tis_numeric_code=data['tis_numeric_code'],
                                        inclusion_exclusion_indicator=data['inclusion_exclusion_indicator'])


class AdditionalRelatedInformationDictionaryDecoder(Decoder):
    def __init__(self):
        super(AdditionalRelatedInformationDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AdditionalRelatedInfoRecord(record_type=data['record_type'],
                                           transaction_sequence_n=data['transaction_sequence_n'],
                                           record_sequence_n=data['record_sequence_n'],
                                           society_n=data['society_n'],
                                           type_of_right=data['type_of_right'],
                                           work_n=data['work_n'], subject_code=data['subject_code'],
                                           note=data['note'])


class AlternateTitleDictionaryDecoder(Decoder):
    def __init__(self):
        super(AlternateTitleDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AlternateTitleRecord(record_type=data['record_type'],
                                    transaction_sequence_n=data['transaction_sequence_n'],
                                    record_sequence_n=data['record_sequence_n'],
                                    alternate_title=data['alternate_title'],
                                    title_type=data['title_type'],
                                    language_code=data['language_code'])


class AuthoredWorkDictionaryDecoder(Decoder):
    def __init__(self):
        super(AuthoredWorkDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AuthoredWorkRecord(record_type=data['record_type'],
                                  transaction_sequence_n=data['transaction_sequence_n'],
                                  record_sequence_n=data['record_sequence_n'],
                                  title=data['title'],
                                  submitter_work_n=data['submitter_work_n'],
                                  writer_1_first_name=data['writer_1_first_name'],
                                  writer_1_last_name=data['writer_1_last_name'],
                                  writer_2_first_name=data['writer_2_first_name'],
                                  writer_2_last_name=data['writer_2_last_name'],
                                  writer_1_ipi_base_n=data['writer_1_ipi_base_n'],
                                  writer_1_ipi_name_n=data['writer_1_ipi_name_n'],
                                  writer_2_ipi_base_n=data['writer_2_ipi_base_n'],
                                  writer_2_ipi_name_n=data['writer_2_ipi_name_n'],
                                  source=data['source'],
                                  language_code=data['language_code'],
                                  iswc=data['iswc'])


class ComponentDictionaryDecoder(Decoder):
    def __init__(self):
        super(ComponentDictionaryDecoder, self).__init__()

    def decode(self, data):
        return ComponentRecord(record_type=data['record_type'],
                               transaction_sequence_n=data['transaction_sequence_n'],
                               record_sequence_n=data['record_sequence_n'],
                               title=data['title'],
                               submitter_work_n=data['submitter_work_n'],
                               writer_1_last_name=data['writer_1_last_name'],
                               writer_1_first_name=data['writer_1_first_name'],
                               writer_2_last_name=data['writer_2_last_name'],
                               writer_2_first_name=data['writer_2_first_name'],
                               writer_1_ipi_base_n=data['writer_1_ipi_base_n'],
                               writer_1_ipi_name_n=data['writer_1_ipi_name_n'],
                               writer_2_ipi_base_n=data['writer_2_ipi_base_n'],
                               writer_2_ipi_name_n=data['writer_2_ipi_name_n'],
                               iswc=data['iswc'],
                               duration=data['duration'])


class GroupHeaderDictionaryDecoder(Decoder):
    def __init__(self):
        super(GroupHeaderDictionaryDecoder, self).__init__()

    def decode(self, data):
        return GroupHeader(record_type=data['record_type'],
                           group_id=data['group_id'],
                           transaction_type=data['transaction_type'],
                           version_number=data['version_number'],
                           batch_request_id=data['batch_request_id'])


class GroupTrailerDictionaryDecoder(Decoder):
    def __init__(self):
        super(GroupTrailerDictionaryDecoder, self).__init__()

    def decode(self, data):
        return GroupTrailer(record_type=data['record_type'],
                            group_id=data['group_id'],
                            transaction_count=data['transaction_count'],
                            record_count=data['record_count'])


class InterestedPartyForAgreementDictionaryDecoder(Decoder):
    def __init__(self):
        super(InterestedPartyForAgreementDictionaryDecoder, self).__init__()

    def decode(self, data):
        return InterestedPartyForAgreementRecord(record_type=data['record_type'],
                                                 transaction_sequence_n=data['transaction_sequence_n'],
                                                 record_sequence_n=data['record_sequence_n'],
                                                 ip_n=data['ip_n'],
                                                 ip_last_name=data['ip_last_name'],
                                                 agreement_role_code=data['agreement_role_code'],
                                                 ip_writer_first_name=data['ip_writer_first_name'],
                                                 ipi_name_n=data['ipi_name_n'], ipi_base_n=data['ipi_base_n'],
                                                 pr_society=data['pr_society'], pr_share=data['pr_share'],
                                                 mr_society=data['mr_society'], mr_share=data['mr_share'],
                                                 sr_society=data['sr_society'], sr_share=data['sr_share'])


class IPTerritoryOfControlDictionaryDecoder(Decoder):
    def __init__(self):
        super(IPTerritoryOfControlDictionaryDecoder, self).__init__()

    def decode(self, data):
        return IPTerritoryOfControlRecord(record_type=data['record_type'],
                                          transaction_sequence_n=data['transaction_sequence_n'],
                                          record_sequence_n=data['record_sequence_n'],
                                          ip_n=data['ip_n'],
                                          inclusion_exclusion_indicator=data['inclusion_exclusion_indicator'],
                                          tis_numeric_code=data['tis_numeric_code'],
                                          sequence_n=data['sequence_n'],
                                          pr_collection_share=data['pr_collection_share'],
                                          mr_collection_share=data['mr_collection_share'],
                                          sr_collection_share=data['sr_collection_share'],
                                          shares_change=data['shares_change'])


class InstrumentationDetailDictionaryDecoder(Decoder):
    def __init__(self):
        super(InstrumentationDetailDictionaryDecoder, self).__init__()

    def decode(self, data):
        return InstrumentationDetailRecord(record_type=data['record_type'],
                                           transaction_sequence_n=data['transaction_sequence_n'],
                                           record_sequence_n=data['record_sequence_n'],
                                           instrument_code=data['instrument_code'],
                                           number_players=data['number_players'])


class InstrumentationSummaryDictionaryDecoder(Decoder):
    def __init__(self):
        super(InstrumentationSummaryDictionaryDecoder, self).__init__()

    def decode(self, data):
        return InstrumentationSummaryRecord(record_type=data['record_type'],
                                            transaction_sequence_n=data['transaction_sequence_n'],
                                            record_sequence_n=data['record_sequence_n'],
                                            number_voices=data['number_voices'],
                                            standard_instrumentation_type=data['standard_instrumentation_type'],
                                            instrumentation_description=data['instrumentation_description'])


class MessageDictionaryDecoder(Decoder):
    def __init__(self):
        super(MessageDictionaryDecoder, self).__init__()

    def decode(self, data):
        return MessageRecord(record_type=data['record_type'],
                             transaction_sequence_n=data['transaction_sequence_n'],
                             record_sequence_n=data['record_sequence_n'],
                             message_type=data['message_type'],
                             message_text=data['message_text'],
                             original_record_sequence_n=data['original_record_sequence_n'],
                             message_record_type=data['message_record_type'],
                             message_level=data['message_level'],
                             validation_n=data['validation_n'])


class PerformingArtistDictionaryDecoder(Decoder):
    def __init__(self):
        super(PerformingArtistDictionaryDecoder, self).__init__()

    def decode(self, data):
        return PerformingArtistRecord(record_type=data['record_type'],
                                      transaction_sequence_n=data['transaction_sequence_n'],
                                      record_sequence_n=data['record_sequence_n'],
                                      performing_artist_last_name=data['performing_artist_last_name'],
                                      performing_artist_first_name=data['performing_artist_first_name'],
                                      performing_artist_ipi_name_n=data['performing_artist_ipi_name_n'],
                                      performing_artist_ipi_base_n=data['performing_artist_ipi_base_n'])


class PublisherForWriterDictionaryDecoder(Decoder):
    def __init__(self):
        super(PublisherForWriterDictionaryDecoder, self).__init__()

    def decode(self, data):
        return PublisherForWriterRecord(record_type=data['record_type'],
                                        transaction_sequence_n=data['transaction_sequence_n'],
                                        record_sequence_n=data['record_sequence_n'],
                                        publisher_ip_n=data['publisher_ip_n'],
                                        writer_ip_n=data['writer_ip_n'],
                                        submitter_agreement_n=data['submitter_agreement_n'],
                                        society_assigned_agreement_n=data['society_assigned_agreement_n'])


class RecordingDetailDictionaryDecoder(Decoder):
    def __init__(self):
        super(RecordingDetailDictionaryDecoder, self).__init__()

    def decode(self, data):
        return RecordingDetailRecord(record_type=data['record_type'],
                                     transaction_sequence_n=data['transaction_sequence_n'],
                                     record_sequence_n=data['record_sequence_n'],
                                     first_release_date=data['first_release_date'],
                                     first_release_duration=data['first_release_duration'],
                                     first_album_title=data['first_album_title'],
                                     first_album_label=data['first_album_label'],
                                     first_release_catalog_n=data['first_release_catalog_n'],
                                     ean=data['ean'],
                                     isrc=data['isrc'],
                                     recording_format=data['recording_format'],
                                     recording_technique=data['recording_technique'],
                                     media_type=data['media_type'])


class FileDictionaryDecoder(Decoder):
    def __init__(self):
        super(FileDictionaryDecoder, self).__init__()

        self._tag_decoder = FileTagDictionaryDecoder()
        self._transmission_decoder = TransmissionDictionaryDecoder()

    def decode(self, data):
        tag = data['tag']
        if isinstance(tag, dict):
            tag = self._tag_decoder.decode(tag)

        transmission = data['transmission']
        if isinstance(transmission, dict):
            transmission = self._transmission_decoder.decode(transmission)

        return CWRFile(tag, transmission)


class TransmissionDictionaryDecoder(Decoder):
    def __init__(self):
        super(TransmissionDictionaryDecoder, self).__init__()

        self._header_decoder = TransmissionHeaderDictionaryDecoder()
        self._trailer_decoder = TransmissionTrailerDictionaryDecoder()
        self._group_decoder = GroupDictionaryDecoder()

    def decode(self, data):
        header = data['header']
        if isinstance(header, dict):
            header = self._header_decoder.decode(header)

        trailer = data['trailer']
        if isinstance(trailer, dict):
            trailer = self._trailer_decoder.decode(trailer)

        groups = []
        if len(data['groups']) > 0:
            if isinstance(data['groups'][0], dict):
                for group in data['groups']:
                    groups.append(self._group_decoder.decode(group))
            else:
                groups = data['groups']

        return Transmission(header, trailer, groups)


class GroupDictionaryDecoder(Decoder):
    def __init__(self):
        super(GroupDictionaryDecoder, self).__init__()

        self._header_decoder = GroupHeaderDictionaryDecoder()
        self._trailer_decoder = GroupTrailerDictionaryDecoder()
        self._transaction_decoder = TransactionRecordDictionaryDecoder()

    def decode(self, data):
        header = data['group_header']
        if isinstance(header, dict):
            header = self._header_decoder.decode(header)

        trailer = data['group_trailer']
        if isinstance(trailer, dict):
            trailer = self._trailer_decoder.decode(trailer)

        transactions = []
        if len(data['transactions']) > 0:
            if isinstance(data['transactions'][0][0], dict):
                for transaction in data['transactions']:
                    transaction_records = []
                    for record in transaction:
                        transaction_records.append(self._transaction_decoder.decode(record))
                    transactions.append(transaction_records)
            else:
                transactions = data['transactions']

        return Group(header, trailer, transactions)


class TransmissionHeaderDictionaryDecoder(Decoder):
    def __init__(self):
        super(TransmissionHeaderDictionaryDecoder, self).__init__()

    def decode(self, data):
        return TransmissionHeader(record_type=data['record_type'],
                                  sender_id=data['sender_id'],
                                  sender_name=data['sender_name'],
                                  sender_type=data['sender_type'],
                                  creation_date_time=data['creation_date_time'],
                                  transmission_date=data['transmission_date'],
                                  edi_standard=data['edi_standard'],
                                  character_set=data['character_set'])


class TransmissionTrailerDictionaryDecoder(Decoder):
    def __init__(self):
        super(TransmissionTrailerDictionaryDecoder, self).__init__()

    def decode(self, data):
        return TransmissionTrailer(record_type=data['record_type'],
                                   group_count=data['group_count'],
                                   transaction_count=data['transaction_count'],
                                   record_count=data['record_count'])


class WorkDictionaryDecoder(Decoder):
    def __init__(self):
        super(WorkDictionaryDecoder, self).__init__()

    def decode(self, data):
        return WorkRecord(record_type=data['record_type'],
                          transaction_sequence_n=data['transaction_sequence_n'],
                          record_sequence_n=data['record_sequence_n'],
                          submitter_work_n=data['submitter_work_n'],
                          title=data['title'],
                          version_type=data['version_type'],
                          musical_work_distribution_category=data['musical_work_distribution_category'],
                          date_publication_printed_edition=data['date_publication_printed_edition'],
                          text_music_relationship=data['text_music_relationship'],
                          language_code=data['language_code'],
                          copyright_number=data['copyright_number'],
                          copyright_date=data['copyright_date'],
                          music_arrangement=data['music_arrangement'],
                          lyric_adaptation=data['lyric_adaptation'],
                          excerpt_type=data['excerpt_type'],
                          composite_type=data['composite_type'],
                          composite_component_count=data['composite_component_count'],
                          iswc=data['iswc'],
                          work_type=data['work_type'],
                          duration=data['duration'],
                          catalogue_number=data['catalogue_number'],
                          opus_number=data['opus_number'],
                          contact_id=data['contact_id'],
                          contact_name=data['contact_name'],
                          recorded_indicator=data['recorded_indicator'],
                          priority_flag=data['priority_flag'],
                          exceptional_clause=data['exceptional_clause'],
                          grand_rights_indicator=data['grand_rights_indicator'])


class WorkOriginDictionaryDecoder(Decoder):
    def __init__(self):
        super(WorkOriginDictionaryDecoder, self).__init__()

    def decode(self, data):
        return WorkOriginRecord(record_type=data['record_type'],
                                transaction_sequence_n=data['transaction_sequence_n'],
                                record_sequence_n=data['record_sequence_n'],
                                intended_purpose=data['intended_purpose'],
                                production_title=data['production_title'],
                                cd_identifier=data['cd_identifier'],
                                cut_number=data['cut_number'],
                                library=data['library'],
                                bltvr=data['bltvr'],
                                visan=data['visan'],
                                production_n=data['production_n'],
                                episode_title=data['episode_title'],
                                episode_n=data['episode_n'],
                                year_production=data['year_production'],
                                audio_visual_key=data['audio_visual_key'])


class WriterDictionaryDecoder(Decoder):
    def __init__(self):
        super(WriterDictionaryDecoder, self).__init__()

    def decode(self, data):
        return Writer(ip_n=data['ip_n'],
                      personal_number=data['personal_number'],
                      ipi_base_n=data['ipi_base_n'],
                      writer_first_name=data['writer_first_name'],
                      writer_last_name=data['writer_last_name'],
                      tax_id=data['tax_id'],
                      ipi_name_n=data['ipi_name_n'])


class WriterRecordDictionaryDecoder(Decoder):
    def __init__(self):
        super(WriterRecordDictionaryDecoder, self).__init__()
        self._writer_decoder = WriterDictionaryDecoder()

    def decode(self, data):
        writer = self._writer_decoder.decode(data)

        return WriterRecord(record_type=data['record_type'],
                            transaction_sequence_n=data['transaction_sequence_n'],
                            record_sequence_n=data['record_sequence_n'],
                            writer=writer,
                            writer_designation=data['writer_designation'],
                            work_for_hire=data['work_for_hire'],
                            writer_unknown=data['writer_unknown'],
                            reversionary=data['reversionary'],
                            first_recording_refusal=data['first_recording_refusal'],
                            usa_license=data['usa_license'],
                            pr_society=data['pr_society'],
                            pr_ownership_share=data['pr_ownership_share'],
                            mr_society=data['mr_society'],
                            mr_ownership_share=data['mr_ownership_share'],
                            sr_society=data['sr_society'],
                            sr_ownership_share=data['sr_ownership_share'])


class NonRomanAlphabetAgreementPartyDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetAgreementPartyDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetAgreementPartyRecord(record_type=data['record_type'],
                                                    transaction_sequence_n=data['transaction_sequence_n'],
                                                    record_sequence_n=data['record_sequence_n'],
                                                    ip_name=data['ip_name'],
                                                    ip_writer_name=data['ip_writer_name'],
                                                    ip_n=data['ip_n'],
                                                    language_code=data['language_code'])


class NonRomanAlphabetOtherWriterDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetOtherWriterDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetOtherWriterRecord(record_type=data['record_type'],
                                                 transaction_sequence_n=data['transaction_sequence_n'],
                                                 record_sequence_n=data['record_sequence_n'],
                                                 writer_first_name=data['writer_first_name'],
                                                 writer_name=data['writer_name'],
                                                 position=data['position'],
                                                 language_code=data['language_code'])


class NonRomanAlphabetPerformanceDataDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetPerformanceDataDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetPerformanceDataRecord(record_type=data['record_type'],
                                                     transaction_sequence_n=data['transaction_sequence_n'],
                                                     record_sequence_n=data['record_sequence_n'],
                                                     performing_artist_first_name=data['performing_artist_first_name'],
                                                     performing_artist_name=data['performing_artist_name'],
                                                     performing_artist_ipi_name_n=data['performing_artist_ipi_name_n'],
                                                     performing_artist_ipi_base_n=data['performing_artist_ipi_base_n'],
                                                     language_code=data['language_code'],
                                                     performance_language=data['performance_language'],
                                                     performance_dialect=data['performance_dialect'])


class NonRomanAlphabetPublisherNameDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetPublisherNameDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetPublisherNameRecord(record_type=data['record_type'],
                                                   transaction_sequence_n=data['transaction_sequence_n'],
                                                   record_sequence_n=data['record_sequence_n'],
                                                   publisher_sequence_n=data['publisher_sequence_n'],
                                                   ip_n=data['ip_n'],
                                                   publisher_name=data['publisher_name'],
                                                   language_code=data['language_code'])


class NonRomanAlphabetTitleDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetTitleDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetTitleRecord(record_type=data['record_type'],
                                           transaction_sequence_n=data['transaction_sequence_n'],
                                           record_sequence_n=data['record_sequence_n'],
                                           title=data['title'],
                                           title_type=data['title_type'],
                                           language_code=data['language_code'])


class NonRomanAlphabetWorkDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetWorkDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetWorkRecord(record_type=data['record_type'],
                                          transaction_sequence_n=data['transaction_sequence_n'],
                                          record_sequence_n=data['record_sequence_n'],
                                          title=data['title'],
                                          language_code=data['language_code'])


class NonRomanAlphabetWriterNameDictionaryDecoder(Decoder):
    def __init__(self):
        super(NonRomanAlphabetWriterNameDictionaryDecoder, self).__init__()

    def decode(self, data):
        return NonRomanAlphabetWriterNameRecord(record_type=data['record_type'],
                                                transaction_sequence_n=data['transaction_sequence_n'],
                                                record_sequence_n=data['record_sequence_n'],
                                                writer_first_name=data['writer_first_name'],
                                                writer_last_name=data['writer_last_name'],
                                                ip_n=data['ip_n'],
                                                language_code=data['language_code'])


class PublisherDictionaryDecoder(Decoder):
    def __init__(self):
        super(PublisherDictionaryDecoder, self).__init__()

    def decode(self, data):
        return Publisher(ip_n=data['ip_n'],
                         publisher_name=data['publisher_name'],
                         ipi_name_n=data['ipi_name_n'],
                         ipi_base_n=data['ipi_base_n'],
                         tax_id=data['tax_id'])


class PublisherRecordDictionaryDecoder(Decoder):
    def __init__(self):
        super(PublisherRecordDictionaryDecoder, self).__init__()
        self._publisher_decoder = PublisherDictionaryDecoder()

    def decode(self, data):
        publisher = self._publisher_decoder.decode(data)

        return PublisherRecord(record_type=data['record_type'], transaction_sequence_n=data['transaction_sequence_n'],
                               record_sequence_n=data['record_sequence_n'],
                               publisher=publisher, publisher_sequence_n=data['publisher_sequence_n'],
                               submitter_agreement_n=data['submitter_agreement_n'],
                               publisher_type=data['publisher_type'],
                               publisher_unknown=data['publisher_unknown'], agreement_type=data['agreement_type'],
                               international_standard_code=data['international_standard_code'],
                               society_assigned_agreement_n=data['society_assigned_agreement_n'],
                               pr_society=data['pr_society'],
                               pr_ownership_share=data['pr_ownership_share'],
                               mr_society=data['mr_society'], mr_ownership_share=data['mr_ownership_share'],
                               sr_society=data['sr_society'],
                               sr_ownership_share=data['sr_ownership_share'],
                               special_agreements=data['special_agreements'],
                               first_recording_refusal=data['first_recording_refusal'],
                               usa_license=data['usa_license'])


class TableValueDictionaryDecoder(Decoder):
    def __init__(self):
        super(TableValueDictionaryDecoder, self).__init__()

    def decode(self, data):
        return TableValue(code=data['code'],
                          name=data['name'],
                          description=data['description'])


class MediaTypeValueDictionaryDecoder(Decoder):
    def __init__(self):
        super(MediaTypeValueDictionaryDecoder, self).__init__()

    def decode(self, data):
        return MediaTypeValue(code=data['code'],
                              name=data['name'],
                              media_type=data['media_type'],
                              duration_max=data['duration_max'],
                              works_max=data['works_max'],
                              fragments_max=data['fragments_max'])


class InstrumentValueDictionaryDecoder(Decoder):
    def __init__(self):
        super(InstrumentValueDictionaryDecoder, self).__init__()

    def decode(self, data):
        return InstrumentValue(code=data['code'],
                               name=data['name'],
                               family=data['family'],
                               description=data['description'])


class FileTagDictionaryDecoder(Decoder):
    def __init__(self):
        super(FileTagDictionaryDecoder, self).__init__()

    def decode(self, data):
        return FileTag(data['year'],
                       data['sequence_n'],
                       data['sender'],
                       data['receiver'],
                       data['version'])


class AVIKeyDictionaryDecoder(Decoder):
    def __init__(self):
        super(AVIKeyDictionaryDecoder, self).__init__()

    def decode(self, data):
        return AVIKey(data['society_code'],
                      data['av_number'])


class IPIBaseDictionaryDecoder(Decoder):
    def __init__(self):
        super(IPIBaseDictionaryDecoder, self).__init__()

    def decode(self, data):
        return IPIBaseNumber(data['header'],
                             data['id_code'],
                             data['check_digit'])


class ISWCDictionaryDecoder(Decoder):
    def __init__(self):
        super(ISWCDictionaryDecoder, self).__init__()

    def decode(self, data):
        return ISWCCode(data['id_code'],
                        data['check_digit'])


class VISANDictionaryDecoder(Decoder):
    def __init__(self):
        super(VISANDictionaryDecoder, self).__init__()

    def decode(self, data):
        return VISAN(data['version'],
                     data['isan'],
                     data['episode'],
                     data['check_digit'])
