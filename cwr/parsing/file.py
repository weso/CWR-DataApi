# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.file import FileTag


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


def _to_version(parsed):
    """
    Transforms a string representing the file format into a float of two values representing the file CWR version.

    This is used by the parser to create the version number.

    :param parsed: result of parsing the file format
    :return: a float composed of two numeric values
    """
    number = parsed[0]
    return float(number[:1] + '.' + number[-1:])


def _to_default_version(parsed):
    """
    Transforms a string representing the file format into a float of two values representing the default CWR version.

    This is for files which are not CWR files, such as zipped files.

    :param parsed: result of parsing the file format
    :return: a float representing the default version
    """
    return 2.1


def _to_integer(parsed):
    """
    Transforms a string into an integer.

    This is used during the parsing process.

    :param parsed: result of parsing a number
    :return: an integer created from the input
    """
    return int(parsed[0])


def _to_year(parsed):
    """
    Transforms a string with two numeric values into a year.

    The resulting year will be in the current century.

    This is used during the parsing process.

    :param parsed: result of parsing a date
    :return: a year created from the input
    """
    return int('20' + parsed[0])


def _to_filetag(parsed):
    """
    Transforms the final parsing result into a FileTag instance.

    :param parsed: result of parsing a file name
    :return: a FileTag created from the file name
    """
    return FileTag(parsed.year, parsed.sequence_n, parsed.sender, parsed.receiver, parsed.version)


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

    # Fields
    _sequence_old = pp.Word(pp.nums, exact=2).setResultsName("sequence_n")
    _sequence_new = pp.Word(pp.nums, exact=4).setResultsName("sequence_n")
    _year = pp.Word(pp.nums, exact=2).setResultsName("year")
    _sender = pp.Word(pp.alphanums, min=2, max=3).setResultsName("sender")
    _receiver = pp.Word(pp.alphanums, min=2, max=3).setResultsName("receiver")
    _version_num = pp.Word(pp.nums, exact=2).setResultsName("version")

    # Delimiters
    _header = pp.CaselessLiteral('CW').suppress()
    _delimiter_version = pp.CaselessLiteral('.V').suppress()
    _delimiter_ip = pp.Literal('_').suppress()
    _delimiter_zip = pp.CaselessLiteral('.zip').setResultsName("version")

    # CWR file patterns
    _cwr_pattern_old = _header + _year + _sequence_old + _sender + \
                       _delimiter_ip + _receiver + ((_delimiter_version + _version_num) | _delimiter_zip)
    _cwr_pattern = _header + _year + _sequence_new + _sender + \
                   _delimiter_ip + _receiver + ((_delimiter_version + _version_num) | _delimiter_zip)

    # Parsing actions
    _version_num.setParseAction(_to_version)
    _delimiter_zip.setParseAction(_to_default_version)
    _sequence_old.setParseAction(_to_integer)
    _sequence_new.setParseAction(_to_integer)
    _year.setParseAction(_to_year)

    _cwr_pattern.setParseAction(_to_filetag)
    _cwr_pattern_old.setParseAction(_to_filetag)

    def __init__(self):
        pass

    def decode(self, filename):
        """
        Decodes the file name, creating a FileTag from it.

        :param filename: the file name to parse
        :return: a FileTag created from the file name
        """
        return self._cwr_pattern.parseString(filename, parseAll=True)[0]

    def decode_old(self, filename):
        """
        Decodes the file name, creating a FileTag from it.

        This uses the old format, where the sequence number is composed of two digits.

        It should be noted that this has been made obsolete, and files now should
        use four digits.

        These old files names follow the pattern CWyynnsss_rrr.Vxx.

        :param filename: the file name to parse
        :return: a FileTag created from the file name
        """
        return self._cwr_pattern_old.parseString(filename, parseAll=True)[0]


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
