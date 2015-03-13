# -*- coding: utf-8 -*-

import datetime

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.field import group
from cwr.grammar.field import basic


"""
CWR Acknowledgement record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Creation Date
creation_date = basic.date(compulsory=True)
creation_date = creation_date.setName('Creation Date').setResultsName('creation_date')

# Creation Time
creation_time = basic.time(compulsory=True)
creation_time = creation_time.setName('Creation Time').setResultsName('creation_time')

# Original Group ID
original_group_id = group.group_id
original_group_id = original_group_id.setName('Original Group ID')

# Original Transaction Sequence #
original_transaction_sequence_n = basic.numeric(_config.field_size('acknowledgement', 'transaction_n'), compulsory=True)
original_transaction_sequence_n = original_transaction_sequence_n.setName(
    'Original Transaction Sequence #').setResultsName(
    'original_transaction_sequence_n')

# Creation Title
creation_title = basic.alphanum(_config.field_size('acknowledgement', 'title'))
creation_title = creation_title.setName('Creation Title').setResultsName('creation_title')

# Submitter Creation #
submitter_creation_n = basic.alphanum(_config.field_size('acknowledgement', 'submitter_id'))
submitter_creation_n = submitter_creation_n.setName('Submitter Creation #').setResultsName('submitter_creation_n')

# Recipient Creation #
recipient_creation_n = basic.alphanum(_config.field_size('acknowledgement', 'recipient_id'))
recipient_creation_n = recipient_creation_n.setName('Recipient Creation #').setResultsName('recipient_creation_n')

# Processing Date
processing_date = basic.date(compulsory=True)
processing_date = processing_date.setName('Processing Date').setResultsName('processing_date')

# Creation date and time pattern
creation_date_time = pp.Group(creation_date + creation_time)
creation_date_time = creation_date_time.setName('Creation Date and Time').setResultsName('creation_date_time')

"""
Parsing actions for the patterns.
"""

creation_date_time.setParseAction(lambda d: _combine_date_time(d[0].creation_date, d[0].creation_time))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _combine_date_time(date, time):
    """
    Combines the received date and time.

    :param date: date to combine
    :param time: time to combine
    :return: the date and time combined
    """
    return datetime.datetime.combine(date, time)