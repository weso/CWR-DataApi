# -*- encoding: utf-8 -*-

from cwr.file import RecordPrefix
from cwr.parsing import grammar
from cwr.parsing.data.accessor import ParserDataStorage


"""
CWR record parsing classes.

These classes allow decoding and encoding pieces of records.

A record is a line of a CWR file.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _to_recordprefix(parsed):
    """
    Transforms the final parsing result into a RecordPrefix instance.

    :param parsed: result of parsing a record prefix
    :return: a RecordPrefix created from the record prefix
    """
    return RecordPrefix(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n)


class RecordPrefixDecoder():
    """
    Parses a CWR record prefix into a RecordPrefix instance.

    Record prefixes are the first group of characters in each CWR file line.

    They are composed, in order, of:
    - Record type
    - Transaction number
    - Sequence number
    """

    data = ParserDataStorage()

    # Fields
    _transaction_n = grammar.numeric(
        data.expected_record_field_size('record_prefix', 'transaction_sequence_n')).setResultsName(
        "transaction_sequence_n")
    _sequence_n = grammar.numeric(data.expected_record_field_size('record_prefix', 'record_sequence_n')).setResultsName(
        "record_sequence_n")

    # Record prefix pattern
    _pattern = grammar.lineStart + grammar.record_type + _transaction_n + _sequence_n + grammar.lineEnd

    # Parsing actions
    _pattern.setParseAction(_to_recordprefix)

    def __init__(self):
        pass

    def decode(self, record):
        """
        Decodes the file name, creating a RecordPrefix from it.

        :param record: the record to parse
        :return: a RecordPrefix created from the record
        """
        return self._pattern.parseString(record)[0]