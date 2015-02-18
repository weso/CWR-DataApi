# -*- encoding: utf-8 -*-

from cwr.parsing import grammar

"""
CWR record parsing classes.

These classes allow decoding and encoding pieces of records.

A record is a line of a CWR file.
"""

__author__ = 'Benardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class RecordPrefixDecoder(object):
    _pattern = grammar.record_prefix

    def __init__(self):
        pass

    def parse(self, record):
        return self._pattern.parseString(record)