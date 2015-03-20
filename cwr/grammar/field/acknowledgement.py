# -*- coding: utf-8 -*-

import datetime

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory


"""
CWR Acknowledgement record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_ack_factory = DefaultFieldFactory(_config.load_field_config('acknowledgement'))

# Creation Date
creation_date = _ack_factory.get_field('creation_date', compulsory=True)

# Creation Time
creation_time = _ack_factory.get_field('creation_time', compulsory=True)

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