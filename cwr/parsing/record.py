# -*- encoding: utf-8 -*-

from cwr.parsing.grammar import record
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


    def __init__(self):
        pass

    def decode(self, parsed):
        """
        Decodes the file name, creating a TransactionRecord from it.

        :param parsed: the record to parse
        :return: a TransactionRecord created from the record
        """
        return record.record_prefix.parseString(parsed)[0]