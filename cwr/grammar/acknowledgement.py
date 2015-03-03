# -*- encoding: utf-8 -*-

import datetime

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar import field, field_special, record, group, field_table
from cwr.acknowledgement import AcknowledgementRecord
from cwr.constraints import acknowledgement as constraints


"""
CWR Acknowledgement grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Acknowledgement fields.
"""

# Creation Date
creation_date = field.date(compulsory=True)
creation_date = creation_date.setName('Creation Date').setResultsName('creation_date')

# Creation Time
creation_time = field.time(compulsory=True)
creation_time = creation_time.setName('Creation Time').setResultsName('creation_time')

# Original Group ID
original_group_id = group.group_id
original_group_id = original_group_id.setName('Original Group ID')

# Original Transaction Sequence #
original_transaction_n = field.numeric(_config.field_size('acknowledgement', 'transaction_n'), compulsory=True)
original_transaction_n = original_transaction_n.setName('Original Transaction Sequence #').setResultsName(
    'transaction_n')

# Creation Title
creation_title = field.alphanum(_config.field_size('acknowledgement', 'title'))
creation_title = creation_title.setName('Creation Title').setResultsName('title')

# Submitter Creation #
submitter_creation_n = field.alphanum(_config.field_size('acknowledgement', 'submitter_id'))
submitter_creation_n = submitter_creation_n.setName('Submitter Creation #').setResultsName('submitter_id')

# Recipient Creation #
recipient_creation_n = field.alphanum(_config.field_size('acknowledgement', 'recipient_id'))
recipient_creation_n = recipient_creation_n.setName('Recipient Creation #').setResultsName('recipient_id')

# Processing Date
processing_date = field.date(compulsory=True)
processing_date = processing_date.setName('Processing Date').setResultsName('processing_date')

"""
Acknowledgment patterns.
"""

# Creation date and time pattern
creation_date_time = pp.Group(creation_date + creation_time)
creation_date_time = creation_date_time.setName('Creation Date and Time').setResultsName('creation_date_time')

# Acknowledgment Pattern
acknowledgement = field_special.lineStart + record.record_prefix(_config.record_type('acknowledgement')) + \
                  creation_date_time + \
                  original_group_id + original_transaction_n + field_table.original_transaction_type(
    True) + creation_title + \
                  submitter_creation_n + recipient_creation_n + processing_date + field_table.transaction_status(True) + \
                  field_special.lineEnd

"""
Parsing actions for the patterns.
"""

creation_date_time.setParseAction(lambda d: _combine_date_time(d[0].creation_date, d[0].creation_time))

acknowledgement.setParseAction(lambda a: _to_acknowledgement_record(a))

"""
Validation actions for the patterns.
"""

acknowledgement.addParseAction(lambda p: constraints.title_when_record_requires(p[0]))

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


def _to_acknowledgement_record(parsed):
    """
    Transforms the final parsing result into an AcknowledgementRecord instance.

    :param parsed: result of parsing an Acknowledgement record
    :return: a AcknowledgementRecord created from the parsed record
    """
    return AcknowledgementRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                 parsed.group_id, parsed.transaction_n, parsed.transaction_type,
                                 parsed.transaction_status, parsed.creation_date_time, parsed.processing_date,
                                 parsed.title, parsed.submitter_id, parsed.recipient_id)