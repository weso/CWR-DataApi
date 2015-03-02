# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field, field_special, record


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

# Record Prefix
record_prefix_publisher = record.record_prefix(_config.record_type('publisher'))

# Publisher Sequence #
sequence_n = field.numeric(_config.field_size('publisher', 'sequence_n'))
sequence_n = sequence_n.setName('Publisher Sequence #').setResultsName('sequence_n')

# Interested Party #
ip_id = field_special.ip_id()

# Publisher name
name = field.alphanum(_config.field_size('publisher', 'name'))
name = name.setName('Publisher name').setResultsName('name')

# Publisher Unknown Indicator
unknown = field.flag()
unknown = unknown.setName('Publisher Unknown Indicator').setResultsName('unknown')

# Publisher Type
publisher_type = pp.oneOf(_tables.publisher_types())
publisher_type = publisher_type.setName('Publisher Type').setResultsName('publisher_type')

# Tax ID #
tax_id = field.alphanum(_config.field_size('publisher', 'tax_id'))
tax_id = tax_id.setName('Tax ID #').setResultsName('tax_id')

# Publisher IPI Name #
ipi_name = field_special.ipi_name_number()

# Submitter Agreement Number
agreement_id = field.alphanum(_config.field_size('publisher', 'agreement_id'))
agreement_id = agreement_id.setName('Submitter Agreement Number').setResultsName('agreement_id')

# PR Affiliation Society #
pr_society = field.alphanum(_config.field_size('publisher', 'pr_society'))
pr_society = pr_society.setName('PR Affiliation Society #').setResultsName('pr_society')

# Special Agreements Indicator
special_agreement = pp.oneOf(_tables.special_agreement_indicators())
special_agreement = special_agreement.setName('Special Agreements Indicator').setResultsName('special_agreement')

# First Recording Refusal Indicator
first_refusal = field.flag()
first_refusal = first_refusal.setName('First Recording Refusal Indicator').setResultsName('first_refusal')

# Filler
filler = pp.Literal(' ')
filler.leaveWhitespace()
filler.suppress()

# Publisher IPI Base Number
ipi_base = field_special.ipi_base_number()
ipi_base = ipi_base.setName('Publisher IPI Base Number').setResultsName('ipi_base')

# International Standard Agreement Code
international_code = field.alphanum(_config.field_size('publisher', 'international_code'))
international_code = international_code.setName('International Standard Agreement Code').setResultsName(
    'international_code')

# Society-assigned Agreement Number
society_id = field.alphanum(_config.field_size('publisher', 'society_id'))
society_id = society_id.setName('Society-assigned Agreement Number').setResultsName('society_id')

# USA License Indicator
usa_license = pp.oneOf(_tables.usa_license_indicators())
usa_license = usa_license.setName('USA License Indicator').setResultsName('usa_license')