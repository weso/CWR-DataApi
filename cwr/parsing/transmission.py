# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing import grammar

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

    data = ParserDataStorage()

    # Fields
    _record_type = pp.Literal('HDR')
    _sender_type = pp.oneOf(data.sender_types()).setResultsName('sender_type')
    _sender_id = pp.Word(pp.nums, exact=9).setResultsName('sender_id')
    _sender_name = pp.Word(grammar.alphanum_type, exact=45).setResultsName('sender_name')
    _edi_version = pp.Regex('\d\d\.\d\d').setResultsName('edi_version')
    _creation_date = grammar.date_field.copy().setResultsName('creation_date')
    _creation_time = grammar.time_field.copy().setResultsName('creation_time')
    _transmission_date = grammar.date_field.copy().setResultsName('transmission_date')
    _character_set = grammar.char_code.copy().setResultsName('character_set')

    # Transmission Header pattern
    _pattern = _record_type + _sender_type + _sender_id + _sender_name + _edi_version + _creation_date + _creation_time \
               + _transmission_date + _character_set

    def decode(self, record):
        """
        Decodes the Transmission Header, creating a TransmissionHeader from it.

        :param record: the record to parse
        :return: a TransmissionHeader created from the file name
        """
        return self._pattern.parseString(record, parseAll=True)[0]