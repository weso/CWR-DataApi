# -*- coding: utf-8 -*-

import sys

from cwr.agreement import AgreementInterestedParty, AgreementRecord, AgreementTerritoryRecord
from cwr.info import AdditionalRelatedInfoRecord
from cwr.interested_party import IPTerritoryRecord, PublisherRecord, WriterPublisherRecord, WriterRecord
from cwr.work import WorkRecord, ComponentRecord, AuthoredWorkRecord, AlternateTitleRecord, \
    RecordingDetailRecord, InstrumentationDetailRecord, WorkOriginRecord, InstrumentationSummaryRecord, \
    PerformingArtistRecord
from cwr.nra import NPARecord, NPNRecord, NWNRecord, NATRecord, NRARecordWork, NOWRecord, NPRRecord


"""
This is a small tool to print a CWR file contents on the console.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRPrinter():
    """
    Prints the contents of a CWR file on the console.
    """

    def __init__(self):
        pass

    def print_transmission(self, transmission, file):
        # TODO: Add support for Acknowledgement

        out_old = sys.stdout
        sys.stdout = file

        print('CWR Transmission begins')
        print('Contains %s groups' % (len(transmission.groups)))
        print('------------------------------')
        self.print_transmission_header(transmission.header)
        print('------------------------------')
        self.print_transmission_trailer(transmission.trailer)
        i = 1
        for group in transmission.groups:
            print(' ')
            print('------------------------------')
            print('******************************')
            print('*           GROUP            *')
            print('******************************')
            print('------------------------------')
            print(' ')
            print('------------------------------')
            print('Group %s' % (i))
            print('Contains %s transactions' % (len(group.transactions)))
            print('------------------------------')
            self.print_group_header(group.group_header)
            print('------------------------------')
            self.print_group_trailer(group.group_trailer)

            for transaction in group.transactions:
                print(' ')
                print('------------------------------')
                print('******************************')
                print('*        TRANSACTION         *')
                print('******************************')
                print('------------------------------')
                for record in transaction:
                    print(' ')
                    self.print_transaction_record(record)
            i += 1

        sys.stdout = out_old

    def print_transmission_header(self, header):
        print('CWR Transmission Header')
        print('Record Type: %s' % (header.record_type))
        print('Sender ID: %s' % (header.sender_id))
        print('Sender Name: %s' % (header.sender_name))
        print('Sender Type: %s' % (header.sender_type))
        print('Created on: %s' % (header.creation_date_time))
        print('Sent on: %s' % (header.transmission_date))
        print('EDI standard: %s' % (header.edi_standard))
        print('Character set: %s' % (header.character_set))

    def print_transmission_trailer(self, trailer):
        print('CWR Transmission Trailer')
        print('Record Type: %s' % (trailer.record_type))
        print('Group Count: %s' % (trailer.group_count))
        print('Transaction Count: %s' % (trailer.transaction_count))
        print('Record Count: %s' % (trailer.record_count))

    def print_group_header(self, header):
        print('CWR Group Header')
        print('Record Type: %s' % (header.record_type))
        print('Group ID: %s' % (header.group_id))
        print('Transaction Type: %s' % (header.transaction_type))
        print('Version Number: %s' % (header.version_number))
        print('Batch Request ID: %s' % (header.batch_request_id))

    def print_group_trailer(self, trailer):
        print('CWR Group Trailer')
        print('Record Type: %s' % (trailer.record_type))
        print('Group ID: %s' % (trailer.group_id))
        print('Transaction Count: %s' % (trailer.transaction_count))
        print('Record Count: %s' % (trailer.record_count))

    def print_transaction_record(self, record):
        print('Record Type: %s' % (record.record_type))
        print('Transaction Sequence Number: %s' % (record.transaction_sequence_n))
        print('Record Sequence Number: %s' % (record.record_sequence_n))

        if (isinstance(record, AgreementInterestedParty)):
            self.print_ipa(record)
        elif (isinstance(record, NPARecord)):
            self.print_npa(record)
        elif (isinstance(record, AgreementRecord)):
            self.print_agr(record)
        elif (isinstance(record, AgreementTerritoryRecord)):
            self.print_ter(record)
        elif (isinstance(record, AdditionalRelatedInfoRecord)):
            self.print_ari(record)
        elif (isinstance(record, NPNRecord)):
            self.print_npn(record)
        elif (isinstance(record, IPTerritoryRecord)):
            self.print_ipter(record)
        elif (isinstance(record, PublisherRecord)):
            self.print_pubr(record)
        elif (isinstance(record, WriterPublisherRecord)):
            self.print_pwr(record)
        elif (isinstance(record, WriterRecord)):
            self.print_writr(record)
        elif (isinstance(record, NWNRecord)):
            self.print_nwn(record)
        elif (isinstance(record, WorkRecord)):
            self.print_workr(record)
        elif (isinstance(record, ComponentRecord)):
            self.print_com(record)
        elif (isinstance(record, AuthoredWorkRecord)):
            self.print_authr(record)
        elif (isinstance(record, AlternateTitleRecord)):
            self.print_alt(record)
        elif (isinstance(record, NATRecord)):
            self.print_nat(record)
        elif (isinstance(record, RecordingDetailRecord)):
            self.print_rec(record)
        elif (isinstance(record, InstrumentationDetailRecord)):
            self.print_ind(record)
        elif (isinstance(record, WorkOriginRecord)):
            self.print_orn(record)
        elif (isinstance(record, InstrumentationSummaryRecord)):
            self.print_ins(record)
        elif (isinstance(record, PerformingArtistRecord)):
            self.print_per(record)
        elif (isinstance(record, NOWRecord)):
            self.print_now(record)
        elif (isinstance(record, NPRRecord)):
            self.print_npr(record)
        elif (isinstance(record, NRARecordWork)):
            self.print_nra(record)

    def print_ipa(self, record):
        print('IP Number: %s' % (record.ip_n))
        print('Writer Name: %s' % (record.ip_writer_first_name))
        print('Last Name: %s' % (record.ip_last_name))
        print('Agreement Role Code: %s' % (record.agreement_role_code))
        print('IPI Name Number: %s' % (record.ipi_name_n))
        print('IPI Base Number: %s' % (record.ipi_base_n))
        print('PR Society: %s' % (record.pr_society))
        print('PR Shares: %s' % (record.pr_share))
        print('MR Shares: %s' % (record.mr_society))
        print('MR Shares: %s' % (record.mr_share))
        print('SR Shares: %s' % (record.sr_society))
        print('SR Shares: %s' % (record.sr_share))

    def print_npa(self, record):
        print('IP Number: %s' % (record.ip_n))
        print('Writer Name: %s' % (record.ip_writer_name))
        print('Name: %s' % (record.ip_name))
        print('Language: %s' % (record.language_code))

    def print_agr(self, record):
        print('Agreement Number: %s' % (record.submitter_agreement_n))
        print('Society Assigned Agreement Number: %s' % (record.society_assigned_agreement_n))
        print('International Standard Code: %s' % (record.international_standard_code))
        print('Agreement Type: %s' % (record.agreement_type))
        print('Start Date: %s' % (record.agreement_start_date))
        print('End Date: %s' % (record.agreement_end_date))
        print('Signature Date: %s' % (record.date_of_signature))
        print('Works Number: %s' % (record.number_of_works))
        print('Prior Royalty Status: %s' % (record.prior_royalty_status))
        print('Prior Royalty Start Date: %s' % (record.prior_royalty_start_date))
        print('Post-Term Collection Status: %s' % (record.post_term_collection_status))
        print('Post-Term Collection End Date: %s' % (record.post_term_collection_end_date))
        print('Retention End Date: %s' % (record.retention_end_date))
        print('Sales/Manufacture Clause: %s' % (record.sales_manufacture_clause))
        print('Shares Change: %s' % (record.shares_change))
        print('Advance Given: %s' % (record.advance_given))

    def print_ter(self, record):
        print('TIS Code: %s' % (record.tis_numeric_code))
        print('Inclusion/Exclusion Indicator: %s' % (record.inclusion_exclusion_indicator))

    def print_ari(self, record):
        print('Work Number: %s' % (record.submitter_work_n))
        print('Society Number: %s' % (record.society_n))
        print('Subject Code: %s' % (record.subject_code))
        print('Type of Right: %s' % (record.type_of_right))
        print('Note: %s' % (record.note))

    def print_npn(self, record):
        print('Interested Party Number: %s' % (record.ip_n))
        print('Publisher Sequence Number: %s' % (record.publisher_sequence_n))
        print('Name: %s' % (record.publisher_name))
        print('Language: %s' % (record.language_code))

    def print_ipter(self, record):
        print('Interested Party Number: %s' % (record.ip_n))
        print('Inclusion/Exclusion Indicator: %s' % (record.ie_indicator))
        print('TIS: %s' % (record.tis_numeric_code))
        print('Sequence Number: %s' % (record.sequence_n))
        print('PR collection share: %s' % (record.pr_col_share))
        print('MR collection share: %s' % (record.mr_col_share))
        print('SR collection share: %s' % (record.sr_col_share))
        print('Shares Change: %s' % (record.shares_change))

    def print_pubr(self, record):
        print('Publisher Number: %s' % (record.publisher.ip_n))
        print('Name: %s' % (record.publisher.publisher_name))
        print('Unknown: %s' % (record.publisher_unknown))
        print('IPI Base: %s' % (record.publisher.ipi_base_n))
        print('IPI Name: %s' % (record.publisher.ipi_name_n))
        print('Tax ID: %s' % (record.publisher.tax_id))
        print('Sequence Number: %s' % (record.publisher_sequence_n))
        print('Publisher Type: %s' % (record.publisher_type))
        print('Agreement Number: %s' % (record.submitter_agreement_n))
        print('Society Agreement Number: %s' % (record.society_assigned_agreement_n))
        print('Agreement Type: %s' % (record.agreement_type))
        print('ISAC: %s' % (record.isac))
        print('Special Agreements Indicator: %s' % (record.special_agreements))
        print('First Record Refusal Indicator: %s' % (record.first_recording_refusal))
        print('USA License: %s' % (record.usa_license))
        print('PR Society: %s' % (record.pr_society))
        print('PR Owner Share: %s' % (record.pr_ownership_share))
        print('MR Society: %s' % (record.mr_society))
        print('MR Owner Share: %s' % (record.mr_ownership_share))
        print('SR Society: %s' % (record.sr_society))
        print('SR Owner Share: %s' % (record.sr_ownership_share))

    def print_pwr(self, record):
        print('Publisher IP Number: %s' % (record.publisher_ip_number))
        print('writer IP Number: %s' % (record.publisher_ip_number))
        print('Submitter Agreement Number: %s' % (record.submitter_agreement_n))
        print('Society-Assigned Agreement Number: %s' % (record.society_assigned_agreement_n))

    def print_writr(self, record):
        print('writer Number: %s' % (record.writer.ip_n))
        print('Personal Number: %s' % (record.writer.personal_number))
        print('First Name: %s' % (record.writer.writer_first_name))
        print('Last Name: %s' % (record.writer.writer_last_name))
        print('Unknown: %s' % (record.writer_unknown))
        print('IPI Base: %s' % (record.writer.ipi_base_n))
        print('IPI Name: %s' % (record.writer.ipi_name_n))
        print('Tax ID: %s' % (record.writer.tax_id))
        print('writer Designation Code: %s' % (record.writer_designation))
        print('Work For Hire Indicator: %s' % (record.work_for_hire))
        print('Reversionary Indicator: %s' % (record.reversionary))
        print('First Record Refusal Indicator: %s' % (record.first_recording_refusal))
        print('USA License: %s' % (record.usa_license))
        print('PR Society: %s' % (record.pr_society))
        print('PR Owner Share: %s' % (record.pr_ownership_share))
        print('MR Society: %s' % (record.mr_society))
        print('MR Owner Share: %s' % (record.mr_ownership_share))
        print('SR Society: %s' % (record.sr_society))
        print('SR Owner Share: %s' % (record.sr_ownership_share))

    def print_nwn(self, record):
        print('Interested Party Number: %s' % (record.ip_n))
        print('First Name: %s' % (record.writer_first_name))
        print('Last Name: %s' % (record.ip_last_name))
        print('Language: %s' % (record.language_code))

    def print_workr(self, record):
        print('Submitter Work Number: %s' % (record.submitter_work_n))
        print('ISWC: %s' % (record.iswc))
        print('Title: %s' % (record.title))
        print('CWR Work Type: %s' % (record.cwr_work_type))
        print('Catalogue Number: %s' % (record.catalogue_number))
        print('Opus Number: %s' % (record.opus_number))
        print('Duration: %s' % (record.duration))
        print('Printed Edition Publication Date: %s' % (record.date_publication_printed_edition))
        print('Language: %s' % (record.language_code))
        print('Copyright Number: %s' % (record.copyright_number))
        print('Copyright Date: %s' % (record.copyright_date))
        print('Musical Distribution Category: %s' % (record.musical_work_distribution_category))
        print('Version Type: %s' % (record.version_type))
        print('Text-Music Relationship: %s' % (record.text_music_relationship))
        print('Music Arrangement: %s' % (record.music_arrangement))
        print('Lyric Adaptation: %s' % (record.lyric_adaptation))
        print('Excerpt Type: %s' % (record.excerpt_type))
        print('Composite Type: %s' % (record.composite_type))
        print('Composite Component Count: %s' % (record.composite_component_count))
        print('Recorded Indicator: %s' % (record.recorded_indicator))
        print('Priority Flag: %s' % (record.priority_flag))
        print('Exceptional Clause: %s' % (record.exceptional_clause))
        print('Grand Rights Indicator: %s' % (record.grand_rights_indicator))
        print('Contact ID: %s' % (record.contact_id))
        print('Contact Name: %s' % (record.contact_name))

    def print_com(self, record):
        print('Submitter Given Number: %s' % (record.submitter_creation_n))
        print('ISWC: %s' % (record.iswc))
        print('Title: %s' % (record.creation_title))
        print('Duration: %s' % (record.duration))
        print('First Name Writer 1: %s' % (record.writer_1_first_name))
        print('Last Name Writer 1: %s' % (record.writer_1_last_name))
        print('IPI Base Writer 1: %s' % (record.writer_1_ipi_base))
        print('IPI Name Writer 1: %s' % (record.writer_1_ipi_name))
        print('First Name Writer 2: %s' % (record.writer_2_first_name))
        print('Last Name Writer 2: %s' % (record.writer_2_last_name))
        print('IPI Base Writer 2: %s' % (record.writer_2_ipi_base))
        print('IPI Name Writer 2: %s' % (record.writer_2_ipi_name))

    def print_authr(self, record):
        print('Work Number: %s' % (record.submitter_work_n))
        print('ISWC: %s' % (record.iswc))
        print('Title: %s' % (record.title))
        print('Language: %s' % (record.language_code))
        print('Source: %s' % (record.source))
        print('First Name Writer 1: %s' % (record.writer_1_first_name))
        print('Last Name Writer 1: %s' % (record.writer_1_last_name))
        print('IPI Base Writer 1: %s' % (record.writer_1_ipi_base))
        print('IPI Name Writer 1: %s' % (record.writer_1_ipi_name))
        print('First Name Writer 2: %s' % (record.writer_2_first_name))
        print('Last Name Writer 2: %s' % (record.writer_2_last_name))
        print('IPI Base Writer 2: %s' % (record.writer_2_ipi_base))
        print('IPI Name Writer 2: %s' % (record.writer_2_ipi_name))

    def print_alt(self, record):
        print('Alternate Title: %s' % (record.alternate_title))
        print('Title Type: %s' % (record.title_type))
        print('Language: %s' % (record.language_code))

    def print_nat(self, record):
        print('Title: %s' % (record.creation_title))
        print('Title Type: %s' % (record.title_type))
        print('Language: %s' % (record.language_code))

    def print_rec(self, record):
        print('EAN: %s' % (record.ean))
        print('ISRC: %s' % (record.isrc))
        print('First Album Title: %s' % (record.first_album_title))
        print('First Album Label: %s' % (record.first_album_label))
        print('First Release Catalog ID: %s' % (record.first_release_catalog_n))
        print('First Release Date: %s' % (record.first_release_date))
        print('First Release Duration: %s' % (record.first_release_duration))
        print('Recording Format: %s' % (record.recording_format))
        print('Recording Technique: %s' % (record.recording_technique))
        print('Media Type: %s' % (record.media_type))

    def print_ins(self, record):
        print('Number of Voices: %s' % (record.number_voices))
        print('Instrumentation Type: %s' % (record.instr_type))
        print('Description: %s' % (record.instrumentation_description))

    def print_ind(self, record):
        print('Instrument Code: %s' % (record.instrument_code))
        print('Players: %s' % (record.number_players))

    def print_orn(self, record):
        print('Production Number: %s' % (record.production_n))
        print('Production Title: %s' % (record.production_title))
        print('Production Year: %s' % (record.year_production))
        print('Intended Purpose: %s' % (record.intended_purpose))
        print('CD Identifier: %s' % (record.cd_identifier))
        print('Cut Number: %s' % (record.cut_number))
        print('Episode Number: %s' % (record.episode_n))
        print('Episode Title: %s' % (record.episode_title))
        print('Library: %s' % (record.library))
        print('BLTVR: %s' % (record.bltvr))
        print('AVI: %s' % (record.audio_visual_key))
        print('V-ISAN: %s' % (record.visan))

    def print_per(self, record):
        print('IPI Name: %s' % (record.performing_artist_ipi_name_n))
        print('IPI Base: %s' % (record.performing_artist_ipi_base_n))
        print('First Name: %s' % (record.performing_artist_first_name))
        print('Last Name: %s' % (record.performing_artist_last_name))

    def print_nra(self, record):
        print('Title: %s' % (record.creation_title))
        print('Language: %s' % (record.language_code))

    def print_now(self, record):
        print('First Name: %s' % (record.writer_first_name))
        print('Name: %s' % (record.publisher_name))
        print('Position: %s' % (record.position))
        print('Language: %s' % (record.language_code))

    def print_npr(self, record):
        print('First Name: %s' % (record.writer_first_name))
        print('Name: %s' % (record.publisher_name))
        print('IPI Name: %s' % (record.ipi_name_n))
        print('IPI Base: %s' % (record.ipi_base_n))
        print('Language: %s' % (record.language_code))
        print('Performance Language: %s' % (record.performance_language))
        print('Performance Dialect: %s' % (record.performance_dialect))