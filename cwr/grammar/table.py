# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field


"""
Grammar for concrete CWR Table/List Lookup fields.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Lookup fields.
"""

# Original Transaction Type
original_transaction_type = field.lookup(_tables.record_types(), compulsory=True)
original_transaction_type = original_transaction_type.setName('Original Transaction Type').setResultsName(
    'transaction_type')

# Transaction Status
transaction_status = field.lookup(_tables.transaction_status(), compulsory=True)
transaction_status = transaction_status.setName('Transaction Status').setResultsName('transaction_status')

# Prior Royalty Status
prior_royalty_status = field.lookup(_config.field_value('agreement', 'prior_royalty_status'), compulsory=True)
prior_royalty_status = prior_royalty_status.setName('Prior Royalty Status').setResultsName('prior_royalty_status')

# Post Term Collection Status
post_term_collection_status = field.lookup(_config.field_value('agreement', 'post_term_collection_status'),
                                           compulsory=True)
post_term_collection_status = post_term_collection_status.setName('Post Term Collection Status').setResultsName(
    'post_term_collection_status')

# Sales/Manufacture Clause
sm_clause = field.lookup(_config.field_value('agreement', 'sales_manufacture_clause'))
sm_clause = sm_clause.setName('Sales/Manufacture Clause').setResultsName('sales_manufacture_clause')

# Inclusion/Exclusion Indicator
ie_indicator = field.lookup(_config.field_value('agreement_territory', 'ie_indicator'), compulsory=True)
ie_indicator = ie_indicator.setName('Inclusion/Exclusion Indicator').setResultsName('ie_indicator')

# TIS Numeric Code
tis_code = field.lookup(_tables.tis_codes(), compulsory=True)
tis_code = tis_code.setName('TIS Numeric Code').setResultsName('tis_code')
tis_code.setParseAction(lambda c: int(c[0]))

# Agreement Role Code
agreement_role_code = field.lookup(_tables.agreement_roles(), compulsory=True)
agreement_role_code = agreement_role_code.setName('Agreement Role Code').setResultsName('agreement_role_code')

# Language Code
language = field.lookup(_tables.language_codes(), columns=2)
language = language.setName('Language Code').setResultsName('language')

# Publisher Type
publisher_type = field.lookup(_tables.publisher_types(), columns=2)
publisher_type = publisher_type.setName('Publisher Type').setResultsName('publisher_type')

# Special Agreements Indicator
special_agreement = field.lookup(_tables.special_agreement_indicators())
special_agreement = special_agreement.setName('Special Agreements Indicator').setResultsName('special_agreements')

# Transaction type
transaction_type = field.lookup(_tables.transaction_types(), compulsory=True)
transaction_type = transaction_type.setName('Transaction Type').setResultsName('transaction_type')

# Sender Type
sender_type = field.lookup(_tables.sender_types(), compulsory=True)
sender_type = sender_type.setName('Sender Type').setResultsName('sender_type')

# Musical Work Distribution Category
musical_distribution_category = field.lookup(_tables.musical_work_distribution_categories(), compulsory=True)
musical_distribution_category = musical_distribution_category.setName(
    'Musical Work Distribution Category').setResultsName('musical_distribution_category')

# Text Music Relationship
text_music_relationship = field.lookup(_tables.text_music_relationships(), compulsory=True)
text_music_relationship = text_music_relationship.setName('Text Music Relationship').setResultsName(
    'text_music_relationship')

# Composite Type
composite_type = field.lookup(_tables.composite_types(), columns=str(_config.field_size('work', 'composite_type')))
composite_type = composite_type.setName('Composite Type').setResultsName('composite_type')

# Version Type
version_type = field.lookup(_tables.version_types(), compulsory=True)
version_type = version_type.setName('Version Type').setResultsName('version_type')

# Excerpt Type
excerpt_type = field.lookup(_tables.excerpt_types(), compulsory=True)
excerpt_type = excerpt_type.setName('Excerpt Type').setResultsName('excerpt_type')

# Music Arrangement
music_arrangement = field.lookup(_tables.music_arrangements(),
                                 columns=str(_config.field_size('work', 'music_arrangement')))
music_arrangement = music_arrangement.setName('Music Arrangement').setResultsName('music_arrangement')

# Lyric Adaptation
lyric_adaptation = field.lookup(_tables.lyric_adaptations(), columns=_config.field_size('work', 'lyric_adaptation'))
lyric_adaptation = lyric_adaptation.setName('Lyric Adaptation').setResultsName('lyric_adaptation')

# Work Type
work_type = field.lookup(_tables.work_types(), columns=_config.field_size('work', 'work_type'))
work_type = work_type.setName('Work Type').setResultsName('cwr_work_type')

# USA License Indicator
usa_license = field.lookup(_tables.usa_license_indicators())
usa_license = usa_license.setName('USA License Indicator').setResultsName('usa_license')

# Agreement Type
agreement_type = field.lookup(_tables.agreement_types())
agreement_type = agreement_type.setName('Agreement Type').setResultsName('agreement_type')