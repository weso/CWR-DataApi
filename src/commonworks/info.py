# -*- encoding: utf-8 -*-

"""
CWR information model.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class Acknowledgement(object):
    """
    Represents a CWR Acknowledgement of Transaction (ACK).
    """

    def __init__(self, group_id, transaction_n, transaction_type, transaction_status, date_creation, date_processing,
                 title=None, submitter_id=None,
                 recipient_id=None):
        self._group_id = group_id
        self._transaction_n = transaction_n
        self._transaction_type = transaction_type
        self._transaction_status = transaction_status
        self._date_creation = date_creation
        self._date_processing = date_processing
        self._title = title
        self._submitter_id = submitter_id
        self._recipient_id = recipient_id

    @property
    def date_creation(self):
        """
        Creation Date field.

        The Creation Date of the original file that contained the transaction to which this ACK applies.

        Includes time.

        :return: the date of creation
        """
        return self._date_creation

    @property
    def date_processing(self):
        """
        Processing Date field.

        The date this transaction or file was formally processed by the recipient.

        :return: the date in which the transaction or file was processed
        """
        return self._date_processing

    @property
    def group_id(self):
        """
        Original Group ID field.

        The Group ID within which the original transaction to which  this ACK applies.  Note that if the ACK is a result
        of a HDR or TRL record problem, set this field to zeroes.

        :return: the original group id
        """
        return self._group_id

    @property
    def recipient_id(self):
        """
        Recipient Creation # field.

        The unique identifier assigned by the recipient to this work. This field is required if the ACK is in response
        to a transaction and if the transaction status indicates that the recipient has accepted the work.

        :return: the recipient id for this work
        """
        return self._recipient_id

    @property
    def submitter_id(self):
        """
        Submitter Creation # field.

        The unique identifier assigned by the original submitter to this work. This field is required if the ACK is in
        response to a transaction.

        :return: the submitter's id for the work
        """
        return self._submitter_id

    @property
    def title(self):
        """
        Creation Title field.

        The creation title as delivered by the submitter (i.e. the title of the musical work or audio visual production,
        …).  This field is required if the ACK is in response to an NWR or REV transaction.

        :return: the creation title
        """
        return self._title

    @property
    def transaction_n(self):
        """
        Original Transaction Sequence # field.

        The Transaction Sequence # of the original transaction to which this ACK applies. Note that if the ACK is a
        result of a HDR or TRL record problem, set this field to zeroes.

        :return: the original transaction sequence number
        """
        return self._transaction_n

    @property
    def transaction_status(self):
        """
        Transaction Status field.

        The current status of this transaction.  Values for this field reside in the Transaction Status Table.

        :return: the transaction status
        """
        return self._transaction_status

    @property
    def transaction_type(self):
        """
        Original Transaction Type.

        The Transaction Type of the original transaction to which this ACK applies. Note that if the ACK is a result of
        a HDR or TRL record problem, set this field to HDR or TRL (whichever is applicable).

        :return: the original transaction type
        """
        return self._transaction_type


class AdditionalRelatedInfo(object):
    """
    Represents a CWR Additional Related Info (ARI).
    """

    def __init__(self, society_id, right_type, work_id=None, subject=None, note=None):
        self._society_id = society_id
        self._right_type = right_type
        self._work_id = work_id
        self._subject = subject
        self._note = note

    @property
    def note(self):
        """
        Note field.

        Free text field pertaining to the type of right and subject specified above.

        :return: the note
        """
        return self._note

    @property
    def right_type(self):
        """
        Type of Right field.

        Indicates that this information relates to performing rights, mechanical rights, sync. rights or all rights
        (ALL)

        :return: the type of right
        """
        return self._right_type

    @property
    def society_id(self):
        """
        Society # field.

        Number assigned to the Society to which the Note is addressed.  These values reside Society Code Table. If the
        note is addressed to all societies that use the ARI record, use '000'.

        :return: the society number id
        """
        return self._society_id

    @property
    def subject(self):
        """
        Subject Code field.

        Subject of the ARI.

        :return: the subject code
        """
        return self._subject

    @property
    def work_id(self):
        """
        Work # field.

        The Society work # that relates to this registration.  It may have been found on an unidentified list, or a
        website, …

        :return: the work id
        """
        return self._work_id


class Message(object):
    """
    Represents a CWR Message (MSG).
    """

    def __init__(self, message_type, text, sequence_n, record_type, message_level, validation_n):
        self._message_type = message_type
        self._sequence_n = sequence_n
        self._record_type = record_type
        self._message_level = message_level
        self._validation_n = validation_n
        self._text = text

    @property
    def message_level(self):
        """
        Message Level field.

        The level of editing that was responsible for generation of this message.  Values are E = Entire File,
        G = Group, T = Transaction, R = Record, F = Field.

        :return: the message level
        """
        return self._message_level

    @property
    def message_type(self):
        """
        Message Type field.

        Indicates whether this information is a warning, error, or for information only.  Values are F = Field Rejected,
        R = Record Rejected, T = Transaction Rejected, G = Group Rejected, E = Entire File Rejected

        :return: the message type
        """
        return self._message_type

    @property
    def record_type(self):
        """
        Record Type field.

        The record type within the original transaction that caused generation of this message.

        :return: the record type
        """
        return self._record_type

    @property
    def sequence_n(self):
        """
        Original Record Sequence # field.

        The Record Sequence Number within the transaction associated with this acknowledgment that caused the generation
        of this message.

        :return: the original record sequence number
        """
        return self._sequence_n

    @property
    def text(self):
        """
        Message Text field.

        The text associated with this message.

        :return: the message text
        """
        return self._text

    @property
    def validation_n(self):
        """
        Validation Number field.

        Identifies the specific edit condition that generated this message.  Note that the combination of Record Type,
        Message Level, and Validation Number points back to a condition within this document.

        :return: the validation number field
        """
        return self._validation_n