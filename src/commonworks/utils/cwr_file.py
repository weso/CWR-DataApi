# -*- encoding: utf-8 -*-

from commonworks.file import FileTag

"""
CWR file utilities.

CWR files follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
CW - Header indicating it is a CWR file.
yy - Year.
nnnn - Sequence. This was originally 2 numbers, later changed to 4.
sss - Sender. 2 or 3 digits.
rrr - Receiver. 2 or 3 digits.
xx - Version of the CWR standard (version x.x).

It should be noted that the CISAC CWR standard specification indicates that the sequence should be two digits long.
But the CWR Management Committee increased it to four.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_header = 'CW'
_ipa_separator = '_'
_header_l = 2
_year_l = 2
_version_l = 2
_sequence_l_current = 4
_sequence_l_old = 2


def encode_filename_updated(identifier):
    """
    Parses a CWR file name from a FileTag object.

    This method follows the CWR naming convention update done by the CWR Management Committee, which increased the
    sequence length from two digits to four.

    After this change file names no longer follow the CISAC CWR standard, but allows for higher number of CWR file
    transmissions.

    :param identifier: FileTag to parse
    :return: a string file name parsed from the identifier info
    """
    return _encode_filename(identifier, _sequence_l_current)


def encode_filename(identifier):
    """
    Parses a CWR file name from a FileTag object.

    This method follows the CISAC CWR standard, where the sequence number is only two digits longs.

    It should be noted that this has been made obsolete by the CWR Management Committee, and files now should
    use four digits.

    These old files names follow the pattern CWyynnsss_rrr.Vxx.

    :param identifier: FileTag to parse
    :return: a string file name parsed from the identifier info
    """
    return _encode_filename(identifier, _sequence_l_old)


def decode_filename_updated(filename):
    """
    Parses a CWR file name into a FileTag object.

    This method follows the CWR naming convention update done by the CWR Management Committee, which increased the
    sequence length from two digits to four.

    After this change file names no longer follow the CISAC CWR standard, but allows for higher number of CWR file
    transmissions.

    :param filename: file name to parse
    :return: a FileTag object parsed from the file name
    """
    return _decode_filename(filename, _sequence_l_current)


def decode_filename(filename):
    """
    Parses a CWR file name into a FileTag object.

    This method follows the CISAC CWR standard, where the sequence number is only two digits longs.

    It should be noted that this has been made obsolete by the CWR Management Committee, and files now should
    use four digits.

    These old files names follow the pattern CWyynnsss_rrr.Vxx.

    :param filename: file name to parse
    :return: a FileTag object parsed from the file name
    """
    return _decode_filename(filename, _sequence_l_old)


def _decode_filename(filename, sequence_l):
    """
    Parses a CWR file name into a FileTag object.

    As the sequence length was changed from the original specification, this method receives it's length.

    :param filename: file name to parse
    :param sequence_l: the sequence length
    :return: a FileTag object parsed from the file name
    """

    year = int('20' + filename[_header_l:_header_l + _year_l])
    sequence = int(filename[_header_l + _year_l:_header_l + _year_l + sequence_l])

    # The version should be a decimal number, but is encoded as an integer
    version = filename[-_version_l:]
    version = float(version[:1] + '.' + version[-1:])

    # The leftover string will contain the sender and receiver in a pattern similar 'sss_rrr'
    # The length of these numbers is variable, so what matters is the position of the separator
    leftover = filename[_header_l + _year_l + sequence_l:-(_version_l + 2)]
    pos = leftover.find(_ipa_separator)

    sender = leftover[:pos]
    receiver = leftover[pos + 1:]

    return FileTag(year, sequence, sender, receiver, version)


def _encode_filename(identifier, sequence_l):
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

    return _header + year + sequence + sender + _ipa_separator + receiver + ".V" + version