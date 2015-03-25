# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.interested_party import Publisher, PublisherRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


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

_factory = DefaultFieldFactory(_data, CWRTables())

"""
Publisher patterns.
"""

publisher = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('publisher')) + \
            _factory.get_field('publisher_sequence_n', compulsory=True) + \
            _factory.get_field('ip_n') + \
            _factory.get_field('name') + \
            _factory.get_field('publisher_unknown') + \
            _factory.get_field('publisher_type') + \
            _factory.get_field('tax_id') + \
            _factory.get_field('ipi_name_n') + \
            _factory.get_field('submitter_agreement_n') + \
            _factory.get_field('pr_affiliation') + \
            _factory.get_field('pr_share_50', compulsory=True) + \
            _factory.get_field('mr_affiliation') + \
            _factory.get_field('mr_share', compulsory=True) + \
            _factory.get_field('sr_affiliation') + \
            _factory.get_field('sr_share', compulsory=True) + \
            _factory.get_field('special_agreement_indicator') + \
            _factory.get_field('first_recording_refusal') + \
            _factory.get_field('blank') + \
            _factory.get_field('ipi_base_n') + \
            _factory.get_field('international_standard_code') + \
            _factory.get_field('society_assigned_agreement_n') + \
            _factory.get_field('agreement_type') + \
            _factory.get_field('usa_license_indicator') + \
            field_special.lineEnd

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
                           parsed.society_assigned_agreement_n, parsed.pr_affiliation, parsed.pr_share,
                           parsed.mr_affiliation, parsed.mr_share, parsed.sr_affiliation,
                           parsed.sr_share, parsed.special_agreement_indicator,
                           parsed.first_recording_refusal, parsed.usa_license_indicator)