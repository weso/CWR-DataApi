# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Agreement record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Submitter's Agreement Number
submitter_agreement_n = basic.alphanum(_config.field_size('agreement', 'agreement_id'), compulsory=True)
submitter_agreement_n = submitter_agreement_n.setName('Submitters Agreement Number').setResultsName('agreement_id')

# International Standard Agreement Code
is_code = basic.alphanum(_config.field_size('agreement', 'international_standard_code'))
is_code = is_code.setName('International Standard Agreement Code').setResultsName('international_standard_code')

# Agreement Start Date
agreement_start_date = basic.date(compulsory=True)
agreement_start_date = agreement_start_date.setName('Agreement Start Date').setResultsName('start_date')

# Agreement End Date
agreement_end_date = basic.date()
agreement_end_date = agreement_end_date.setName('Agreement End Date').setResultsName('end_date')

# Retention End Date
retention_end_date = basic.date()
retention_end_date = retention_end_date.setName('Retention End Date').setResultsName('retention_end_date')

# Prior Royalty Start Date
prior_royalty_start_date = basic.date()
prior_royalty_start_date = prior_royalty_start_date.setName('Prior Royalty Start Date').setResultsName(
    'prior_royalty_start_date')

# Post Term Collection End Date
post_term_collection_end_date = basic.date()
post_term_collection_end_date = post_term_collection_end_date.setName('Post Term Collection End Date').setResultsName(
    'post_term_collection_end_date')

# Date of Signature of Agreement
date_of_signature = basic.date()
date_of_signature = date_of_signature.setName('Date of Signature of Agreement').setResultsName('signature_date')

# Number of Works
number_works = basic.numeric(_config.field_size('agreement', 'number_works'), compulsory=True)
number_works = number_works.setName('Number of Works').setResultsName('works_number')

# Shares Change
sales_change = basic.boolean()
sales_change = sales_change.setName('Shares Change').setResultsName('shares_change')

# Advance Given
advance_given = basic.boolean()
advance_given = advance_given.setName('Advance Given').setResultsName('advance_given')

# Society Given Agreement Number
society_id = basic.alphanum(_config.field_size('agreement', 'society_agreement_number'))
society_id = society_id.setName('Society Given Agreement Number').setResultsName('society_agreement_number')
society_id.leaveWhitespace()
