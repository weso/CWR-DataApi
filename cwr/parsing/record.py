# -*- encoding: utf-8 -*-

from cwr.parsing import grammar
from cwr.file import RecordPrefix

"""
CWR record parsing classes.

These classes allow decoding and encoding pieces of records.

A record is a line of a CWR file.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _to_integer(data):
    """
    Transforms a string into an integer.

    This is used during the parsing process.

    :param data: result of parsing a number
    :return: an integer created from the input
    """
    return int(data[0])


def _to_recordprefix(data):
    return RecordPrefix(data.record_type, data.transaction_sequence_n, data.record_sequence_n)


class RecordPrefixDecoder(object):
    _record_type = grammar.record_type.copy()
    _transaction_n = grammar.transaction_n.copy()
    _sequence_n = grammar.sequence_n.copy()

    _pattern = _record_type + _transaction_n + _sequence_n

    # Parsing actions
    _transaction_n.setParseAction(_to_integer)
    _sequence_n.setParseAction(_to_integer)
    _pattern.setParseAction(_to_recordprefix)

    def __init__(self):
        pass

    def parse(self, record):
        return self._pattern.parseString(record)[0]