# -*- coding: utf-8 -*-

from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.agreement import InterestedPartyForAgreementRecord, AgreementRecord, AgreementTerritoryRecord
from cwr.group import GroupHeader, GroupTrailer
from cwr.info import AdditionalRelatedInfoRecord
from cwr.interested_party import IPTerritoryOfControlRecord

from cwr.parser.common import Encoder
from cwr.interested_party import Publisher, PublisherRecord, Writer, PublisherForWriterRecord, WriterRecord
from cwr.nra import NRAWorkRecord, NATRecord, NOWRecord, NPARecord, NPNRecord, NPRRecord, NWNRecord


"""
Offers classes to parse CWR objects from and into dictionaries.

This helps for example to create JSON or Mongo objects.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class CWRDictionaryEncoder(Encoder):
    """
    Encodes CWR model classes into dictionaries.
    """

    def __init__(self):
        super(CWRDictionaryEncoder, self).__init__()

    def encode(self, object):
        if isinstance(object, AcknowledgementRecord):
            # Acknowledgement
            encoded = self.__encode_acknowledgement_record(object)
        elif isinstance(object, AdditionalRelatedInfoRecord):
            # Additional Related Info
            encoded = self.__encode_additional_related_info_record(object)
        elif isinstance(object, AgreementRecord):
            # Agreement
            encoded = self.__encode_agreement_record(object)
        elif isinstance(object, AgreementTerritoryRecord):
            # Agreement Territory
            encoded = self.__encode_agreement_territory_record(object)
        elif isinstance(object, GroupHeader):
            # Group Header
            encoded = self.__encode_group_header(object)
        elif isinstance(object, GroupTrailer):
            # Group Trailer
            encoded = self.__encode_group_trailer(object)
        elif isinstance(object, InterestedPartyForAgreementRecord):
            # Interested Party for Agreement
            encoded = self.__encode_interested_party_agreement_record(object)
        elif isinstance(object, IPTerritoryOfControlRecord):
            # Interested Party (Writer/Publisher) Territory of Control
            encoded = self.__encode_interested_party_territory_control_record(object)
        elif isinstance(object, MessageRecord):
            # Message
            encoded = self.__encode_message_record(object)
        elif isinstance(object, NATRecord):
            # NAT Record
            encoded = self.__encode_nat_record(object)
        elif isinstance(object, NOWRecord):
            # NOW Record
            encoded = self.__encode_now_record(object)
        elif isinstance(object, NPARecord):
            # NPA Record
            encoded = self.__encode_npa_record(object)
        elif isinstance(object, NPNRecord):
            # NPN Record
            encoded = self.__encode_npn_record(object)
        elif isinstance(object, NPRRecord):
            # NPR Record
            encoded = self.__encode_npr_record(object)
        elif isinstance(object, NRAWorkRecord):
            # NRA Record for Works
            encoded = self.__encode_nra_work_record(object)
        elif isinstance(object, NWNRecord):
            # NWN Record for Works
            encoded = self.__encode_nwn_record(object)
        elif isinstance(object, Publisher):
            # Publisher IP
            encoded = self.__encode_publisher(object)
        elif isinstance(object, PublisherForWriterRecord):
            # Publisher For Writer
            encoded = self.__encode_publisher_for_writer_record(object)
        elif isinstance(object, PublisherRecord):
            # Publisher
            encoded = self.__encode_publisher_record(object)
        elif isinstance(object, Writer):
            # Writer IP
            encoded = self.__encode_writer(object)
        elif isinstance(object, WriterRecord):
            # Writer
            encoded = self.__encode_writer_record(object)
        else:
            encoded = None

        return encoded

    def __encode_transaction_record_head(self, record):
        """
        Creates the head of a transaction record.

        :param record: the record with the head to transform into a dictionary
        :return: a dictionary created from the record head
        """
        encoded = {}

        encoded['record_type'] = record.record_type
        encoded['transaction_sequence_n'] = record.transaction_sequence_n
        encoded['record_sequence_n'] = record.record_sequence_n

        return encoded

    def __encode_interested_party(self, record):
        """
        Creates a dictionary from an InterestedParty.

        :param record: the InterestedParty to transform into a dictionary
        :return: a dictionary created from the InterestedParty
        """
        encoded = {}

        encoded['ip_n'] = record.ip_n
        encoded['ipi_base_n'] = record.ipi_base_n
        encoded['ipi_name_n'] = record.ipi_name_n
        encoded['tax_id'] = record.tax_id

        return encoded

    def __encode_interested_party_record(self, record):
        """
        Creates a dictionary from a InterestedPartyRecord.

        :param record: the InterestedPartyRecord to transform into a dictionary
        :return: a dictionary created from the InterestedPartyRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['first_recording_refusal'] = record.first_recording_refusal
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['mr_society'] = record.mr_society
        encoded['mr_ownership_share'] = record.mr_ownership_share
        encoded['sr_society'] = record.sr_society
        encoded['sr_ownership_share'] = record.sr_ownership_share
        encoded['usa_license'] = record.usa_license

        return encoded

    def __encode_nra_record(self, record):
        """
        Creates a dictionary from a NRARecord.

        :param record: the NRARecord to transform into a dictionary
        :return: a dictionary created from the NRARecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['language_code'] = record.language_code

        return encoded

    def __encode_acknowledgement_record(self, record):
        """
        Creates a dictionary from an AcknowledgementRecord.

        :param record: the AcknowledgementRecord to transform into a dictionary
        :return: a dictionary created from the AcknowledgementRecord
        """
        encoded = self.__encode_transaction_record_head(record)

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

    def __encode_additional_related_info_record(self, record):
        """
        Creates a dictionary from an AdditionalRelatedInfoRecord.

        :param record: the AdditionalRelatedInfoRecord to transform into a dictionary
        :return: a dictionary created from the AdditionalRelatedInfoRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['note'] = record.note
        encoded['society_n'] = record.society_n
        encoded['subject_code'] = record.subject_code
        encoded['type_of_right'] = record.type_of_right
        encoded['work_n'] = record.work_n

        return encoded

    def __encode_agreement_record(self, record):
        """
        Creates a dictionary from an AgreementRecord.

        :param record: the AgreementRecord to transform into a dictionary
        :return: a dictionary created from the AgreementRecord
        """
        encoded = self.__encode_transaction_record_head(record)

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

    def __encode_agreement_territory_record(self, record):
        """
        Creates a dictionary from an AgreementTerritoryRecord.

        :param record: the AgreementTerritoryRecord to transform into a dictionary
        :return: a dictionary created from the AgreementTerritoryRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['inclusion_exclusion_indicator'] = record.inclusion_exclusion_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code

        return encoded

    def __encode_group_header(self, record):
        """
        Creates a dictionary from an GroupHeader.

        :param record: the GroupHeader to transform into a dictionary
        :return: a dictionary created from the GroupHeader
        """
        encoded = {}

        encoded['batch_request_id'] = record.batch_request_id
        encoded['group_id'] = record.group_id
        encoded['record_type'] = record.record_type
        encoded['transaction_type'] = record.transaction_type
        encoded['version_number'] = record.version_number

        return encoded

    def __encode_group_trailer(self, record):
        """
        Creates a dictionary from an GroupTrailer.

        :param record: the GroupTrailer to transform into a dictionary
        :return: a dictionary created from the GroupTrailer
        """
        encoded = {}

        encoded['group_id'] = record.group_id
        encoded['record_count'] = record.record_count
        encoded['record_type'] = record.record_type
        encoded['transaction_count'] = record.transaction_count

        return encoded

    def __encode_interested_party_agreement_record(self, record):
        """
        Creates a dictionary from an AgreementInterestedParty.

        :param record: the AgreementInterestedParty to transform into a dictionary
        :return: a dictionary created from the AgreementInterestedParty
        """
        encoded = self.__encode_transaction_record_head(record)

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

    def __encode_interested_party_territory_control_record(self, record):
        """
        Creates a dictionary from an IPTerritoryOfControlRecord.

        :param record: the IPTerritoryOfControlRecord to transform into a dictionary
        :return: a dictionary created from the IPTerritoryOfControlRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['ip_n'] = record.ip_n
        encoded['ie_indicator'] = record.ie_indicator
        encoded['tis_numeric_code'] = record.tis_numeric_code
        encoded['sequence_n'] = record.sequence_n
        encoded['pr_col_share'] = record.pr_col_share
        encoded['mr_col_share'] = record.mr_col_share
        encoded['sr_col_share'] = record.sr_col_share
        encoded['shares_change'] = record.shares_change

        return encoded

    def __encode_message_record(self, record):
        """
        Creates a dictionary from a MessageRecord.

        :param record: the MessageRecord to transform into a dictionary
        :return: a dictionary created from the MessageRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['message_level'] = record.message_level
        encoded['message_record_type'] = record.message_record_type
        encoded['message_text'] = record.message_text
        encoded['message_type'] = record.message_type
        encoded['original_record_sequence_n'] = record.original_record_sequence_n
        encoded['validation_n'] = record.validation_n

        return encoded

    def __encode_nat_record(self, record):
        """
        Creates a dictionary from a NATRecord.

        :param record: the NATRecord to transform into a dictionary
        :return: a dictionary created from the NATRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['title'] = record.title
        encoded['title_type'] = record.title_type

        return encoded

    def __encode_now_record(self, record):
        """
        Creates a dictionary from a NOWRecord.

        :param record: the NOWRecord to transform into a dictionary
        :return: a dictionary created from the NOWRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['position'] = record.position
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_name'] = record.writer_name

        return encoded

    def __encode_npa_record(self, record):
        """
        Creates a dictionary from a NPARecord.

        :param record: the NPARecord to transform into a dictionary
        :return: a dictionary created from the NPARecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['ip_name'] = record.ip_name
        encoded['ip_writer_name'] = record.ip_writer_name
        encoded['ip_n'] = record.ip_n

        return encoded

    def __encode_npn_record(self, record):
        """
        Creates a dictionary from a NPNRecord.

        :param record: the NPNRecord to transform into a dictionary
        :return: a dictionary created from the NPNRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['ip_n'] = record.ip_n
        encoded['publisher_name'] = record.publisher_name
        encoded['publisher_sequence_n'] = record.publisher_sequence_n

        return encoded

    def __encode_npr_record(self, record):
        """
        Creates a dictionary from a NPRRecord.

        :param record: the NPRRecord to transform into a dictionary
        :return: a dictionary created from the NPRRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['performance_dialect'] = record.performance_dialect
        encoded['performance_language'] = record.performance_language
        encoded['performing_artist_first_name'] = record.performing_artist_first_name
        encoded['performing_artist_ipi_base_n'] = record.performing_artist_ipi_base_n
        encoded['performing_artist_ipi_name_n'] = record.performing_artist_ipi_name_n
        encoded['performing_artist_name'] = record.performing_artist_name

        return encoded

    def __encode_nra_work_record(self, record):
        """
        Creates a dictionary from a NRAWorkRecord.

        :param record: the NRAWorkRecord to transform into a dictionary
        :return: a dictionary created from the NRAWorkRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['title'] = record.title

        return encoded

    def __encode_publisher(self, record):
        """
        Creates a dictionary from a Publisher.

        :param record: the Publisher to transform into a dictionary
        :return: a dictionary created from the Publisher
        """
        encoded = self.__encode_interested_party(record)

        encoded['publisher_name'] = record.publisher_name

        return encoded

    def __encode_nwn_record(self, record):
        """
        Creates a dictionary from a NWNRecord.

        :param record: the NWNRecord to transform into a dictionary
        :return: a dictionary created from the NWNRecord
        """
        encoded = self.__encode_nra_record(record)

        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name
        encoded['ip_n'] = record.ip_n

        return encoded

    def __encode_publisher_for_writer_record(self, record):
        """
        Creates a dictionary from a PublisherForWriterRecord.

        :param record: the PublisherForWriterRecord to transform into a dictionary
        :return: a dictionary created from the PublisherForWriterRecord
        """
        encoded = self.__encode_transaction_record_head(record)

        encoded['publisher_ip_n'] = record.publisher_ip_n
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['submitter_agreement_n'] = record.submitter_agreement_n
        encoded['writer_ip_n'] = record.writer_ip_n

        return encoded

    def __encode_publisher_record(self, record):
        """
        Creates a dictionary from a PublisherRecord.

        :param record: the PublisherRecord to transform into a dictionary
        :return: a dictionary created from the PublisherRecord
        """
        encoded = self.__encode_interested_party_record(record)

        encoded['agreement_type'] = record.agreement_type
        encoded['isac'] = record.isac
        encoded['pr_society'] = record.pr_society
        encoded['pr_ownership_share'] = record.pr_ownership_share
        encoded['publisher_sequence_n'] = record.publisher_sequence_n
        encoded['publisher_type'] = record.publisher_type
        encoded['publisher_unknown'] = record.publisher_unknown
        encoded['society_assigned_agreement_n'] = record.society_assigned_agreement_n
        encoded['special_agreements'] = record.special_agreements
        encoded['submitter_agreement_n'] = record.submitter_agreement_n

        encoded['publisher'] = self.__encode_publisher(record.publisher)

        return encoded

    def __encode_writer(self, record):
        """
        Creates a dictionary from a Writer.

        :param record: the Writer to transform into a dictionary
        :return: a dictionary created from the Writer
        """
        encoded = self.__encode_interested_party(record)

        encoded['personal_number'] = record.personal_number
        encoded['writer_first_name'] = record.writer_first_name
        encoded['writer_last_name'] = record.writer_last_name

        return encoded

    def __encode_writer_record(self, record):
        """
        Creates a dictionary from a WriterRecord.

        :param record: the WriterRecord to transform into a dictionary
        :return: a dictionary created from the WriterRecord
        """
        encoded = self.__encode_interested_party_record(record)

        encoded['reversionary'] = record.reversionary
        encoded['writer_designation'] = record.writer_designation
        encoded['writer_unknown'] = record.writer_unknown
        encoded['work_for_hire'] = record.work_for_hire

        encoded['writer'] = self.__encode_writer(record.writer)

        return encoded