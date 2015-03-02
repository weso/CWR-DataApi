# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field, field_special, record, society, table
from cwr.interested_party import Publisher, PublisherRecord


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
_tables = CWRTables()
_config = CWRConfiguration()

"""
Publisher fields.
"""

# Publisher Sequence #
sequence_n = field.numeric(_config.field_size('publisher', 'sequence_n'), compulsory=True)
sequence_n = sequence_n.setName('Publisher Sequence #').setResultsName('sequence_n')

# Publisher name
name = field.alphanum(_config.field_size('publisher', 'name'))
name = name.setName('Publisher name').setResultsName('name')

# Publisher Unknown Indicator
unknown = field.flag()
unknown = unknown.setName('Publisher Unknown Indicator').setResultsName('publisher_unknown')

# Tax ID #
tax_id = field.alphanum(_config.field_size('publisher', 'tax_id'))
tax_id = tax_id.setName('Tax ID #').setResultsName('tax_id')

# Submitter Agreement Number
agreement_id = field.alphanum(_config.field_size('publisher', 'submitter_agreement_id'))
agreement_id = agreement_id.setName('Submitter Agreement Number').setResultsName('submitter_agreement_id')

# PR Affiliation Society #
pr_society = field.alphanum(_config.field_size('publisher', 'pr_society'))
pr_society = pr_society.setName('PR Affiliation Society #').setResultsName('pr_society')

# First Recording Refusal Indicator
first_refusal = field.flag()
first_refusal = first_refusal.setName('First Recording Refusal Indicator').setResultsName('first_record_refusal')

# Filler
filler = pp.Literal(' ')
filler.leaveWhitespace()
filler.suppress()

# Publisher IPI Base Number
ipi_base = field_special.ipi_base_number()

# International Standard Agreement Code
international_code = field.alphanum(_config.field_size('publisher', 'international_code'))
international_code = international_code.setName('International Standard Agreement Code').setResultsName(
    'isac')

# Society-assigned Agreement Number
society_id = field.alphanum(_config.field_size('publisher', 'society_agreement_id'))
society_id = society_id.setName('Society-assigned Agreement Number').setResultsName('society_agreement_id')

"""
Publisher patterns.
"""

publisher = field_special.lineStart + record.record_prefix(_config.record_type('publisher')) + sequence_n + \
            field_special.ip_id() + name + unknown + \
            table.publisher_type + tax_id + field_special.ipi_name_number() + agreement_id + \
            society.pr_affiliation() + society.pr_share + \
            society.mr_affiliation() + society.mr_share + \
            society.sr_affiliation() + society.sr_share + \
            table.special_agreement + first_refusal + filler + ipi_base + international_code + \
            society_id + table.agreement_type + table.usa_license + field_special.lineEnd

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
    :return: an Publisher created from the parsed record
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