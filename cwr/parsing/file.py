# -*- encoding: utf-8 -*-

from cwr.parsing.grammar import filename


"""
CWR file parsing classes.

These classes allow decoding and encoding file related information, such as the file name.

CWR file names follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
CW - Header indicating it is a CWR file.
yy - Year.
nnnn - Sequence. This was originally 2 numbers, later changed to 4.
sss - Sender. 2 or 3 digits.
rrr - Receiver. 2 or 3 digits.
xx - Version of the CWR standard (version x.x).
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class CWRFileNameDecoder():
    """
    Parses a CWR file name into a FileTag class.

    As the file name is a very precise type of string, this parsing will be lossless, meaning that all the information
    from the file name will be always parsed into the resulting object.

    CWR file names follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
    CW - Header indicating it is a CWR file.
    yy - Year.
    nnnn - Sequence. This was originally 2 numbers, later changed to 4.
    sss - Sender. 2 or 3 digits.
    rrr - Receiver. 2 or 3 digits.
    xx - Version of the CWR standard (version x.x).
    """

    def __init__(self):
        pass

    def decode(self, file_name):
        """
        Decodes the file name, creating a FileTag from it.

        :param file_name: the file name to parse
        :return: a FileTag created from the file name
        """
        return filename.cwr_filename.parseString(file_name, parseAll=True)[0]

    def decode_old(self, file_name):
        """
        Decodes the file name, creating a FileTag from it.

        This uses the old format, where the sequence number is composed of two digits.

        It should be noted that this has been made obsolete, and files now should
        use four digits.

        These old files names follow the pattern CWyynnsss_rrr.Vxx.

        :param file_name: the file name to parse
        :return: a FileTag created from the file name
        """
        return filename.cwr_filename_old.parseString(file_name, parseAll=True)[0]


class CWRFileNameEncoder():
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
    """

    # Delimiters
    _header = 'CW'
    _ip_delimiter = '_'
    _version_delimiter = '.V'

    # Sequence lengths
    _sequence_l_current = 4
    _sequence_l_old = 2

    def __init__(self):
        pass

    def encode(self, identifier):
        """
        Parses a CWR file name from a FileTag object.

        This method follows the CWR naming convention update done by the CWR Management Committee, which increased the
        sequence length from two digits to four.

        After this change file names no longer follow the CISAC CWR standard, but allows for higher number of CWR file
        transmissions.

        :param identifier: FileTag to parse
        :return: a string file name parsed from the identifier info
        """
        return self._encode(identifier, self._sequence_l_current)

    def encode_old(self, identifier):
        """
        Parses a CWR file name from a FileTag object.

        This method follows the old format, where the sequence number is only two digits longs.

        It should be noted that this has been made obsolete, and files now should
        use four digits.

        These old files names follow the pattern CWyynnsss_rrr.Vxx.

        :param identifier: FileTag to parse
        :return: a string file name parsed from the identifier info
        """
        return self._encode(identifier, self._sequence_l_old)

    def _encode(self, identifier, sequence_l):
        """
        Parses a CWR file name from a FileTag object.

        As the sequence length was changed from the original specification, this method receives it's length.

        :param identifier: FileTag to parse
        :param sequence_l: the sequence length
        :return: a string file name parsed from the identifier info
        """
        sequence = str(identifier.sequence_n)[:4]
        while len(sequence) < sequence_l:
            sequence = '0' + sequence

        version = str(identifier.version)
        if len(version) > 2:
            version = version[:1] + version[-1:]
        while len(version) < 2:
            version = '0' + version

        year = str(identifier.year)[-2:]

        sender = identifier.sender[:3]
        receiver = identifier.receiver[:3]

        return self._header + year + sequence + sender + self._ip_delimiter + receiver + ".V" + version
