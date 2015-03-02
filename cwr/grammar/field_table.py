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
def original_transaction_type(compulsory=False):
    original_transaction_type_field = field.lookup(_tables.record_types(), compulsory=compulsory)
    original_transaction_type_field = original_transaction_type_field.setName(
        'Original Transaction Type').setResultsName(
        'transaction_type')

    return original_transaction_type_field


# Transaction Status
def transaction_status(compulsory=False):
    transaction_status_field = field.lookup(_tables.transaction_status(), compulsory=compulsory)
    transaction_status_field = transaction_status_field.setName('Transaction Status').setResultsName(
        'transaction_status')

    return transaction_status_field


# Prior Royalty Status
def prior_royalty_status(compulsory=False):
    prior_royalty_status_field = field.lookup(_config.field_value('agreement', 'prior_royalty_status'),
                                              compulsory=compulsory)
    prior_royalty_status_field = prior_royalty_status_field.setName('Prior Royalty Status').setResultsName(
        'prior_royalty_status')

    return prior_royalty_status_field


# Post Term Collection Status
def post_term_collection_status(compulsory=False):
    post_term_collection_status_field = field.lookup(_config.field_value('agreement', 'post_term_collection_status'),
                                                     compulsory=compulsory)
    post_term_collection_status_field = post_term_collection_status_field.setName(
        'Post Term Collection Status').setResultsName(
        'post_term_collection_status')

    return post_term_collection_status_field


# Sales/Manufacture Clause
def sm_clause(compulsory=False):
    sm_clause_field = field.lookup(_config.field_value('agreement', 'sales_manufacture_clause'), compulsory=compulsory)
    sm_clause_field = sm_clause_field.setName('Sales/Manufacture Clause').setResultsName('sales_manufacture_clause')

    return sm_clause_field


# Inclusion/Exclusion Indicator
def ie_indicator(compulsory=False):
    ie_indicator_field = field.lookup(_config.field_value('agreement_territory', 'ie_indicator'), compulsory=compulsory)
    ie_indicator_field = ie_indicator_field.setName('Inclusion/Exclusion Indicator').setResultsName('ie_indicator')

    return ie_indicator_field


# TIS Numeric Code
def tis_code(compulsory=False):
    tis_code_field = field.lookup(_tables.tis_codes(), compulsory=compulsory)
    tis_code_field = tis_code_field.setName('TIS Numeric Code').setResultsName('tis_code')
    tis_code_field.setParseAction(lambda c: int(c[0]))

    return tis_code_field


# Agreement Role Code
def agreement_role_code(compulsory=False):
    agreement_role_code_field = field.lookup(_tables.agreement_roles(), compulsory=compulsory)
    agreement_role_code_field = agreement_role_code_field.setName('Agreement Role Code').setResultsName(
        'agreement_role_code')

    return agreement_role_code_field


# Language Code
def language(compulsory=False):
    language_field = field.lookup(_tables.language_codes(), columns=2, compulsory=compulsory)
    language_field = language_field.setName('Language Code').setResultsName('language')

    return language_field


# Publisher Type
def publisher_type(compulsory=False):
    publisher_type_field = field.lookup(_tables.publisher_types(), columns=2, compulsory=compulsory)
    publisher_type_field = publisher_type_field.setName('Publisher Type').setResultsName('publisher_type')

    return publisher_type_field


# Special Agreements Indicator
def special_agreement(compulsory=False):
    special_agreement_field = field.lookup(_tables.special_agreement_indicators(), compulsory=compulsory)
    special_agreement_field = special_agreement_field.setName('Special Agreements Indicator').setResultsName(
        'special_agreements')

    return special_agreement_field


# Transaction type
def transaction_type(compulsory=False):
    transaction_type_field = field.lookup(_tables.transaction_types(), compulsory=compulsory)
    transaction_type_field = transaction_type_field.setName('Transaction Type').setResultsName('transaction_type')

    return transaction_type_field


# Sender Type
def sender_type(compulsory=False):
    sender_type_field = field.lookup(_tables.sender_types(), compulsory=compulsory)
    sender_type_field = sender_type_field.setName('Sender Type').setResultsName('sender_type')

    return sender_type_field


# Musical Work Distribution Category
def musical_distribution_category(compulsory=False):
    musical_distribution_category_field = field.lookup(_tables.musical_work_distribution_categories(),
                                                       compulsory=compulsory)
    musical_distribution_category_field = musical_distribution_category_field.setName(
        'Musical Work Distribution Category').setResultsName('musical_distribution_category')

    return musical_distribution_category_field


# Text Music Relationship
def text_music_relationship(compulsory=False):
    text_music_relationship_field = field.lookup(_tables.text_music_relationships(), compulsory=compulsory)
    text_music_relationship_field = text_music_relationship_field.setName('Text Music Relationship').setResultsName(
        'text_music_relationship')

    return text_music_relationship_field


# Composite Type
def composite_type(compulsory=False):
    composite_type_field = field.lookup(_tables.composite_types(),
                                        columns=str(_config.field_size('work', 'composite_type')),
                                        compulsory=compulsory)
    composite_type_field = composite_type_field.setName('Composite Type').setResultsName('composite_type')

    return composite_type_field


# Version Type
def version_type(compulsory=False):
    version_type_field = field.lookup(_tables.version_types(), compulsory=compulsory)
    version_type_field = version_type_field.setName('Version Type').setResultsName('version_type')

    return version_type_field


# Excerpt Type
def excerpt_type(compulsory=False):
    excerpt_type_field = field.lookup(_tables.excerpt_types(), compulsory=compulsory)
    excerpt_type_field = excerpt_type_field.setName('Excerpt Type').setResultsName('excerpt_type')

    return excerpt_type_field


# Music Arrangement
def music_arrangement(compulsory=False):
    music_arrangement_field = field.lookup(_tables.music_arrangements(),
                                           columns=str(_config.field_size('work', 'music_arrangement')),
                                           compulsory=compulsory)
    music_arrangement_field = music_arrangement_field.setName('Music Arrangement').setResultsName('music_arrangement')

    return music_arrangement_field


# Lyric Adaptation
def lyric_adaptation(compulsory=False):
    lyric_adaptation_field = field.lookup(_tables.lyric_adaptations(),
                                          columns=_config.field_size('work', 'lyric_adaptation'), compulsory=compulsory)
    lyric_adaptation_field = lyric_adaptation_field.setName('Lyric Adaptation').setResultsName('lyric_adaptation')

    return lyric_adaptation_field


# Work Type
def work_type(compulsory=False):
    work_type_field = field.lookup(_tables.work_types(), columns=_config.field_size('work', 'work_type'),
                                   compulsory=compulsory)
    work_type_field = work_type_field.setName('Work Type').setResultsName('cwr_work_type')

    return work_type_field


# USA License Indicator
def usa_license(compulsory=False):
    usa_license_field = field.lookup(_tables.usa_license_indicators(), compulsory=compulsory)
    usa_license_field = usa_license_field.setName('USA License Indicator').setResultsName('usa_license')

    return usa_license_field


# Agreement Type
def agreement_type(compulsory=False):
    agreement_type_field = field.lookup(_tables.agreement_types(), compulsory=compulsory)
    agreement_type_field = agreement_type_field.setName('Agreement Type').setResultsName('agreement_type')

    return agreement_type_field