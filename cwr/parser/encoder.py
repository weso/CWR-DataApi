# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


"""
Offers classes to parse data from CWR model instances.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Encoder(object):
    """
    Interface for encoders. These are parsers which transform a a model class into another data.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def encode(self, data):
        """
        Encodes the data, creating an structure from a model object instance.

        :param data: the data to encode
        :return: a data structure created from the received data
        """
        pass


class CWRFileTagEncoder(Encoder):
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
    __metaclass__ = ABCMeta

    # Delimiters
    _header = 'CW'
    _ip_delimiter = '_'
    _version_delimiter = '.V'

    # Sequence lengths
    _sequence_l_current = 4
    _sequence_l_old = 2

    def __init__(self):
        super(CWRFileTagEncoder, self).__init__()

    def _encode(self, tag, sequence_l):
        """
        Parses a CWR file name from a FileTag object.

        As the sequence length was changed from the original specification, this method receives it's length.

        :param tag: FileTag to parse
        :param sequence_l: the sequence length
        :return: a string file name parsed from the identifier info
        """
        sequence = str(tag.sequence_n)[:4]
        while len(sequence) < sequence_l:
            sequence = '0' + sequence

        version = str(tag.version)
        if len(version) > 2:
            version = version[:1] + version[-1:]
        while len(version) < 2:
            version = '0' + version

        year = str(tag.year)[-2:]

        sender = tag.sender[:3]
        receiver = tag.receiver[:3]

        return self._header + year + sequence + sender + self._ip_delimiter + receiver + ".V" + version


class CWRFileNameEncoder(CWRFileTagEncoder):
    # Sequence length
    _sequence_l = 4

    def __init__(self):
        super(CWRFileNameEncoder, self).__init__()

    def encode(self, tag):
        """
        Parses a CWR file name from a FileTag object.

        This method follows the CWR naming convention update done by the CWR Management Committee, which increased the
        sequence length from two digits to four.

        After this change file names no longer follow the CISAC CWR standard, but allows for higher number of CWR file
        transmissions.

        :param tag: FileTag to parse
        :return: a string file name parsed from the identifier info
        """
        return self._encode(tag, self._sequence_l)


class CWRFileNameEncoderOld(CWRFileTagEncoder):
    # Sequence lengths
    _sequence_l = 2

    def __init__(self):
        super(CWRFileNameEncoderOld, self).__init__()

    def encode(self, tag):
        """
        Parses a CWR file name from a FileTag object.

        This method follows the old format, where the sequence number is only two digits longs.

        It should be noted that this has been made obsolete, and files now should
        use four digits.

        These old files names follow the pattern CWyynnsss_rrr.Vxx.

        :param tag: FileTag to parse
        :return: a string file name parsed from the identifier info
        """
        return self._encode(tag, self._sequence_l)
