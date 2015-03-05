# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.record import agreement
from cwr.grammar.field import special, record, basic
from cwr.interested_party import WriterPublisherRecord


"""
CWR Publisher For Writer (PWR) records grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
General fields.
"""

# Publisher IP #
publisher_ip_id = special.ip_id()
publisher_ip_id = publisher_ip_id.setName('Publisher IP #').setResultsName('publisher_id')

# Publisher Name
publisher_name = basic.alphanum(_config.field_size('writer_publisher', 'publisher_name'))
publisher_name = publisher_name.setName('Publisher Name').setResultsName('publisher_name')

# Writer IP #
writer_ip_id = special.ip_id()
writer_ip_id = writer_ip_id.setName('Writer IP #').setResultsName('writer_id')

"""
Patterns.
"""

publisher = special.lineStart + record.record_prefix(
    _config.record_type(
        'writer_publisher')) + publisher_ip_id + publisher_name + agreement.submitter_agreement_n + \
            agreement.society_id + writer_ip_id + special.lineEnd

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
                                 parsed.publisher_id, parsed.writer_id, parsed.agreement_id,
                                 parsed.society_agreement_number)