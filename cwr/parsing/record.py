# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.file import RecordPrefix
from cwr.parsing import grammar


"""
CWR record parsing classes.

These classes allow decoding and encoding pieces of records.

A record is a line of a CWR file.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _to_integer(parsed):
    """
    Transforms a string into an integer.

    This is used during the parsing process.

    :param parsed: result of parsing a number
    :return: an integer created from the input
    """
    return int(parsed[0])


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

    # Fields
    _transaction_n = pp.Word(pp.nums, exact=8).setResultsName("transaction_sequence_n")
    _sequence_n = pp.Word(pp.nums, exact=8).setResultsName("record_sequence_n")

    # Record prefix pattern
    _pattern = grammar.record_type + _transaction_n + _sequence_n

    # Parsing actions
    _transaction_n.setParseAction(_to_integer)
    _sequence_n.setParseAction(_to_integer)
    _pattern.setParseAction(_to_recordprefix)

    def decode(self, record):
        """
        Decodes the file name, creating a RecordPrefix from it.

        :param record: the record to parse
        :return: a RecordPrefix created from the file name
        """
        return self._pattern.parseString(record, parseAll=True)[0]