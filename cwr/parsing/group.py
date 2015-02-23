# -*- encoding: utf-8 -*-

from cwr.parsing.grammar import group


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

    def __init__(self):
        pass

    def decode(self, record):
        """
        Decodes the Group Header, creating a GroupHeader from it.

        :param record: the record to parse
        :return: a GroupHeader created from the record
        """
        return group.group_header.parseString(record, parseAll=True)