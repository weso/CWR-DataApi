# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import agreement as field_agreement
from cwr.grammar.field import writer_publisher as field_writer_publisher
from cwr.interested_party import WriterPublisherRecord


"""
CWR Publisher For Writer (PWR) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Patterns.
"""

publisher = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'writer_publisher'),
    compulsory=True) + field_writer_publisher.publisher_ip_number + field_writer_publisher.publisher_name + field_agreement.submitter_agreement_n + \
            field_agreement.society_assigned_agreement_n + field_writer_publisher.writer_ip_n + field_special.lineEnd

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
    return WriterPublisherRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                 parsed.publisher_ip_number, parsed.writer_ip_n, parsed.submitter_agreement_n,
                                 parsed.society_assigned_agreement_n)