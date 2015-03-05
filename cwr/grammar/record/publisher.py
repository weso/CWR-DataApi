# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table, society
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import publisher as field_publisher
from cwr.interested_party import Publisher, PublisherRecord
from cwr.constraints import publisher as constraints


"""
CWR Publisher Record grammar.

This is for the following records:
- Publisher Controlled By Submitter Record (SPU)
- Other Publisher Record (OPU)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Publisher patterns.
"""

publisher = field_special.lineStart + field_record.record_prefix(_config.record_type('publisher'),
                                                                 compulsory=True) + field_publisher.sequence_n + \
            field_special.ip_id() + field_publisher.name + field_publisher.unknown + \
            field_table.publisher_type() + field_publisher.tax_id + field_special.ipi_name_number() + field_publisher.agreement_id + \
            society.pr_affiliation() + society.pr_share(maximum=50) + \
            society.mr_affiliation() + society.mr_share() + \
            society.sr_affiliation() + society.sr_share() + \
            field_table.special_agreement() + field_publisher.first_refusal + field_special.blank(
    1) + field_publisher.ipi_base + field_publisher.international_code + \
            field_publisher.society_id + field_table.agreement_type() + field_table.usa_license() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

publisher.setParseAction(lambda p: _to_publisherrecord(p))

"""
Validation actions for the patterns.
"""

publisher.addParseAction(lambda p: constraints.no_owner_has_no_shares(p[0]))
publisher.addParseAction(lambda p: constraints.owner_has_shares(p[0]))
publisher.addParseAction(lambda p: constraints.sequence_above_zero(p[0]))
publisher.addParseAction(lambda p: constraints.controlled_publisher_has_id(p[0]))
publisher.addParseAction(lambda p: constraints.controlled_or_known_publisher_has_name(p[0]))
publisher.addParseAction(lambda p: constraints.controlled_has_type(p[0]))
publisher.addParseAction(lambda p: constraints.controlled_has_unknown_blank(p[0]))
publisher.addParseAction(lambda p: constraints.other_has_unknown_not_blank(p[0]))
publisher.addParseAction(lambda p: constraints.other_unknown_has_no_name(p[0]))

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
    return Publisher(parsed.ip_id, parsed.name, parsed.ipi_base, parsed.tax_id, parsed.ipi_name)


def _to_publisherrecord(parsed):
    """
    Transforms the final parsing result into an PublisherRecord instance.

    :param parsed: result of parsing a Publisher record
    :return: an PublisherRecord created from the parsed record
    """
    publisher_data = _to_publisher(parsed)

    return PublisherRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                           publisher_data, parsed.sequence_n, parsed.submitter_agreement_id, parsed.publisher_type,
                           parsed.publisher_unknown, parsed.agreement_type, parsed.isac,
                           parsed.society_agreement_id, parsed.pr_society, parsed.pr_share,
                           parsed.mr_society, parsed.mr_share, parsed.sr_society,
                           parsed.sr_share, parsed.special_agreements,
                           parsed.first_record_refusal, parsed.usa_license)