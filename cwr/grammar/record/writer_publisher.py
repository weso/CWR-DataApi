# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.interested_party import PublisherForWriterRecord
from cwr.grammar.factory.field import DefaultFieldFactory


"""
CWR Publisher For Writer (PWR) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_agr_factory = DefaultFieldFactory(_config.load_field_config('agreement'))
_writer_publisher_factory = DefaultFieldFactory(_config.load_field_config('writer_publisher'))

"""
Patterns.
"""

publisher = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('writer_publisher'), compulsory=True) + \
            _writer_publisher_factory.get_field('publisher_ip_n') + \
            _writer_publisher_factory.get_field('publisher_name') + \
            _agr_factory.get_field('submitter_agreement_n', compulsory=True) + \
            _agr_factory.get_field('society_assigned_agreement_n') + \
            _writer_publisher_factory.get_field('writer_ip_n') + \
            field_special.lineEnd

"""
Parsing actions for the patterns.
"""

publisher.setParseAction(lambda p: _to_publisher(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_publisher(parsed):
    """
    Transforms the final parsing result into a WriterPublisherRecord instance.

    :param parsed: result of parsing a Writer Publisher record
    :return: a WriterPublisherRecord created from the parsed record
    """
    return PublisherForWriterRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                    parsed.publisher_ip_n, parsed.writer_ip_n, parsed.submitter_agreement_n,
                                    parsed.society_assigned_agreement_n)