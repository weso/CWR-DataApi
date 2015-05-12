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

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n,
                 original_group_id, original_transaction_sequence_n, original_transaction_type,
                 transaction_status, creation_date_time, processing_date,
                 creation_title='', submitter_creation_n='', recipient_creation_n=''):
        super(AcknowledgementRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
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

        The date and time in which the file containing the transaction was created.

        Note that these are two different fields on the CWR field, but are combined for easing its use.

        :return: the date and time in which the file was created
        """
        return self._creation_date_time

    @property
    def creation_title(self):
        """
        Creation Title field. Alphanumeric.

        The creation title as delivered by the submitter (i.e. the title of the musical work or audio visual
        production).

        This field is required if the ACK is in response to an NWR or REV transaction.

        :return: the creation title
        """
        return self._creation_title

    @property
    def original_group_id(self):
        """
        Original Group ID field. Numeric.

        The Group ID within which the original transaction to which  this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set this field to zeroes.

        :return: the original transaction group id
        """
        return self._original_group_id

    @property
    def original_transaction_sequence_n(self):
        """
        Original Transaction Sequence Number field. Numeric.

        The Transaction Sequence number of the original transaction to which this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem this attribute is zero.

        :return: the original transaction sequence number
        """
        return self._original_transaction_sequence_n

    @property
    def original_transaction_type(self):
        """
        Original Transaction Type. Table Lookup (Transaction Type table).

        The Transaction Type of the original transaction to which this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set this field to HDR or TRL (whichever is
        applicable).

        :return: the original transaction type
        """
        return self._original_transaction_type

    @property
    def processing_date(self):
        """
        Processing Date field. Date.

        The date this transaction or file was formally processed by the recipient.

        :return: the date in which the transaction or file was processed
        """
        return self._processing_date

    @property
    def recipient_creation_n(self):
        """
        Recipient Creation Number field. Alphanumeric.

        ID given by the recipient to this work.

        This attribute is required if the ACK is in response to a transaction and if the transaction status indicates
        that the recipient has accepted the work.

        :return: the recipient ID for this work
        """
        return self._recipient_creation_n

    @property
    def submitter_creation_n(self):
        """
        Submitter Creation Number field. Alphanumeric.

        ID given by the original submitter to this work.

        This attribute is required if the ACK is in response to a transaction.

        :return: the submitter ID for the work
        """
        return self._submitter_creation_n

    @property
    def transaction_status(self):
        """
        Transaction Status field. Table Lookup (Transaction Status Table).

        The current status of this transaction.

        :return: the transaction status
        """
        return self._transaction_status


class AcknowledgementTransaction(object):
    """
    Represents a CWR Acknowledgment Transaction (ACK).

    This transaction is used by the recipient to indicate for each received transaction if it was accepted or not,
    adding any error or warning message that may have resulted from checking the file.

    The acknowledged transactions will be included inside this one.

    But not all transactions will be acknowledged, only AGR, NWR, REV or EXC transactions need acknowledgment, and
    these will be returned with a few changes, as the ACK transaction will contain all the records sent by
    the submitter that have relevance to the recipient.

    For example, a society will generally not return SPU/SPT records for sub-publishers in territories it does not
    control.

    The exception are NWR and REV transactions will be as the submitter sent, but supplemented with additional
    information such as IPI name numbers where possible. In particular, the use of controlled/non-controlled
    record types will be as for the submitter.  For example, if a submitter sent a publisher on an SPU, the ACK will
    contain an SPU for that publisher.

    All the messages caused by processing the records will be included in the ACK transaction along the acknowledged
    transaction.

    The transaction follows the form:
    [ACK, MSG*, AGR|NWR|REV|EXC]
    """

    def __init__(self, ack, agr=None, nwr=None, rev=None, exc=None, messages=None):
        self._ack = ack
        self._agr = agr
        self._nwr = nwr
        self._rev = rev
        self._exc = exc

        if messages is None:
            self._messages = []
        else:
            self._messages = messages

    def __str__(self):
        return '%s [agr=%r, nwr=%r, rev=%r, exc=%r, messages=%r]' % (
            'Acnowledgement Transaction', self._agr,
            self._nwr, self._rev, self._exc, self._messages)

    def __repr__(self):
        return '<class %s>(agr=%r, nwr=%r, rev=%r, exc=%r, messages=%r)' % (
            self.__class__.__name__, self._agr,
            self._nwr, self._rev, self._exc, self._messages)

    @property
    def ack(self):
        """
        The Acknowledgment record.

        This is the record with the transaction's general information.

        :return: the acknowledgment record
        """
        return self._ack

    @property
    def agr(self):
        """
        Agreement supporting Work Registration field.

        :return: the agreement transaction affected by this acknowledgement
        """
        return self._agr

    @property
    def exc(self):
        """
        Existing Work in Conflict field.

        :return: the existing work in conflict transaction affected by this acknowledgement
        """
        return self._exc

    @property
    def messages(self):
        """
        Message field.

        List all messages generated as a result of editing this transaction.

        :return: a list with all the messages
        """
        return self._messages

    @property
    def nwr(self):
        """
        New Works Registration field.

        :return: the new works transaction affected by this acknowledgement
        """
        return self._nwr

    @property
    def rev(self):
        """
        Revised Registration field.

        :return: the revised registration transaction affected by this acknowledgement
        """
        return self._rev


class MessageRecord(TransactionRecord):
    """
    Represents a CWR Message (MSG).

    These records are used to communicate the results of validation on individual transactions back to the
    transaction’s originator.

    A table of messages used for CWR can be found in the CWR website.  The table contains all of the messages in
    this format.

    The message text in the table have been reworded to make them more easily understood, but the content is the same
    as in this manual.

    The combination of Record Type, Message Level and Validation Number can be used to reference the error in this
    document.

    For example, NWR T 003 refers to the 3rd Transaction level validation for the NWR/REV transaction
    (Instrumentation required for serious works).

    Message Type provides you with the severity of the error.

    For example, if Message Type is equal to T, then the entire work registration has been rejected.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n,
                 message_level, validation_n, message_type, message_text,
                 original_record_sequence_n, message_record_type):
        super(MessageRecord, self).__init__(record_type, transaction_sequence_n, record_sequence_n)
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

        The level of editing that was responsible for generation of this message.

        The possible values are:
        - E: Entire File
        - F: Field
        - G: Group
        - R: Record
        - T: Transaction

        :return: the message level
        """
        return self._message_level

    @property
    def message_record_type(self):
        """
        Message's Record Type field. Alphanumeric.

        The record type within the original transaction that caused generation of this message.

        :return: the record type
        """
        return self._message_record_type

    @property
    def message_type(self):
        """
        Message Type field. Table Lookup ('E'/'F'/'G'/'R'/'T').

        Indicates whether this information is a warning, error, or for information only.

        The possible values are:
        - E: Entire File Rejected
        - F: Field Rejected
        - G: Group Rejected
        - R: Record Rejected
        - T: Transaction Rejected

        :return: the message type
        """
        return self._message_type

    @property
    def original_record_sequence_n(self):
        """
        Original Record Sequence # field. Numeric.

        The Record Sequence Number within the transaction associated with this acknowledgment that caused the generation
        of this message.

        :return: the original record sequence number
        """
        return self._original_record_sequence_n

    @property
    def message_text(self):
        """
        Message Text field. Alphanumeric.

        The text associated with this message.

        :return: the message text
        """
        return self._message_text

    @property
    def validation_n(self):
        """
        Validation Number field. Alphanumeric.

        Identifies the specific edit condition that generated this message.  Note that the combination of Record Type,
        Message Level, and Validation Number points back to a condition within this document.

        :return: the validation number field
        """
        return self._validation_n
