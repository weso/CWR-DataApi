# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import field, special


"""
CWR Group parsing classes.

These classes allow decoding and encoding Group records.

These are the Group Header (GRH) and Group Trailer (GRT).
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class GroupHeaderDecoder():
    """
    Parses a CWR Group Header (GRH) into a GroupHeader instance.

    The Group Header is the first record on a Group.

    It is composed, in order, of:
    - Record type
    - Transaction type
    - Group ID
    - Version number
    - Batch request
    - Submission/Distribution type (unused)
    """

    data = ParserDataStorage()

    # Fields
    _record_type = pp.Literal(data.expected_record_type('group_header')).setResultsName('record_type')
    _transaction_type = pp.oneOf(data.transaction_types()).setResultsName('transaction_type')
    _group_id = field.numeric_from(data.expected_record_field_size('group_header', 'group_id'), 1).setResultsName(
        'group_id')
    _version_number = pp.Literal(data.expected_record_field_value('group_header', 'version_number')).setResultsName(
        'version_number')
    _batch_request_id = field.numeric(
        data.expected_record_field_size('group_header', 'batch_request_id')).setResultsName(
        'batch_request_id')
    _sd_type = field.alphanum(data.expected_record_field_size('group_header', 'sd_type')).setResultsName(
        'sd_type')

    # Group Header pattern
    _pattern = special.lineStart + _record_type + _transaction_type + _group_id + _version_number + _batch_request_id + \
               (_sd_type | pp.empty) + special.lineEnd

    def __init__(self):
        pass

    def decode(self, record):
        """
        Decodes the Group Header, creating a GroupHeader from it.

        :param record: the record to parse
        :return: a GroupHeader created from the record
        """
        return self._pattern.parseString(record)