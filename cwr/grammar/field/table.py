# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar.field import basic


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
    original_transaction_type_field = basic.lookup(_tables.transaction_types(),
                                                   columns=_config.field_size('table', 'original_transaction_type'),
                                                   compulsory=compulsory,
                                                   name='Original Transaction Type')
    original_transaction_type_field = original_transaction_type_field.setResultsName(
        'transaction_type')

    return original_transaction_type_field


# Transaction Status
def transaction_status(compulsory=False):
    transaction_status_field = basic.lookup(_tables.transaction_status(),
                                            columns=_config.field_size('table', 'transaction_status'),
                                            compulsory=compulsory,
                                            name='Transaction Status')
    transaction_status_field = transaction_status_field.setResultsName(
        'transaction_status')

    return transaction_status_field


# Prior Royalty Status
def prior_royalty_status(compulsory=False):
    prior_royalty_status_field = basic.lookup(_tables.prior_royalty_status(),
                                              columns=_config.field_size('table', 'prior_royalty_status'),
                                              compulsory=compulsory, name='Prior Royalty Status')
    prior_royalty_status_field = prior_royalty_status_field.setResultsName(
        'prior_royalty_status')

    return prior_royalty_status_field


# Post Term Collection Status
def post_term_collection_status(compulsory=False):
    post_term_collection_status_field = basic.lookup(_tables.post_term_collection_status(),
                                                     columns=_config.field_size('table', 'post_term_collection_status'),
                                                     compulsory=compulsory, name='Post Term Collection Status')
    post_term_collection_status_field = post_term_collection_status_field.setResultsName(
        'post_term_collection_status')

    return post_term_collection_status_field


# Sales/Manufacture Clause
def sm_clause(compulsory=False):
    sm_clause_field = basic.lookup(_tables.sales_manufacture_clause(),
                                   columns=_config.field_size('table', 'sm_clause'),
                                   compulsory=compulsory,
                                   name='Sales/Manufacture Clause')
    sm_clause_field = sm_clause_field.setResultsName('sales_manufacture_clause')

    return sm_clause_field


# Inclusion/Exclusion Indicator
def ie_indicator(compulsory=False):
    ie_indicator_field = basic.lookup(_tables.ie_indicator(), compulsory=compulsory,
                                      columns=_config.field_size('table', 'ie_indicator_field'),
                                      name='Inclusion/Exclusion Indicator')
    ie_indicator_field = ie_indicator_field.setResultsName('ie_indicator')

    return ie_indicator_field


# TIS Numeric Code
def tis_code(compulsory=False):
    tis_code_field = basic.lookup(_tables.tis_codes(),
                                  columns=_config.field_size('table', 'tis_code'),
                                  compulsory=compulsory, name='TIS Numeric Code')
    tis_code_field = tis_code_field.setResultsName('tis_code')
    tis_code_field.setParseAction(lambda c: int(c[0]))

    return tis_code_field


# Agreement Role Code
def agreement_role_code(compulsory=False):
    agreement_role_code_field = basic.lookup(_tables.agreement_roles(),
                                             columns=_config.field_size('table', 'agreement_role_code'),
                                             compulsory=compulsory,
                                             name='Agreement Role Code')
    agreement_role_code_field = agreement_role_code_field.setResultsName(
        'agreement_role_code')

    return agreement_role_code_field


# Language Code
def language(compulsory=False):
    language_field = basic.lookup(_tables.language_codes(),
                                  columns=_config.field_size('table', 'language'), compulsory=compulsory,
                                  name='Language Code')
    language_field = language_field.setResultsName('language')

    return language_field


# Publisher Type
def publisher_type(compulsory=False):
    publisher_type_field = basic.lookup(_tables.publisher_types(),
                                        columns=_config.field_size('table', 'publisher_type'), compulsory=compulsory,
                                        name='Publisher Type')
    publisher_type_field = publisher_type_field.setResultsName('publisher_type')

    return publisher_type_field


# Special Agreements Indicator
def special_agreement(compulsory=False):
    special_agreement_field = basic.lookup(_tables.special_agreement_indicators(),
                                           columns=_config.field_size('table', 'special_agreement'),
                                           compulsory=compulsory,
                                           name='Special Agreements Indicator')
    special_agreement_field = special_agreement_field.setResultsName(
        'special_agreements')

    return special_agreement_field


# Transaction type
def transaction_type(compulsory=False):
    transaction_type_field = basic.lookup(_tables.transaction_types(),
                                          columns=_config.field_size('table', 'transaction_type'),
                                          compulsory=compulsory,
                                          name='Transaction Type')
    transaction_type_field = transaction_type_field.setResultsName('transaction_type')

    return transaction_type_field


# Sender Type
def sender_type(compulsory=False):
    sender_type_field = basic.lookup(_tables.sender_types(),
                                     columns=_config.field_size('table', 'sender_type'),
                                     compulsory=compulsory, name='Sender Type')
    sender_type_field = sender_type_field.setResultsName('sender_type')

    return sender_type_field


# Musical Work Distribution Category
def musical_distribution_category(compulsory=False):
    musical_distribution_category_field = basic.lookup(_tables.musical_work_distribution_categories(),
                                                       columns=_config.field_size('table',
                                                                                  'musical_distribution_category'),
                                                       compulsory=compulsory,
                                                       name='Musical Work Distribution Category')
    musical_distribution_category_field = musical_distribution_category_field.setResultsName(
        'musical_distribution_category')

    return musical_distribution_category_field


# Text Music Relationship
def text_music_relationship(compulsory=False):
    text_music_relationship_field = basic.lookup(_tables.text_music_relationships(),
                                                 columns=_config.field_size('table', 'text_music_relationship'),
                                                 compulsory=compulsory,
                                                 name='Text Music Relationship')
    text_music_relationship_field = text_music_relationship_field.setResultsName(
        'text_music_relationship')

    return text_music_relationship_field


# Composite Type
def composite_type(compulsory=False):
    composite_type_field = basic.lookup(_tables.composite_types(),
                                        columns=_config.field_size('table', 'composite_type'),
                                        compulsory=compulsory, name='Composite Type')
    composite_type_field = composite_type_field.setResultsName('composite_type')

    return composite_type_field


# Version Type
def version_type(compulsory=False):
    version_type_field = basic.lookup(_tables.version_types(),
                                      columns=_config.field_size('table', 'version_type'),
                                      compulsory=compulsory,
                                      name='Version Type')
    version_type_field = version_type_field.setResultsName('version_type')

    return version_type_field


# Excerpt Type
def excerpt_type(compulsory=False):
    excerpt_type_field = basic.lookup(_tables.excerpt_types(),
                                      columns=_config.field_size('table', 'excerpt_type'),
                                      compulsory=compulsory,
                                      name='Excerpt Type')
    excerpt_type_field = excerpt_type_field.setResultsName('excerpt_type')

    return excerpt_type_field


# Music Arrangement
def music_arrangement(compulsory=False):
    music_arrangement_field = basic.lookup(_tables.music_arrangements(),
                                           columns=_config.field_size('table', 'music_arrangement'),
                                           compulsory=compulsory,
                                           name='Music Arrangement')
    music_arrangement_field = music_arrangement_field.setResultsName('music_arrangement')

    return music_arrangement_field


# Lyric Adaptation
def lyric_adaptation(compulsory=False):
    lyric_adaptation_field = basic.lookup(_tables.lyric_adaptations(),
                                          columns=_config.field_size('table', 'lyric_adaptation'),
                                          compulsory=compulsory,
                                          name='Lyric Adaptation')
    lyric_adaptation_field = lyric_adaptation_field.setResultsName('lyric_adaptation')

    return lyric_adaptation_field


# Work Type
def work_type(compulsory=False):
    work_type_field = basic.lookup(_tables.work_types(), columns=_config.field_size('table', 'work_type'),
                                   compulsory=compulsory, name='Work Type')
    work_type_field = work_type_field.setResultsName('cwr_work_type')

    return work_type_field


# USA License Indicator
def usa_license(compulsory=False):
    usa_license_field = basic.lookup(_tables.usa_license_indicators(),
                                     columns=_config.field_size('table', 'usa_license'),
                                     compulsory=compulsory,
                                     name='USA License Indicator')
    usa_license_field = usa_license_field.setResultsName('usa_license')

    return usa_license_field


# Agreement Type
def agreement_type(compulsory=False):
    agreement_type_field = basic.lookup(_tables.agreement_types(),
                                        columns=_config.field_size('table', 'agreement_type'),
                                        compulsory=compulsory, name='Agreement Type')
    agreement_type_field = agreement_type_field.setResultsName('agreement_type')

    return agreement_type_field


def society(compulsory=False):
    """
    Creates the grammar for a society ID.

    These are rights societies, used to identify Performing, Mechanical and Synchronization rights.

    :return: grammar for the society ID field
    """
    society_field = basic.lookup(_tables.society_codes(),
                                 columns=_config.field_size('table', 'society'), compulsory=compulsory)

    society_field.setParseAction(lambda c: None if c[0] is None else int(c[0]))

    society_field.setName('Society ID Field')

    return society_field


# Writer Designation
def writer_designation(compulsory=False):
    writer_designation_field = basic.lookup(_tables.writer_designation_codes(),
                                            columns=_config.field_size('table', 'writer_designation'),
                                            compulsory=compulsory, name='Writer Designation')
    writer_designation_field = writer_designation_field.setResultsName('writer_designation')

    return writer_designation_field


# Title Type
def title_type(compulsory=False):
    title_type_field = basic.lookup(_tables.title_types(),
                                    columns=_config.field_size('table', 'title_type'),
                                    compulsory=compulsory, name='Title Type')
    title_type_field = title_type_field.setResultsName('title_type')

    return title_type_field


# Recording Formats
def recording_formats(compulsory=False):
    recording_format_field = basic.lookup(_tables.recording_formats(),
                                          columns=_config.field_size('table', 'recording_format'),
                                          compulsory=compulsory, name='Recording Format')
    recording_format_field = recording_format_field.setResultsName('recording_format')

    return recording_format_field


# Recording Techniques
def recording_techniques(compulsory=False):
    recording_technique_field = basic.lookup(_tables.recording_techniques(),
                                             columns=_config.field_size('table', 'recording_technique'),
                                             compulsory=compulsory, name='Recording Technique')
    recording_technique_field = recording_technique_field.setResultsName('recording_technique')

    return recording_technique_field


# Media Types
def media_types(compulsory=False):
    media_type_field = basic.lookup(_tables.media_types(),
                                    columns=_config.field_size('table', 'media_type'),
                                    compulsory=compulsory, name='Media Type')
    media_type_field = media_type_field.setResultsName('media_type')

    return media_type_field


# Intended Purposes
def intended_purposes(compulsory=False):
    intended_purpose_field = basic.lookup(_tables.intended_purposes(),
                                          columns=_config.field_size('table', 'intended_purpose'),
                                          compulsory=compulsory, name='Media Type')
    intended_purpose_field = intended_purpose_field.setResultsName('intended_purpose')

    return intended_purpose_field


# Standard Instrumentations
def standard_instrumentations(compulsory=False):
    standard_instrumentations_field = basic.lookup(_tables.standard_instrumentation_types(),
                                                   columns=_config.field_size('table', 'standard_instrumentations'),
                                                   compulsory=compulsory, name='Standard Instrumentation Type')
    standard_instrumentations_field = standard_instrumentations_field.setResultsName('standard_instrumentation')

    return standard_instrumentations_field


# Instruments
def instruments(compulsory=False):
    instruments_field = basic.lookup(_tables.instruments(),
                                     columns=_config.field_size('table', 'instruments'),
                                     compulsory=compulsory, name='Instrument')
    instruments_field = instruments_field.setResultsName('instruments')

    return instruments_field


def char_code(columns, compulsory=False):
    """
    Character set code.

    This accepts one of the character sets allowed on the file.

    :param columns: number of columns for this field
    :param compulsory: indicates if the empty string is disallowed
    :return: a parser for the character set field
    """

    if columns <= 0:
        raise BaseException()

    char_sets = None
    for char_set in _tables.character_sets():
        regex = '[ ]{' + str(15 - len(char_set)) + '}' + char_set
        if char_sets is None:
            char_sets = regex
        else:
            char_sets += '|' + regex

    # Accepted sets
    _character_sets = pp.Regex(char_sets)
    _unicode_1_16b = pp.Regex('U\+0[0-8,A-F]{3}[ ]{' + str(columns - 6) + '}')
    _unicode_2_21b = pp.Regex('U\+0[0-8,A-F]{4}[ ]{' + str(columns - 7) + '}')

    # Basic field
    char_code_field = (_character_sets | _unicode_1_16b | _unicode_2_21b)

    # Parse action
    char_code_field = char_code_field.setParseAction(lambda s: s[0].strip())

    # Name
    char_code_field.setName('Char Code Field (' + str(columns) + ' columns)')

    char_code_field.setName('Character Set Field')

    if not compulsory:
        char_code_field_empty = pp.Regex('[ ]{' + str(columns) + '}')
        char_code_field_empty.setName('Character Set Field')

        char_code_field_empty.leaveWhitespace()

        char_code_field_empty.setParseAction(pp.replaceWith(None))

        char_code_field = char_code_field | char_code_field_empty

        char_code_field.setName('Character Set Field')

    return char_code_field
