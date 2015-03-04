# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar import society
from cwr.grammar.field import table, special, record, basic
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
Publisher fields.
"""

# Publisher Sequence #
sequence_n = basic.numeric(_config.field_size('publisher', 'sequence_n'), compulsory=True)
sequence_n = sequence_n.setName('Publisher Sequence #').setResultsName('sequence_n')

# Publisher name
name = basic.alphanum(_config.field_size('publisher', 'name'))
name = name.setName('Publisher name').setResultsName('name')

# Publisher Unknown Indicator
unknown = basic.flag()
unknown = unknown.setName('Publisher Unknown Indicator').setResultsName('publisher_unknown')

# Tax ID #
tax_id = basic.numeric(_config.field_size('publisher', 'tax_id'))
tax_id = tax_id.setName('Tax ID #').setResultsName('tax_id')

# Submitter Agreement Number
agreement_id = basic.alphanum(_config.field_size('publisher', 'submitter_agreement_id'))
agreement_id = agreement_id.setName('Submitter Agreement Number').setResultsName('submitter_agreement_id')

# First Recording Refusal Indicator
first_refusal = basic.lookup(('Y', 'N'), columns=1)
first_refusal = first_refusal.setName('First Recording Refusal Indicator').setResultsName('first_record_refusal')

# Publisher IPI Base Number
ipi_base = special.ipi_base_number()

# International Standard Agreement Code
international_code = basic.alphanum(_config.field_size('publisher', 'international_code'))
international_code = international_code.setName('International Standard Agreement Code').setResultsName(
    'isac')

# Society-assigned Agreement Number
society_id = basic.alphanum(_config.field_size('publisher', 'society_agreement_id'))
society_id = society_id.setName('Society-assigned Agreement Number').setResultsName('society_agreement_id')

"""
Publisher patterns.
"""

publisher = special.lineStart + record.record_prefix(_config.record_type('publisher')) + sequence_n + \
            special.ip_id() + name + unknown + \
            table.publisher_type() + tax_id + special.ipi_name_number() + agreement_id + \
            society.pr_affiliation() + society.pr_share(max=50) + \
            society.mr_affiliation() + society.mr_share() + \
            society.sr_affiliation() + society.sr_share() + \
            table.special_agreement() + first_refusal + special.blank(1) + ipi_base + international_code + \
            society_id + table.agreement_type() + table.usa_license() + special.lineEnd

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