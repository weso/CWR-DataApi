# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.interested_party import Publisher, PublisherRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Publisher Record grammar.

This is for the following records:
- Publisher Controlled By Submitter Record (SPU)
- Other Publisher Record (OPU)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
Publisher patterns.
"""

publisher = _factory_record.get_transaction_record('publisher')

"""
Parsing actions for the patterns.
"""

publisher.setParseAction(lambda p: _to_publisherrecord(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_publisher(parsed):
    """
    Transforms the final parsing result into an Publisher instance.

    :param parsed: result of parsing the Publisher info in a Publisher record
    :return: a Publisher created from the parsed record
    """
    return Publisher(parsed.ip_n, parsed.name, parsed.ipi_base_n, parsed.tax_id, parsed.ipi_name_n)


def _to_publisherrecord(parsed):
    """
    Transforms the final parsing result into an PublisherRecord instance.

    :param parsed: result of parsing a Publisher record
    :return: an PublisherRecord created from the parsed record
    """
    publisher_data = _to_publisher(parsed)

    return PublisherRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                           publisher_data, parsed.publisher_sequence_n, parsed.submitter_agreement_n,
                           parsed.publisher_type,
                           parsed.publisher_unknown, parsed.agreement_type, parsed.international_standard_code,
                           parsed.society_assigned_agreement_n, parsed.pr_society, parsed.pr_share,
                           parsed.mr_society, parsed.mr_share, parsed.sr_society,
                           parsed.sr_share, parsed.special_agreement_indicator,
                           parsed.first_recording_refusal, parsed.usa_license_indicator)