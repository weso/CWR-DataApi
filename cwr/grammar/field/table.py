# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar.field import basic


"""
Grammar rules for concrete CWR Table/List Lookup fields.

These fields all apply the same kind of constraint: all the values not contained in a defined collection are rejected.

The only exception is when the field is set as optional. Then an empty string composed of whitespaces is allowed.

Additionally, the usual constraints of the Alphanumeric field (non lowercase ASCII) apply.

All the values are read from the lists contained in the library, through the CWRTables class.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

"""
Configuration classes.
"""

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Fields.
"""


def original_transaction_type(name=None, compulsory=False):
    """
    Original Transaction Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Original Transaction Type field rules
    """
    if name is None:
        name = 'Original Transaction Type'

    original_transaction_type_field = basic.lookup(_tables.transaction_types(),
                                                   columns=_config.field_size('table', 'original_transaction_type'),
                                                   compulsory=compulsory,
                                                   name=name)
    original_transaction_type_field = original_transaction_type_field.setResultsName(
        'transaction_type')

    return original_transaction_type_field


def transaction_status(name=None, compulsory=False):
    """
    Transaction Status field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Transaction Status field rules
    """
    if name is None:
        name = 'Transaction Status'

    transaction_status_field = basic.lookup(_tables.transaction_status(),
                                            columns=_config.field_size('table', 'transaction_status'),
                                            compulsory=compulsory,
                                            name='Transaction Status')
    transaction_status_field = transaction_status_field.setResultsName(
        'transaction_status')

    return transaction_status_field


def prior_royalty_status(name=None, compulsory=False):
    """
    Prior Royalty Status field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Prior Royalty Status field rules
    """
    if name is None:
        name = 'Prior Royalty Status'

    prior_royalty_status_field = basic.lookup(_tables.prior_royalty_status(),
                                              columns=_config.field_size('table', 'prior_royalty_status'),
                                              compulsory=compulsory, name=name)
    prior_royalty_status_field = prior_royalty_status_field.setResultsName(
        'prior_royalty_status')

    return prior_royalty_status_field


def post_term_collection_status(name=None, compulsory=False):
    """
    Post Term Collection Status field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Post Term Collection Status field rules
    """
    if name is None:
        name = 'Post Term Collection Status'

    post_term_collection_status_field = basic.lookup(_tables.post_term_collection_status(),
                                                     columns=_config.field_size('table', 'post_term_collection_status'),
                                                     compulsory=compulsory, name=name)
    post_term_collection_status_field = post_term_collection_status_field.setResultsName(
        'post_term_collection_status')

    return post_term_collection_status_field


def sm_clause(name=None, compulsory=False):
    """
    Sales/Manufacture Clause field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Sales/Manufacture Clause field rules
    """
    if name is None:
        name = 'Sales/Manufacture Clause'

    sm_clause_field = basic.lookup(_tables.sales_manufacture_clause(),
                                   columns=_config.field_size('table', 'sm_clause'),
                                   compulsory=compulsory,
                                   name=name)
    sm_clause_field = sm_clause_field.setResultsName('sales_manufacture_clause')

    return sm_clause_field


def ie_indicator(name=None, compulsory=False):
    """
    Inclusion/Exclusion Indicator field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Inclusion/Exclusion Indicator field rules
    """
    if name is None:
        name = 'Inclusion/Exclusion Indicator'

    ie_indicator_field = basic.lookup(_tables.ie_indicator(), compulsory=compulsory,
                                      columns=_config.field_size('table', 'ie_indicator_field'),
                                      name='Inclusion/Exclusion Indicator')
    ie_indicator_field = ie_indicator_field.setResultsName('ie_indicator')

    return ie_indicator_field


def tis_code(name=None, compulsory=False):
    """
    TIS Numeric Code field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the TIS Numeric Code field rules
    """
    if name is None:
        name = 'TIS Numeric Code'

    tis_code_field = basic.lookup(_tables.tis_codes(),
                                  columns=_config.field_size('table', 'tis_code'),
                                  compulsory=compulsory, name=name)
    tis_code_field = tis_code_field.setResultsName('tis_code')
    tis_code_field.setParseAction(lambda c: int(c[0]))

    return tis_code_field


def agreement_role_code(name=None, compulsory=False):
    """
    Agreement Role Code field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Agreement Role Code field rules
    """
    if name is None:
        name = 'Agreement Role Code'

    agreement_role_code_field = basic.lookup(_tables.agreement_roles(),
                                             columns=_config.field_size('table', 'agreement_role_code'),
                                             compulsory=compulsory,
                                             name=name)
    agreement_role_code_field = agreement_role_code_field.setResultsName(
        'agreement_role_code')

    return agreement_role_code_field


def language(name=None, compulsory=False):
    """
    Language Code field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Language Code field rules
    """
    if name is None:
        name = 'Language Code'

    language_field = basic.lookup(_tables.language_codes(),
                                  columns=_config.field_size('table', 'language'), compulsory=compulsory,
                                  name=name)
    language_field = language_field.setResultsName('language')

    return language_field


def publisher_type(name=None, compulsory=False):
    """
    Publisher Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Publisher Type field rules
    """
    if name is None:
        name = 'Publisher Type'

    publisher_type_field = basic.lookup(_tables.publisher_types(),
                                        columns=_config.field_size('table', 'publisher_type'), compulsory=compulsory,
                                        name=name)
    publisher_type_field = publisher_type_field.setResultsName('publisher_type')

    return publisher_type_field


def special_agreement(name=None, compulsory=False):
    """
    Special Agreements Indicator field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Special Agreements Indicator field rules
    """
    if name is None:
        name = 'Special Agreements Indicator'

    special_agreement_field = basic.lookup(_tables.special_agreement_indicators(),
                                           columns=_config.field_size('table', 'special_agreement'),
                                           compulsory=compulsory,
                                           name=name)
    special_agreement_field = special_agreement_field.setResultsName(
        'special_agreements')

    return special_agreement_field


def transaction_type(name=None, compulsory=False):
    """
    Transaction Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Transaction Type field rules
    """
    if name is None:
        name = 'Transaction Type'

    transaction_type_field = basic.lookup(_tables.transaction_types(),
                                          columns=_config.field_size('table', 'transaction_type'),
                                          compulsory=compulsory,
                                          name=name)
    transaction_type_field = transaction_type_field.setResultsName('transaction_type')

    return transaction_type_field


def sender_type(name=None, compulsory=False):
    """
    Sender Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Sender Type field rules
    """
    if name is None:
        name = 'Sender Type'

    sender_type_field = basic.lookup(_tables.sender_types(),
                                     columns=_config.field_size('table', 'sender_type'),
                                     compulsory=compulsory, name=name)
    sender_type_field = sender_type_field.setResultsName('sender_type')

    return sender_type_field


def musical_distribution_category(name=None, compulsory=False):
    """
    Musical Work Distribution Category field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Musical Work Distribution Category field rules
    """
    if name is None:
        name = 'Musical Work Distribution Category'

    musical_distribution_category_field = basic.lookup(_tables.musical_work_distribution_categories(),
                                                       columns=_config.field_size('table',
                                                                                  'musical_distribution_category'),
                                                       compulsory=compulsory,
                                                       name=name)
    musical_distribution_category_field = musical_distribution_category_field.setResultsName(
        'musical_distribution_category')

    return musical_distribution_category_field


def text_music_relationship(name=None, compulsory=False):
    """
    Text Music Relationship field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Text Music Relationship field rules
    """
    if name is None:
        name = 'Text Music Relationship'

    text_music_relationship_field = basic.lookup(_tables.text_music_relationships(),
                                                 columns=_config.field_size('table', 'text_music_relationship'),
                                                 compulsory=compulsory,
                                                 name=name)
    text_music_relationship_field = text_music_relationship_field.setResultsName(
        'text_music_relationship')

    return text_music_relationship_field


def composite_type(name=None, compulsory=False):
    """
    Composite Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Composite Type field rules
    """
    if name is None:
        name = 'Composite Type'

    composite_type_field = basic.lookup(_tables.composite_types(),
                                        columns=_config.field_size('table', 'composite_type'),
                                        compulsory=compulsory, name=name)
    composite_type_field = composite_type_field.setResultsName('composite_type')

    return composite_type_field


def version_type(name=None, compulsory=False):
    """
    Version Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Version Type field rules
    """
    if name is None:
        name = 'Version Type'

    version_type_field = basic.lookup(_tables.version_types(),
                                      columns=_config.field_size('table', 'version_type'),
                                      compulsory=compulsory,
                                      name=name)
    version_type_field = version_type_field.setResultsName('version_type')

    return version_type_field


def excerpt_type(name=None, compulsory=False):
    """
    Excerpt Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Excerpt Type field rules
    """
    if name is None:
        name = 'Excerpt Type'

    excerpt_type_field = basic.lookup(_tables.excerpt_types(),
                                      columns=_config.field_size('table', 'excerpt_type'),
                                      compulsory=compulsory,
                                      name=name)
    excerpt_type_field = excerpt_type_field.setResultsName('excerpt_type')

    return excerpt_type_field


def music_arrangement(name=None, compulsory=False):
    """
    Music Arrangement field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Music Arrangement field rules
    """
    if name is None:
        name = 'Music Arrangement'

    music_arrangement_field = basic.lookup(_tables.music_arrangements(),
                                           columns=_config.field_size('table', 'music_arrangement'),
                                           compulsory=compulsory,
                                           name=name)
    music_arrangement_field = music_arrangement_field.setResultsName('music_arrangement')

    return music_arrangement_field


def lyric_adaptation(name=None, compulsory=False):
    """
    Lyric Adaptation field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Lyric Adaptation field rules
    """
    if name is None:
        name = 'Lyric Adaptation'

    lyric_adaptation_field = basic.lookup(_tables.lyric_adaptations(),
                                          columns=_config.field_size('table', 'lyric_adaptation'),
                                          compulsory=compulsory,
                                          name=name)
    lyric_adaptation_field = lyric_adaptation_field.setResultsName('lyric_adaptation')

    return lyric_adaptation_field


def work_type(name=None, compulsory=False):
    """
    Work Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Work Type field rules
    """
    if name is None:
        name = 'Work Type'

    work_type_field = basic.lookup(_tables.work_types(), columns=_config.field_size('table', 'work_type'),
                                   compulsory=compulsory, name=name)
    work_type_field = work_type_field.setResultsName('cwr_work_type')

    return work_type_field


def usa_license(name=None, compulsory=False):
    """
    USA License Indicator field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the USA License Indicator field rules
    """
    if name is None:
        name = 'USA License Indicator'

    usa_license_field = basic.lookup(_tables.usa_license_indicators(),
                                     columns=_config.field_size('table', 'usa_license'),
                                     compulsory=compulsory,
                                     name=name)
    usa_license_field = usa_license_field.setResultsName('usa_license')

    return usa_license_field


def agreement_type(name=None, compulsory=False):
    """
    Agreement Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Agreement Type field rules
    """
    if name is None:
        name = 'Agreement Type'

    agreement_type_field = basic.lookup(_tables.agreement_types(),
                                        columns=_config.field_size('table', 'agreement_type'),
                                        compulsory=compulsory, name=name)
    agreement_type_field = agreement_type_field.setResultsName('agreement_type')

    return agreement_type_field


def society(name=None, compulsory=False):
    """
    Society ID field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Society ID field rules
    """
    if name is None:
        name = 'Society ID Field'

    codes = _tables.society_codes()
    for code in codes:
        if len(code) > 1 and code[0] == '0':
            codes.append(code[1:])
            if len(code) > 2 and code[1] == '0':
                codes.append(code[2:])

    society_field = basic.lookup(_tables.society_codes(),
                                 columns=_config.field_size('table', 'society'), compulsory=compulsory,
                                 name=name)

    society_field.setParseAction(lambda c: None if c[0] is None else int(c[0]))

    society_field = society_field.setResultsName('society')

    return society_field


def writer_designation(name=None, compulsory=False):
    """
    Writer Designation field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Writer Designation field rules
    """
    if name is None:
        name = 'Writer Designation'

    writer_designation_field = basic.lookup(_tables.writer_designation_codes(),
                                            columns=_config.field_size('table', 'writer_designation'),
                                            compulsory=compulsory, name=name)
    writer_designation_field = writer_designation_field.setResultsName('writer_designation')

    return writer_designation_field


def title_type(name=None, compulsory=False):
    """
    Title Type field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Title Type field rules
    """
    if name is None:
        name = 'Title Type'

    title_type_field = basic.lookup(_tables.title_types(),
                                    columns=_config.field_size('table', 'title_type'),
                                    compulsory=compulsory, name=name)
    title_type_field = title_type_field.setResultsName('title_type')

    return title_type_field


def recording_formats(name=None, compulsory=False):
    """
    Recording Formats field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Recording Formats field rules
    """
    if name is None:
        name = 'Recording Format'

    recording_format_field = basic.lookup(_tables.recording_formats(),
                                          columns=_config.field_size('table', 'recording_format'),
                                          compulsory=compulsory, name=name)
    recording_format_field = recording_format_field.setResultsName('recording_format')

    return recording_format_field


def recording_techniques(name=None, compulsory=False):
    """
    Recording Techniques field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Recording Techniques field rules
    """
    if name is None:
        name = 'Recording Technique'

    recording_technique_field = basic.lookup(_tables.recording_techniques(),
                                             columns=_config.field_size('table', 'recording_technique'),
                                             compulsory=compulsory, name=name)
    recording_technique_field = recording_technique_field.setResultsName('recording_technique')

    return recording_technique_field


def media_types(name=None, compulsory=False):
    """
    Media Types field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Media Types field rules
    """
    if name is None:
        name = 'Media Type'

    media_type_field = basic.lookup(_tables.media_types(),
                                    columns=_config.field_size('table', 'media_type'),
                                    compulsory=compulsory, name=name)
    media_type_field = media_type_field.setResultsName('media_type')

    return media_type_field


def intended_purposes(name=None, compulsory=False):
    """
    Intended Purposes field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Intended Purposes field rules
    """
    if name is None:
        name = 'Intended Purpose'

    intended_purpose_field = basic.lookup(_tables.intended_purposes(),
                                          columns=_config.field_size('table', 'intended_purpose'),
                                          compulsory=compulsory, name='Intended Purpose')
    intended_purpose_field = intended_purpose_field.setResultsName('intended_purpose')

    return intended_purpose_field


def standard_instrumentations(name=None, compulsory=False):
    """
    Standard Instrumentations field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Standard Instrumentations field rules
    """
    if name is None:
        name = 'Standard Instrumentation Type'

    standard_instrumentations_field = basic.lookup(_tables.standard_instrumentation_types(),
                                                   columns=_config.field_size('table', 'standard_instrumentations'),
                                                   compulsory=compulsory, name=name)
    standard_instrumentations_field = standard_instrumentations_field.setResultsName('standard_instrumentation')

    return standard_instrumentations_field


def instruments(name=None, compulsory=False):
    """
    Instruments field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Instruments field rules
    """
    if name is None:
        name = 'Instrument'

    instruments_field = basic.lookup(_tables.instruments(),
                                     columns=_config.field_size('table', 'instruments'),
                                     compulsory=compulsory, name='Instrument')
    instruments_field = instruments_field.setResultsName('instruments')

    return instruments_field


def message_types(name=None, compulsory=False):
    """
    Message Types field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Message Types field rules
    """
    if name is None:
        name = 'Message Type'

    message_type_field = basic.lookup(_tables.message_types(),
                                      columns=_config.field_size('table', 'message_type'),
                                      compulsory=compulsory, name=name)
    message_type_field = message_type_field.setResultsName('message_type')

    return message_type_field


def message_levels(name=None, compulsory=False):
    """
    Message Levels field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Message Levels field rules
    """
    if name is None:
        name = 'Message Level'

    message_level_field = basic.lookup(_tables.message_levels(),
                                       columns=_config.field_size('table', 'message_level'),
                                       compulsory=compulsory, name=name)
    message_level_field = message_level_field.setResultsName('message_level')

    return message_level_field


def record_types(name=None, compulsory=False):
    """
    Record Types field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Record Types field rules
    """
    if name is None:
        name = 'Record Type'

    record_type_field = basic.lookup(_tables.record_types(),
                                     columns=_config.field_size('table', 'record_type'),
                                     compulsory=compulsory, name=name)
    record_type_field = record_type_field.setResultsName('record_type')

    return record_type_field


def types_of_right(name=None, compulsory=False):
    """
    Types of Right field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Types of Right field rules
    """
    if name is None:
        name = 'Type of Right'

    types_of_right_field = basic.lookup(_tables.type_of_rights(),
                                        columns=_config.field_size('table', 'type_of_right'),
                                        compulsory=compulsory, name=name)
    types_of_right_field = types_of_right_field.setResultsName('type_of_right')

    return types_of_right_field


def subject_codes(name=None, compulsory=False):
    """
    Subject Codes field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Subject Codes field rules
    """
    if name is None:
        name = 'Subject Code'

    subject_codes_field = basic.lookup(_tables.subject_codes(),
                                       columns=_config.field_size('table', 'subject_code'),
                                       compulsory=compulsory, name=name)
    subject_codes_field = subject_codes_field.setResultsName('subject_code')

    return subject_codes_field


def char_code(columns, name=None, compulsory=False):
    """
    Character set code field.

    :param name: name for the field
    :param compulsory: indicates if the empty string is disallowed
    :return: an instance of the Character set code field rules
    """
    if name is None:
        name = 'Char Code Field (' + str(columns) + ' columns)'

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
    char_code_field.setName(name)

    if not compulsory:
        char_code_field_empty = pp.Regex('[ ]{' + str(columns) + '}')
        char_code_field_empty.setName(name)

        char_code_field_empty.leaveWhitespace()

        char_code_field_empty.setParseAction(pp.replaceWith(None))

        char_code_field = char_code_field | char_code_field_empty

        char_code_field.setName(name)

    return char_code_field
