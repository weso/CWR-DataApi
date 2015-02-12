# -*- encoding: utf-8 -*-

from commonworks.file import Record


"""
Acknowledgement entity model classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class AcknowledgementRecord(Record):
    """
    Represents a CWR Acknowledgement of Transaction (ACK).
    """

    def __init__(self, prefix, group_id, transaction_n, transaction_type, transaction_status, date_creation,
                 date_processing, title='', submitter_id='', recipient_id=''):
        super(AcknowledgementRecord, self).__init__(prefix)
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
        Creation Date and Time field. Date and Time.

        The date and time in which the file containing the transaction was created.

        :return: the date and time in which the file was created
        """
        return self._date_creation

    @property
    def date_processing(self):
        """
        Processing Date field. Date.

        The date this transaction or file was formally processed by the recipient.

        :return: the date in which the transaction or file was processed
        """
        return self._date_processing

    @property
    def group_id(self):
        """
        Original Group ID field. Numeric.

        The Group ID within which the original transaction to which  this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set this field to zeroes.

        :return: the original transaction group id
        """
        return self._group_id

    @property
    def recipient_id(self):
        """
        Recipient Creation Number field. Alphanumeric.

        ID given by the recipient to this work.

        This attribute is required if the ACK is in response to a transaction and if the transaction status indicates
        that the recipient has accepted the work.

        :return: the recipient ID for this work
        """
        return self._recipient_id

    @property
    def submitter_id(self):
        """
        Submitter Creation Number field. Alphanumeric.

        ID given by the original submitter to this work.

        This attribute is required if the ACK is in response to a transaction.

        :return: the submitter ID for the work
        """
        return self._submitter_id

    @property
    def title(self):
        """
        Creation Title field. Alphanumeric.

        The creation title as delivered by the submitter (i.e. the title of the musical work or audio visual
        production).

        This field is required if the ACK is in response to an NWR or REV transaction.

        :return: the creation title
        """
        return self._title

    @property
    def transaction_n(self):
        """
        Original Transaction Sequence Number field. Numeric.

        The Transaction Sequence number of the original transaction to which this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem this attribute is zero.

        :return: the original transaction sequence number
        """
        return self._transaction_n

    @property
    def transaction_status(self):
        """
        Transaction Status field. Table Lookup (Transaction Status Table).

        The current status of this transaction.

        :return: the transaction status
        """
        return self._transaction_status

    @property
    def transaction_type(self):
        """
        Original Transaction Type. Table Lookup (Transaction Type table).

        The Transaction Type of the original transaction to which this ACK applies.

        Note that if the ACK is a result of a HDR or TRL record problem, set this field to HDR or TRL (whichever is
        applicable).

        :return: the original transaction type
        """
        return self._transaction_type


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
    information such as CAE/IPI name numbers where possible. In particular, the use of controlled/non-controlled
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
