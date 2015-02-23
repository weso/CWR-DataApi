# -*- encoding: utf-8 -*-

from cwr.parsing.grammar import transmission


"""
CWR Transmission parsing classes.

These classes allow decoding and encoding Transmission records.

These are the Transmission Header (HDR) and Transmission Trailer (TRL).
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TransmissionHeaderDecoder():
    """
    Parses a CWR Transmission Header (HDR) into a TransmissionHeader instance.

    The Transmission Header is the first record on the file.

    It is composed, in order, of:
    - Record type
    - Sender type
    - Sender ID
    - Sender Name
    - EDI Standard
    - Version Number
    - Creation Date
    - Creation Time
    - Transmission Date
    - Character Set
    """

    def __init__(self):
        pass

    def decode(self, record):
        """
        Decodes the Transmission Header, creating a TransmissionHeader from it.

        :param record: the record to parse
        :return: a TransmissionHeader created from the record
        """
        return transmission.transmission_header.parseString(record, parseAll=True)[0]