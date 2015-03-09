# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

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
