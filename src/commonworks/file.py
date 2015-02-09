# -*- encoding: utf-8 -*-

"""
CWR file information model.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class FileTag(object):
    """
    Represents a CWR file tagging data.

    This data identifies a concrete file in the file system and, according to the standard, is indicated in the file
    name, using the pattern CWyynnnnsss_rrr.Vxx,, where each section means the following:
    CW - Header indicating it is a CWR file.
    yy - Year.
    nnnn - Sequence. This was originally 2 numbers, later changed to 4.
    sss - Sender. 2 or 3 digits.
    rrr - Receiver. 2 or 3 digits.
    xx - Version of the CWR standard

    So according to this, the files sent between a sender and a receiver each year are numerated following a sequence.
    Then a termination is added indicating the version of the CWR standard specification used on the file.
    """

    def __init__(self, year, sequence_n, sender, receiver, version):
        self._year = year
        self._sequence_n = sequence_n
        self._sender = sender
        self._receiver = receiver
        self._version = version

    @property
    def year(self):
        """
        The year in which the file has been created.

        :return: the file's year
        """
        return self._year

    @property
    def sequence_n(self):
        """
        File sequence number.

        This is nth file sent from the sender to the receiver. So if the sequence number is 10 this would be the tenth
        file sent.

        :return: the file sequence number
        """
        return self._sequence_n

    @property
    def sender(self):
        """
        The file sender.

        This is stored as an alphanumeric code.

        :return: the file sender alphanumeric code
        """
        return self._sender

    @property
    def receiver(self):
        """
        The file receiver.

        This is stored as an alphanumeric code.

        :return: the file receiver alphanumeric code
        """
        return self._receiver

    @property
    def version(self):
        """
        The CWR standard specification used to code the file.

        :return: the CWR standard specification used
        """
        return self._version


class HDR(object):
    """
    Represents a CWR file Transmission Header (HDR).

    This is a required “cover sheet” for transmissions submitted by a participant.  It will contain the file control
    information as well as the name of the submitter.
    """

    def __init__(self, sender_id, sender_name, sender_type, creation_date, transmission_date):
        # Sender info
        self._sender_id = sender_id
        self._sender_name = sender_name
        self._sender_type = sender_type

        # Dates
        self._creation_date = creation_date
        self._transmission_date = transmission_date

    @property
    def sender_id(self):
        """
        Sender ID field.

        If Sender Type is equal to PB, AA, or WR, the sender  must enter their assigned CWR CAE # in this field.

        These values reside in the CWR Sender ID and Codes Table. If Sender Type is equal to SO, the sending society
        must enter their Society Code.  These values reside in the Society Code Table.

        :return: the sender ID
        """
        return self._sender_id

    @property
    def sender_name(self):
        """
        Sender Name field.

        The name of the sender (publisher, society, agency).

        :return: name of the sender
        """
        return self._sender_name

    @property
    def sender_type(self):
        """
        Sender Type field.

        Indicates if the sender of the file is a society or a publisher.

        Values are PB = Publisher, SO = Society, AA = Administrative Agency, WR = Writer

        :return: the sender type
        """
        return self._sender_type

    @property
    def transmission_date(self):
        """
        Transmission Date field.

        The date that this file was transmitted to all receiving entities.

        :return: the transmission date
        """
        return self._transmission_date


class GRH(object):
    """
    Represents a CWR file Group Header (GRH).

    The GRH record is used to indicate the presence of a group (or batch) of transactions within the file.  A group can
    only contain one type of transaction and this is indicated in the Transaction Type field.
    """

    def __init__(self, group_id, transaction_type):
        self._group_id = group_id
        self._transaction_type = transaction_type

    def group_id(self):
        """
        Group ID field.

        A unique sequential number for this group within this file.

        :return: the group id
        """
        return self._group_id

    def transaction_type(self):
        """
        Transaction Type field.

        Indicates the type of transactions included in this group.  Values for this field reside in the Transaction Type
        table.

        :return: the transaction type
        """
        return self._transaction_type


class GRT(object):
    """
    Represents a CWR file Group Trailer (GRT).

    The Group Trailer Record indicates the end of a group and provides both transaction and record counts for the group.
    """

    def __init__(self, group_id, transaction_count, record_count):
        self._group_id = group_id
        self._transaction_count = transaction_count
        self._record_count = record_count

    def group_id(self):
        """
        Group ID field.

        A unique sequential number for this group within this file.

        It is the same group id that was present on the preceding GRH record.

        :return: the group id
        """
        return self._group_id

    def record_count(self):
        """
        Record Count field.

        The number of physical records included within this group including GRH and GRT records.

        :return: the record count
        """
        return self._record_count

    def transaction_count(self):
        """
        Transaction Count field.

        The number of transactions included within this group.

        :return: the number of transactions
        """
        return self._transaction_count


class TRL(object):
    """
    Represents a CWR file Transmission Trailer (TRL).

    The Transmission Trailer record indicates the end of the transmission file.  Control totals representing the number
    of groups, transactions, and records within the file are included on this record.
    """

    def __init__(self, group_count, transaction_count, record_count):
        self._group_count = group_count
        self._transaction_count = transaction_count
        self._record_count = record_count

    def group_count(self):
        """
        Group Count field.

        The number of groups included within this file.

        :return: the group count
        """
        return self._group_count

    def record_count(self):
        """
        Record Count field.

        The number of physical records included in this file including HDR and TRL records.

        :return: the record count
        """
        return self._record_count

    def transaction_count(self):
        """
        Transaction Count field.

        The number of transactions included within this file.

        :return: the transaction count
        """
        return self._transaction_count