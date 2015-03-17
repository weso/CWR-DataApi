# -*- coding: utf-8 -*-

from cwr.acknowledgement import AcknowledgementRecord, MessageRecord
from cwr.agreement import InterestedPartyForAgreementRecord, AgreementRecord, AgreementTerritoryRecord
from cwr.group import GroupHeader, GroupTrailer
from cwr.info import AdditionalRelatedInfoRecord

from cwr.parser.common import Encoder


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
        elif isinstance(object, MessageRecord):
            # Message
            encoded = self.__encode_message_record(object)
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