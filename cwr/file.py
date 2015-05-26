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
            self.__class__.__name__, self._tag,
            self._transmission)

    @property
    def tag(self):
        """
        The file's metadata tag.

        This is stored as a FileTag.

        :return: the file's metadata
        """
        return self._tag

    @property
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
        return '<class %s>(year=%s, sequence_n=%r, sender=%r, receiver=%r, version=%r)' % (
            self.__class__.__name__, self._year,
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
