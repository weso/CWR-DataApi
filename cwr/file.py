# -*- encoding: utf-8 -*-
from abc import ABCMeta

"""
CWR file structure and information model.

Classes inside this module represent the control records of a CWR file, which are used to partition and control the
structure of these files.

These records ensure the integrity of the file after being transmitted over telecommunication lines, and also confirm
that the data has not suffered any other kind of tampering, may it be intentional or not.

Four of them are used on CWR v2.1: Transmission Header (HDR), Transmission Trailer (TRL), Group Header (GRH) and Group
Trailer (GRT). Each represented by the TransmissionHeader, TransmissionTrailer, GroupHeader and GroupTrailer classes.

With these divisions a file can be considered a single transmission composed by several groups: [HDR, [GRH,GRT]*, TRL].

It is important to know that while there can be multiple groups each should contain a single type of transaction,
and all transactions of the same type should be on the same group.

So if the file contains NWR transactions all of the should be on a single group, which can not contain any other type
of transaction. Just to remark this, no other group on that file should contain NWR transactions.

A fifth class related to the file structure, RecordPrefix, stores the information each row contains at their
beginning, indicating their type and position in the records sequence. As this combination of data is unique for
each prefix, it can be considered to be a Record's identifier.

This is to be used along the abstract class Record, to create any kind of CWR file record.

Additionally to the internal data structure this module allows to represent the file's metadata, stored according to the
standard in the file name, with FileTag, which stores the information used to identify and differentiate CWR files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class CWRFile(object):
    """
    Represents a CWR file and all the data contained in it.

    This can be divided into two groups: the metadata and the transmission data.

    The first is indicated, according to the standard, by the file name. While the second is contained inside the file.

    Both are to be represented with the classes in this module. FileTag for the metadata, and Transmission for the
    file contents.
    """

    def __init__(self, tag, transmission):
        """
        Constructs a CWRFile.

        The tag should be a FileTag, and the transmission a Transmission.

        :param tag: the file metadata
        :param transmission: the file contents
        """
        self._tag = tag
        self._transmission = transmission

    def __str__(self):
        return '%s [%s]' % (
            self._tag, self._transmission)

    def __repr__(self):
        return '<class %s>(tag=%r, transmission=%r)' % (
            'CWRFile', self._tag,
            self._transmission)

    def tag(self):
        """
        The file's metadata tag.

        This is stored as a FileTag.

        :return: the file's metadata
        """
        return self._tag

    def transmission(self):
        """
        The file's transmission.

        This wraps all the file's data, and is stored as a Transmission class.

        :return: the file's transmission
        """
        return self._transmission


class FileTag(object):
    """
    Represents a CWR file metadata, which is tagged on the filename.

    This data identifies a concrete file in the file system and, according to the standard, is indicated in the file
    name, using the pattern CWyynnnnsss_rrr.Vxx,, where each section means the following:
    CW - Header indicating it is a CWR file.
    yy - Year.
    nnnn - Sequence. This was originally 2 numbers, later changed to 4.
    sss - Sender. 2 or 3 digits.
    rrr - Receiver. 2 or 3 digits.
    xx - Version of the CWR standard (version x.x).

    So according to this, the files sent between a sender and a receiver each year are numerated following a sequence.
    Then a termination is added indicating the version of the CWR standard specification used on the file.
    """

    def __init__(self, year, sequence_n, sender, receiver, version):
        """
        Constructs a FileTag.

        :param year: year the file was created
        :param sequence_n: sequence number for the file
        :param sender: sender ID
        :param receiver: received ID
        :param version: CWR version of the file
        """
        self._year = year
        self._sequence_n = sequence_n
        self._sender = sender
        self._receiver = receiver
        self._version = version

    def __str__(self):
        return 'file number %s, year %s, sent from %s to %s (CWR v%s)' % (
            self._sequence_n, self._year, self._sender, self._receiver,
            self._version)

    def __repr__(self):
        return '<class %s>(year=%s, sequence_n=%r, sender=%r, receiver=%r, version=%r)' % ('FileTag', self._year,
                                                                                           self._sequence_n,
                                                                                           self._sender, self._receiver,
                                                                                           self._version)

    @property
    def year(self):
        """
        The year in which the file has been created. This is a numeric value.

        :return: the file's year
        """
        return self._year

    @property
    def sequence_n(self):
        """
        File sequence number. This is a numeric value.

        This value indicates the position of this file among all those sent from the sender to the receiver.

        So if the sequence number is 10 this would be the tenth file sent.

        :return: the file sequence number
        """
        return self._sequence_n

    @property
    def sender(self):
        """
        The file sender ID. This is an alphanumeric code.

        :return: the file sender ID
        """
        return self._sender

    @property
    def receiver(self):
        """
        The file receiver ID. This is an alphanumeric code.

        :return: the file receiver ID
        """
        return self._receiver

    @property
    def version(self):
        """
        The CWR standard specification used to code the file. This is a comma separated numeric value.

        :return: the CWR standard specification version used
        """
        return self._version


class GroupHeader(object):
    """
    Represents a CWR file Group Header (GRH).

    The GRH record is used to indicate the presence of a group (or batch) of transactions within the file.

    A group can only contain one type of transaction and this is indicated in the Transaction Type field.
    """

    def __init__(self, group_id, transaction_type, version_number="02.10", batch_request_id=0):
        self._group_id = group_id
        self._transaction_type = transaction_type
        self._version_number = version_number
        self._batch_request_id = batch_request_id

    def __str__(self):
        return '%s(%s)' % (
            self._transaction_type,
            self._group_id)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_type=%r, version_number=%r, batch_request_id=%r)' % (
            'GroupHeader', self._group_id,
            self._transaction_type,
            self._version_number,
            self._batch_request_id)

    @property
    def batch_request_id(self):
        """
        Batch request ID field. Numeric.

        A unique sequential number to identify the group. This number is managed by the submitter to identify the group
        among multiple submission files.

        :return: the submitter's batch request id
        """
        return self._batch_request_id

    @property
    def group_id(self):
        """
        Group ID field. Numeric.

        A unique sequential number for this group within this file.

        :return: the group id
        """
        return self._group_id

    @property
    def transaction_type(self):
        """
        Transaction Type field. Table lookup (Transaction Type table).

        Indicates the type of transactions included in this group. No other type of transaction may be included.

        Values for this field reside in the Transaction Type table.

        :return: the transaction type
        """
        return self._transaction_type

    @property
    def version_number(self):
        """
        Version Number for this transaction type field. Alphanumeric.

        Indicates the version of the transaction type on this group.

        By default this is '02.10', meaning CWR v2.1.

        :return: transaction version number
        """
        return self._version_number


class GroupTrailer(object):
    """
    Represents a CWR file Group Trailer (GRT).

    The Group Trailer Record indicates the end of a group and provides both transaction and record counts for the group.
    """

    def __init__(self, group_id, transaction_count, record_count):
        """
        Constructs a GroupTrailer.

        :param group_id: group ID
        :param transaction_count: number of transactions in the group
        :param record_count: number of records in the group
        """
        self._group_id = group_id
        self._transaction_count = transaction_count
        self._record_count = record_count

    def __str__(self):
        return '%s(g:%s, t:%s)' % (
            self._group_id,
            self._group_id,
            self._transaction_count)

    def __repr__(self):
        return '<class %s>(group_id=%r, transaction_count=%r, record_count=%r)' % (
            'GroupTrailer', self._group_id,
            self._transaction_count,
            self._record_count)

    @property
    def group_id(self):
        """
        Group ID field. Numeric.

        A unique sequential number for this group within this file.

        It is the same group id that was present on the preceding GRH record.

        :return: the group id
        """
        return self._group_id

    @property
    def record_count(self):
        """
        Record Count field. Numeric.

        The number of physical records included within this group including GRH and GRT records.

        :return: the record count
        """
        return self._record_count

    @property
    def transaction_count(self):
        """
        Transaction Count field. Numeric.

        The number of transactions included within this group.

        :return: the number of transactions
        """
        return self._transaction_count


class Record(object):
    """
    Represents a CWR Record.

    This is meant to be used with those records containing a prefix, which are transaction and detail records.

    The prefix serves both to identify them and to validate their position on the file.
    """
    __metaclass__ = ABCMeta

    def __init__(self, prefix):
        """
        Constructs a record with the specified prefix.

        :param prefix: the record prefix
        """
        self._prefix = prefix

    def __str__(self):
        return '%s' % (
            self._prefix)

    def __repr__(self):
        return '<class %s>(prefix=%r)' % (
            'Record', self._prefix)

    @property
    def prefix(self):
        """
        The record's prefix.

        This is a RecordPrefix, and serves both to uniquely identify the Record and to validate it's position in the
        file.

        :return: this record's prefix
        """
        return self._prefix


class RecordPrefix(object):
    """
    Represents a CWR file Record Prefix.

    Albeit it's name, this prefix appears in both detail record and Transaction headers, being always the
    first values on their lines.

    With this prefix it is possible to identify each record or transaction, and also to verify it's correct
    position on the file.

    This is so because it is composed of three values: the record type, the transaction sequence number and
    the record sequence number.

    So, for example, a Transaction header's prefix could be: INS - 12 - 0. Meaning it is an Instrumentation transaction
    and that it should be the 13th (the numeration begins with 0) transaction on the file. As transactions are not
    records, the second number should be always zero.

    In the case of a detail record, it could be: IND - 12 - 3. Meaning it is an Instrumentation Detail record, owned
    by the 13th transaction (which is the one of the previous paragraph), and that it is the 4th (again, starting with
    0) detail on the file.

    It should be noted that as the record type is represented by the object class it is not stored.
    """

    def __init__(self, record_type, transaction_sequence_n, record_sequence_n):
        """
        Constructs a RecordPrefix.

        Note that the sequence numbering differs if this is the header for a Transaction or a detail record.

        In the first case, the record sequence is always zero. In the second, the Transaction sequence
        is equal to its parent Transaction sequence number.

        In both cases the sequence number should be equal or great than zero.

        :param record_type: type code
        :param transaction_sequence_n: position in the transactions sequence
        :param record_sequence_n: position in the records sequence
        """
        self._record_type = record_type
        self._transaction_sequence_n = transaction_sequence_n
        self._record_sequence_n = record_sequence_n

    def __str__(self):
        return '%s (%s-%s)' % (
            self._record_type, self._transaction_sequence_n, self._record_sequence_n)

    def __repr__(self):
        return '<class %s>(record_type=%r, transaction_sequence_n=%r, record_sequence_n=%r)' % (
            'RecordPrefix', self._record_type,
            self._transaction_sequence_n,
            self._record_sequence_n)

    @property
    def record_sequence_n(self):
        """
        Record Sequence number field. Numeric.

        Transactions always have this value set to 0.

        For detail records this value is equal to the record sequence number of the previous detail record stored
        on the file, plus 1.

        :return: the record sequence number
        """
        return self._record_sequence_n

    @property
    def record_type(self):
        """
        Record Type field. Table Lookup (Record Type).

        The transaction type or detail record type.

        :return: the record type
        """
        return self._record_type

    @property
    def transaction_sequence_n(self):
        """
        Transaction Sequence number field. Numeric.

        In each Group the transaction sequence starts with 0, so the first Transaction of each Group should have
        0 as the sequence number.

        The following Transactions should have a sequence number equal to the previous Transaction header's number
        incremented by 1.

        In the case of detail records the transaction sequence should be equal to the transaction sequence of the
        previous Transaction header, the owner of the detail.

        :return: the transaction sequence number
        """
        return self._transaction_sequence_n


class TransactionGroup(object):
    """
    Represents a CWR file group of transactions inside a transmission.

    All transactions of the same type should be contained in the same group (i.e. all NWR transactions should
    appear in one single NWR group), and each group type can only be used once per file (i.e there can only be one NWR
    and one REV group per file).

    The type of the group is indicated by the header.
    """

    def __init__(self, grh, grt, transactions):
        """
        Constructs a TransactionGroup.

        This stores all the transaction of a kind in the file, containing only transactions of that kind.

        A file can not contain two groups with the same type of transaction.

        The group header should be a GroupHeader, and the trailer a GroupTrailer.

        The transactions is a collection of entities representing the transactions.

        :param grh: the group header
        :param grt: the group trailer
        :param transactions: the group transactions
        """
        self._grh = grh
        self._grt = grt
        self._transactions = transactions

    def __str__(self):
        return '%s to %s [%s]' % (
            self._grh, self._grt, self._transactions)

    def __repr__(self):
        return '<class %s>(grh=%r, grt=%r, transactions=%r)' % (
            'TransactionGroup', self._grh,
            self._grt,
            self._transactions)

    @property
    def grh(self):
        """
        The group's header. This is a GroupHeader.

        :return: group's header
        """
        return self._grh

    @property
    def grt(self):
        """
        The group's trailer. This is a GroupTrailer.

        :return: group's trailer
        """
        return self._grt

    @property
    def transactions(self):
        """
        The group transactions.

        This is a collection of entities representing instances of one type of transaction.

        :return: the group transactions
        """
        return self._transactions


class Transmission(object):
    """
    Represents a CWR file Transmission.

    As a Transmission wraps all the file's data, this in practise equals to the file content.

    It is composed by a Transmission Header and a Transmission Trailer, and in-between a collection of groups,
    following the structure [HDR, [GRH,GRT]*, TRL].
    """

    def __init__(self, hdr, trl, groups):
        """
        Constructs a Transmission.

        The transaction groups should be a collection of TransactionGroup instances. While the header should be a
        TransmissionHeader and the trailer a TransmissionTrailer.

        :param hdr: the transmission header
        :param trl: the transmission trailer
        :param groups: the transaction groups
        """
        self._hdr = hdr
        self._trl = trl
        self._groups = groups

    def __str__(self):
        return '%s to %s [%s]' % (
            self._hdr, self._trl, self._groups)

    def __repr__(self):
        return '<class %s>(hdr=%r, trl=%r, groups=%r)' % (
            'Transmission', self._hdr,
            self._trl,
            self._groups)

    def groups(self):
        """
        The transmission groups. This is a collection of TransactionGroups.

        :return: a collection with transaction groups
        """
        return self._groups

    def hdr(self):
        """
        The transmission header. This is a TransmissionHeader.

        :return: the transmission header
        """
        return self._hdr

    def trl(self):
        """
        The transmission trailer. This is a TransmissionTrailer.

        :return: the transmission trailer
        """
        return self._trl


class TransmissionHeader(object):
    """
    Represents a CWR file Transmission Header (HDR).

    This is a required “cover sheet” for transmissions submitted by a participant, containing the file control
    information as well as the name of the sender.
    """

    def __init__(self, sender_id, sender_name, sender_type, creation_date, transmission_date, record_type='HDR',
                 edi_standard='01.10',
                 character_set=""):
        """
        Constructs a TransmissionHeader.

        :param sender_id: the CWR Sender ID or the Society Code
        :param sender_name: name of the sender
        :param sender_type: code identifying the type of sender
        :param creation_date: creation date and time for the file
        :param transmission_date: date in which the file was transmitted
        :param record_type: the CWR record type
        :param edi_standard: EDI standard version (01.10 by default)
        :param character_set: file encoding set (ASCII by default)
        """
        # Record info
        self._record_type = record_type

        # Sender info
        self._sender_id = sender_id
        self._sender_name = sender_name
        self._sender_type = sender_type

        # Dates
        self._creation_date = creation_date
        self._transmission_date = transmission_date

        # Other info
        self._edi_standard = edi_standard
        self._character_set = character_set

    def __str__(self):
        return '%s (%s, %s) on %s' % (
            self._sender_name, self._sender_id, self._sender_type, self._transmission_date)

    def __repr__(self):
        return '<class %s>(sender_id=%r, sender_name=%r, sender_type=%r, creation_date=%r, transmission_date=%r)' % (
            'TransmissionHeader', self._sender_id,
            self._sender_name, self._sender_type, self._creation_date, self._transmission_date)

    @property
    def character_set(self):
        """
        Character Set field. Table lookup (not yet existing).

        By default this is ASCII, and files using any other set are only intended to be sent to societies that accept
        and use such character sets (e.g, CASH).

        The table containing the accepted values does not exist at the time of this implementation.

        :return: the character set used on the file
        """
        return self._character_set

    @property
    def creation_date(self):
        """
        Creation Date field. Date.

        The date that this file was created.

        :return: the creation date
        """
        return self._creation_date.date()

    @property
    def creation_time(self):
        """
        Creation Time fields. Time.

        The time at which this file was created.

        :return: the creation time
        """
        return self._creation_date.time()

    @property
    def edi_standard(self):
        """
        EDI Standard Version Number field. Alphanumeric.

        Indicates which version of the header and trailer records was used to create the data in this file.

        By default this is '01.10', which is required by the CWR v2.1 standard.

        :return: the EDI standard version number
        """
        return self._edi_standard

    @property
    def record_type(self):
        """
        Record Type field

        This is expected to be 'HDR'.

        :return: the record Type
        """
        return self._record_type

    @property
    def sender_id(self):
        """
        Sender ID field. Numeric.

        If Sender Type is equal to 'PB' (Publisher), 'AA' (Administrative Agency), or 'WR' (Writer), the sender  must
        enter their assigned CWR CAE number in this field.

        If Sender Type is equal to 'SO' (Society), the sending society must enter their Society Code.

        The Society codes reside in the Society Code Table. The others on the CWR Sender ID and Codes Table.

        :return: the sender ID
        """
        return self._sender_id

    @property
    def sender_name(self):
        """
        Sender Name field. Alphanumeric.

        The name of the sender.

        :return: name of the sender
        """
        return self._sender_name

    @property
    def sender_type(self):
        """
        Sender Type field. Alphanumeric.

        Indicates if the sender of the file is a society or a publisher.

        Possible values are:
        - 'AA': Administrative Agency
        - 'PB': Publisher
        - 'SO': Society
        - 'WR': Writer

        :return: the sender type
        """
        return self._sender_type

    @property
    def transmission_date(self):
        """
        Transmission Date field. Date.

        The date that this file was transmitted to all receiving entities.

        :return: the transmission date
        """
        return self._transmission_date


class TransmissionTrailer(object):
    """
    Represents a CWR file Transmission Trailer (TRL).

    The Transmission Trailer record indicates the end of the transmission file.

    Control totals representing the number of groups, transactions, and records within the file are included on this
    record.
    """

    def __init__(self, group_count, transaction_count, record_count):
        """
        Constructs a TransmissionTrailer.

        :param group_count: the total number of groups on the file
        :param transaction_count: the total number of transactions on the file
        :param record_count: the total number of records on the file
        """
        self._group_count = group_count
        self._transaction_count = transaction_count
        self._record_count = record_count

    def __str__(self):
        return '%s groups, %s transactions, %s records' % (
            self._group_count, self._transaction_count, self._record_counte)

    def __repr__(self):
        return '<class %s>(group_count=%r, transaction_count=%r, record_count=%r)' % (
            'TransmissionTrailer', self._group_count,
            self._transaction_count, self._record_count)

    @property
    def group_count(self):
        """
        Group Count field. Numeric.

        The number of groups included within this file.

        :return: the total group count
        """
        return self._group_count

    @property
    def record_count(self):
        """
        Record Count field. Numeric.

        The number of physical records included in this file including HDR and TRL records.

        :return: the total record count
        """
        return self._record_count

    @property
    def transaction_count(self):
        """
        Transaction Count field. Numeric.

        The number of transactions included within this file.

        :return: the total transaction count
        """
        return self._transaction_count