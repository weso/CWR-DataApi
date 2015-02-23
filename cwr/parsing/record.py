# -*- encoding: utf-8 -*-

from cwr.file import TransactionRecord
from cwr.parsing.grammar import field, special, record
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
    Transforms the final parsing result into a TransactionRecord instance.

    :param parsed: result of parsing a record prefix
    :return: a TransactionRecord created from the record prefix
    """
    return TransactionRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n)


class TransactionRecordPrefixDecoder():
    """
    Parses a CWR record prefix into a TransactionRecord instance.

    Record prefixes are the first group of characters in each CWR file line.

    They are composed, in order, of:
    - Record type
    - Transaction number
    - Sequence number
    """

    data = ParserDataStorage()

    # Fields
    _transaction_n = field.numeric(
        data.expected_record_field_size('record_prefix', 'transaction_sequence_n')).setResultsName(
        "transaction_sequence_n")
    _sequence_n = field.numeric(data.expected_record_field_size('record_prefix', 'record_sequence_n')).setResultsName(
        "record_sequence_n")

    # Record prefix pattern
    _pattern = special.lineStart + record.record_type + _transaction_n + _sequence_n + special.lineEnd

    # Parsing actions
    _pattern.setParseAction(_to_recordprefix)

    def __init__(self):
        pass

    def decode(self, parsed):
        """
        Decodes the file name, creating a TransactionRecord from it.

        :param parsed: the record to parse
        :return: a TransactionRecord created from the record
        """
        return self._pattern.parseString(parsed)[0]