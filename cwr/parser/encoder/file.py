# -*- coding: utf-8 -*-

from cwr.parser.common import Encoder


"""
Parsers for encoding CWR model classes, creating a text string for them which complies with the CWR standard.

While the encoder classes are accessible, they are meant to be used directly only when creating custom versions,
by default the factory methods old_filename_encoder() and default_filename_encoder() should be used to acquire
the encoders to use when creating a file.

The old_filename_encoder() method will return an encoder which creates a filename following the old specification,
where ne numeric sequence consists of two numbers, while the default_filename_encoder() will create a filename
following the new specification, where the sequence consists of four numbers.

Both encoders require a FileTag containing valid values, which will be transformed into the resulting string.

These encoders are created from BaseCWRFileNameEncoder, just setting the correct sequence number length.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def old_filename_encoder():
    """
    Creates an encoder which parses a CWR file name from a FileTag object.

    This encoder will follow the old format, where the sequence number is only two digits longs.

    It should be noted that this format has been made obsolete, and files now should use four digits.

    These old file names follow the pattern CWyynnsss_rrr.Vxx.

    :return: an encoder for filenames using the old convention
    """
    return BaseCWRFileNameEncoder(2)


def default_filename_encoder():
    """
    Creates an encoder which parses a CWR file name from a FileTag object.

    This encoder will follow the CWR naming convention update done by the CWR Management Committee, which increased the
    sequence length from two digits to four.

    After this change file names no longer follow the CISAC CWR standard, but allows for higher number of CWR file
    transmissions.

    These old files names follow the pattern CWyynnnnsss_rrr.Vxx.

    :return: an encoder for filenames using the new convention
    """
    return BaseCWRFileNameEncoder(4)


class BaseCWRFileNameEncoder(Encoder):
    """
    Parses a CWR file name from a FileTag class.

    As the file name is a very precise type of string, this parsing will be lossless, meaning that all the information
    from the file name will be always parsed into the resulting object.

    CWR file names follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
    CW - Header indicating it is a CWR file.
    yy - Year.
    nnnn - Sequence. This was originally 2 numbers, later changed to 4.
    sss - Sender. 2 or 3 digits.
    rrr - Receiver. 2 or 3 digits.
    xx - Version of the CWR standard (version x.x).

    As the Sequence number length was changed, the encoder will require this length to be indicated.
    """

    # Delimiters
    _header = 'CW'
    _ip_delimiter = '_'
    _version_delimiter = '.V'

    def __init__(self, sequence_l):
        super(BaseCWRFileNameEncoder, self).__init__()
        self._sequence_l = sequence_l

    def encode(self, tag):
        """
        Parses a CWR file name from a FileTag object.

        The result will be a string following the format CWyynnnnsss_rrr.Vxx, where the numeric sequence will
        have the length set on the encoder's constructor.

        :param tag: FileTag to parse
        :return: a string file name parsed from the FileTag
        """
        # Acquires sequence number
        sequence = str(tag.sequence_n)

        # If the sequence is bigger the max, it is cut
        if (len(sequence) > self._sequence_l):
            sequence = sequence[:self._sequence_l]

        # If the sequence is smaller the max, it is padded with zeroes
        while len(sequence) < self._sequence_l:
            sequence = '0' + sequence

        # Acquires version
        version = str(tag.version)

        # If the version is too long only the first and last number are taken, to remove decimal separator
        if len(version) > 2:
            version = version[:1] + version[-1:]

        # If the version is too short, it is padded with zeroes
        while len(version) < 2:
            version = '0' + version

        # Acquires year
        # Only the two last digits of the year are used
        year = str(tag.year)[-2:]

        # Acquires sender and receiver
        sender = tag.sender[:3]
        receiver = tag.receiver[:3]

        return self._header + year + sequence + sender + self._ip_delimiter + receiver + ".V" + version
