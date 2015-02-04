# -*- encoding: utf-8 -*-

from commonworks.domain.file import FileVersion

"""
CWR file utilities.

CWR files follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
CW - Header indicating it is a CWR file.
yy - Year.
nnnn - Sequence. This was originally 2 numbers, later changed to 4.
sss - Sender. 2 or 3 digits.
rrr - Receiver. 2 or 3 digits.
xx - Version
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_header_l = 2
_year_l = 2
_version_l = 2
_ipa_separator = '_'


def parse_filename(filename):
    """
    Parses a CWR file name into a FileVersion object.

    :param filename: file name to parse
    :return: a FileVersion object parsed from the file name
    """
    return _parse_filename(filename, 4)


def parse_filename_old(filename):
    """
    Parses a CWR file name into a FileVersion object.

    This parses a CWR file using the old standard, where the sequence is composed of two digits.

    This means these files name follow the pattern CWyynnsss_rrr.Vxx.

    :param filename: file name to parse
    :return: a FileVersion object parsed from the file name
    """
    return _parse_filename(filename, 2)


def _parse_filename(filename, sequence_l):
    """
    Parses a CWR file name into a FileVersion object.

    As the sequence length was changed from the original specification, this method receives it's length.

    :param filename: file name to parse
    :param sequence_l: the sequence length
    :return: a FileVersion object parsed from the file name
    """

    year = int(filename[_header_l:_header_l + _year_l])
    sequence = int(filename[_header_l + _year_l:_header_l + _year_l + sequence_l])
    version = int(filename[-_version_l:])

    # This contains the sender and receiver in a pattern similar 'sss_rrr'
    # The possible patterns are 'ss_rr', 'sss_rr', 'ss_rrr' and 'sss_rrr'
    leftover = filename[_header_l + _year_l + sequence_l:-(_version_l + 2)]
    pos = leftover.find(_ipa_separator)

    sender = leftover[:pos]
    receiver = leftover[pos + 1:]

    return FileVersion(year, sequence, sender, receiver, version)