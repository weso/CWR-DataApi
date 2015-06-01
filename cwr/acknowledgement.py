# -*- coding: utf-8 -*-

from cwr.record import TransactionRecord

"""
Acknowledgement entity model classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class AcknowledgementRecord(TransactionRecord):
    """
    Represents a CWR Acknowledgement of Transaction (ACK).
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 original_group_id=0,
                 original_transaction_sequence_n=0,
                 original_transaction_type='',
                 transaction_status=None,
                 creation_date_time=None,
                 processing_date=None,
                 creation_title='',
                 submitter_creation_n='',
                 recipient_creation_n=''
                 ):
        super(AcknowledgementRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n
        )
        # Record information
        self._original_group_id = original_group_id
        self._original_transaction_sequence_n = original_transaction_sequence_n

        # Transaction information
        self._original_transaction_type = original_transaction_type
        self._transaction_status = transaction_status

        # Transmission information
        self._creation_date_time = creation_date_time
        self._processing_date = processing_date
        self._creation_title = creation_title
        self._submitter_creation_n = submitter_creation_n
        self._recipient_creation_n = recipient_creation_n

    @property
    def creation_date_time(self):
        """
        Creation Date and Time field. Date and Time combined.

        The date and time in which the file containing the transaction was
        created.

        Note that these are two different fields on the CWR field, but are
        combined for easing its use.

        :return: the date and time in which the file was created
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, value):
        self._creation_date_time = value

    @property
    def creation_title(self):
        """
        Creation Title field. Alphanumeric.

        The creation title as delivered by the submitter (i.e. the title of
        the musical work or audio visual
        production).

        This field is required if the ACK is in response to an NWR or REV
        transaction.

        :return: the creation title
        """
        return self._creation_title

    @creation_title.setter
    def creation_title(self, value):
        self._creation_title = value

    @property
    def original_group_id(self):
        """
        Original Group ID field. Numeric.

        The Group ID within which the original transaction to which  this ACK
        applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set
        this field to zeroes.

        :return: the original transaction group id
        """
        return self._original_group_id

    @original_group_id.setter
    def original_group_id(self, value):
        self._original_group_id = value

    @property
    def original_transaction_sequence_n(self):
        """
        Original Transaction Sequence Number field. Numeric.

        The Transaction Sequence number of the original transaction to which
        this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem this
        attribute is zero.

        :return: the original transaction sequence number
        """
        return self._original_transaction_sequence_n

    @original_transaction_sequence_n.setter
    def original_transaction_sequence_n(self, value):
        self._original_transaction_sequence_n = value

    @property
    def original_transaction_type(self):
        """
        Original Transaction Type. Table Lookup (Transaction Type table).

        The Transaction Type of the original transaction to which this ACK
        applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set
        this field to HDR or TRL (whichever is applicable).

        :return: the original transaction type
        """
        return self._original_transaction_type

    @original_transaction_type.setter
    def original_transaction_type(self, value):
        self._original_transaction_type = value

    @property
    def processing_date(self):
        """
        Processing Date field. Date.

        The date this transaction or file was formally processed by the
        recipient.

        :return: the date in which the transaction or file was processed
        """
        return self._processing_date

    @processing_date.setter
    def processing_date(self, value):
        self._processing_date = value

    @property
    def recipient_creation_n(self):
        """
        Recipient Creation Number field. Alphanumeric.

        ID given by the recipient to this work.

        This attribute is required if the ACK is in response to a transaction
        and if the transaction status indicates that the recipient has
        accepted the work.

        :return: the recipient ID for this work
        """
        return self._recipient_creation_n

    @recipient_creation_n.setter
    def recipient_creation_n(self, value):
        self._recipient_creation_n = value

    @property
    def submitter_creation_n(self):
        """
        Submitter Creation Number field. Alphanumeric.

        ID given by the original submitter to this work.

        This attribute is required if the ACK is in response to a transaction.

        :return: the submitter ID for the work
        """
        return self._submitter_creation_n

    @submitter_creation_n.setter
    def submitter_creation_n(self, value):
        self._submitter_creation_n = value

    @property
    def transaction_status(self):
        """
        Transaction Status field. Table Lookup (Transaction Status Table).

        The current status of this transaction.

        :return: the transaction status
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, value):
        self._transaction_status = value


class MessageRecord(TransactionRecord):
    """
    Represents a CWR Message (MSG).

    These records are used to communicate the results of validation on
    individual transactions back to the transaction’s originator.

    A table of messages used for CWR can be found in the CWR website. The
    table contains all of the messages in this format.

    The message text in the table have been reworded to make them more easily
    understood, but the content is the same as in this manual.

    The combination of Record Type, Message Level and Validation Number can be
    used to reference the error in this document.

    For example, NWR T 003 refers to the 3rd Transaction level validation for
    the NWR/REV transaction (Instrumentation required for serious works).

    Message Type provides you with the severity of the error.

    For example, if Message Type is equal to T, then the entire work
    registration has been rejected.
    """

    def __init__(self,
                 record_type='',
                 transaction_sequence_n=0,
                 record_sequence_n=0,
                 message_level=None,
                 validation_n='',
                 message_type='',
                 message_text='',
                 original_record_sequence_n=0,
                 message_record_type=''
                 ):
        super(MessageRecord, self).__init__(
            record_type,
            transaction_sequence_n,
            record_sequence_n
        )
        # Message info
        self._message_type = message_type
        self._message_text = message_text

        # Message identification
        self._message_level = message_level
        self._validation_n = validation_n

        # Record info
        self._original_record_sequence_n = original_record_sequence_n
        self._message_record_type = message_record_type

    @property
    def message_level(self):
        """
        Message Level field. Table Lookup ('E'/'F'/'G'/'R'/'T').

        The level of editing that was responsible for generation of this
        message.

        The possible values are:
        - E: Entire File
        - F: Field
        - G: Group
        - R: Record
        - T: Transaction

        :return: the message level
        """
        return self._message_level

    @message_level.setter
    def message_level(self, value):
        self._message_level = value

    @property
    def message_record_type(self):
        """
        Message's Record Type field. Alphanumeric.

        The record type within the original transaction that caused generation
        of this message.

        :return: the record type
        """
        return self._message_record_type

    @message_record_type.setter
    def message_record_type(self, value):
        self._message_record_type = value

    @property
    def message_type(self):
        """
        Message Type field. Table Lookup ('E'/'F'/'G'/'R'/'T').

        Indicates whether this information is a warning, error, or for
        information only.

        The possible values are:
        - E: Entire File Rejected
        - F: Field Rejected
        - G: Group Rejected
        - R: Record Rejected
        - T: Transaction Rejected

        :return: the message type
        """
        return self._message_type

    @message_type.setter
    def message_type(self, value):
        self._message_type = value

    @property
    def original_record_sequence_n(self):
        """
        Original Record Sequence # field. Numeric.

        The Record Sequence Number within the transaction associated with this
        acknowledgment that caused the generation of this message.

        :return: the original record sequence number
        """
        return self._original_record_sequence_n

    @original_record_sequence_n.setter
    def original_record_sequence_n(self, value):
        self._original_record_sequence_n = value

    @property
    def message_text(self):
        """
        Message Text field. Alphanumeric.

        The text associated with this message.

        :return: the message text
        """
        return self._message_text

    @message_text.setter
    def message_text(self, value):
        self._message_text = value

    @property
    def validation_n(self):
        """
        Validation Number field. Alphanumeric.

        Identifies the specific edit condition that generated this message.
        Note that the combination of Record Type, Message Level, and
        Validation Number points back to a condition within this document.

        :return: the validation number field
        """
        return self._validation_n

    @validation_n.setter
    def validation_n(self, value):
        self._validation_n = value
