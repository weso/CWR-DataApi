# -*- coding: utf-8 -*-

"""
CWR file structure and information model.

These classes represent a CWR file. This consists on two parts: the metadata on the filename and data inside the file.

The file data is stored into groups, which then are stored into a single transmission. Both of these structures contain
a header and a trailer record, which serve not only to mark the beginning and end of them, but also, in the case of the
trailer records, to validate the previous rows.

Being these four header and trailer records, called control records, are Transmission Header (HDR), Transmission Trailer
(TRL), Group Header (GRH) and Group Trailer (GRT).

These are grouped into a single transmission composed by several groups: [HDR, [GRH,GRT]*, TRL].

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


class TransactionGroup(object):
    """
    Represents a CWR file group of transactions inside a transmission.

    All transactions of the same type should be contained in the same group (i.e. all NWR transactions should
    appear in one single NWR group), and each group type can only be used once per file (i.e there can only be one NWR
    and one REV group per file).

    The type of the group is indicated by the header.
    """

    def __init__(self, group_header, group_trailer, transactions):
        """
        Constructs a TransactionGroup.

        This stores all the transaction of a kind in the file, containing only transactions of that kind.

        A file can not contain two groups with the same type of transaction.

        The group header should be a GroupHeader, and the trailer a GroupTrailer.

        The transactions is a collection of entities representing the transactions.

        :param group_header: the group header
        :param group_trailer: the group trailer
        :param transactions: the group transactions
        """
        self._group_header = group_header
        self._group_trailer = group_trailer
        self._transactions = transactions

    def __str__(self):
        return '%s to %s [%s]' % (
            self._group_header, self._group_trailer, self._transactions)

    def __repr__(self):
        return '<class %s>(grh=%r, grt=%r, transactions=%r)' % (
            'TransactionGroup', self._group_header,
            self._group_trailer,
            self._transactions)

    @property
    def group_header(self):
        """
        The group's header. This is a GroupHeader.

        :return: group's header
        """
        return self._group_header

    @property
    def group_trailer(self):
        """
        The group's trailer. This is a GroupTrailer.

        :return: group's trailer
        """
        return self._group_trailer

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

    def __init__(self, header, trailer, groups):
        """
        Constructs a Transmission.

        The transaction groups should be a collection of TransactionGroup instances. While the header should be a
        TransmissionHeader and the trailer a TransmissionTrailer.

        :param header: the transmission header
        :param trailer: the transmission trailer
        :param groups: the transaction groups
        """
        self._header = header
        self._trailer = trailer
        self._groups = groups

    def __str__(self):
        return '%s to %s [%s]' % (
            self._header, self._trailer, self._groups)

    def __repr__(self):
        return '<class %s>(hdr=%r, trl=%r, groups=%r)' % (
            'Transmission', self._header,
            self._trailer,
            self._groups)

    @property
    def groups(self):
        """
        The transmission groups. This is a collection of TransactionGroups.

        :return: a collection with transaction groups
        """
        return self._groups

    @property
    def header(self):
        """
        The transmission header. This is a TransmissionHeader.

        :return: the transmission header
        """
        return self._header

    @property
    def trailer(self):
        """
        The transmission trailer. This is a TransmissionTrailer.

        :return: the transmission trailer
        """
        return self._trailer