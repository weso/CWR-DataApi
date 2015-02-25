# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.parsing.data.accessor import ParserDataStorage
from cwr.parsing.grammar import record, field, special
from cwr import work

"""
CWR Work grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

"""
Work fields.
"""

# Record Type for the work
record_prefix_agreement = record.record_prefix(data.record_type('work'))

# Work Title
work_title = field.alphanum(data.field_size('work', 'work_title'), compulsory=True)
work_title = work_title.setName('Work Title').setResultsName('title')

# Language Code
language_code = special.language_code()
language_code = language_code.setName('Language Code').setResultsName('language_code')

# Submitter Work Number
work_id = field.alphanum(data.field_size('work', 'work_id'), compulsory=True)
work_id = work_id.setName('Submitter Work Number').setResultsName('work_id')

# ISWC
iswc = field.alphanum(data.field_size('work', 'iswc'))
iswc = iswc.setName('ISWC').setResultsName('iswc')

# Copyright Date
copyright_date = field.date()
copyright_date = copyright_date.setName('Copyright Date').setResultsName('copyright_date')

# Copyright Number
copyright_number = field.alphanum(data.field_size('work', 'copyright_number'))
copyright_number = copyright_number.setName('Copyright Number').setResultsName('copyright_number')

# Musical Work Distribution Category
musical_distribution_category = pp.oneOf(data.musical_work_distribution_categories())
musical_distribution_category = musical_distribution_category.setName(
    'Musical Work Distribution Category').setResultsName('musical_distribution_category')

# Duration
duration = field.time()
duration = duration.setName('Duration').setResultsName('duration')

# Recorded Indicator
recorded = field.flag()
recorded = recorded.setName('Recorded Indicator').setResultsName('recorded_indicator')

# Text Music Relationship
text_music_relationship = pp.oneOf(data.text_music_relationships())
text_music_relationship = text_music_relationship.setName('Text Music Relationship').setResultsName(
    'text_music_relationship')

# Composite Type
composite_type = pp.oneOf(data.composite_types())
composite_type = composite_type.setName('Composite Type').setResultsName('composite_type')

# Version Type
version_type = pp.oneOf(data.version_types())
version_type = version_type.setName('Version Type').setResultsName('version_type')

# Excerpt Type
excerpt_type = pp.oneOf(data.excerpt_types())
excerpt_type = excerpt_type.setName('Excerpt Type').setResultsName('excerpt_type')

# Music Arrangement
music_arrangement = pp.oneOf(data.music_arrangements())
music_arrangement = music_arrangement.setName('Music Arrangement').setResultsName('music_arrangement')

# Lyric Adaptation
lyric_adaptation = pp.oneOf(data.lyric_adaptations())
lyric_adaptation = lyric_adaptation.setName('Lyric Adaptation').setResultsName('lyric_adaptation')

# Contact Name
contact_name = field.alphanum(data.field_size('work', 'contact_name'))
contact_name = contact_name.setName('Contact Name').setResultsName('contact_name')

# Contact ID
contact_id = field.alphanum(data.field_size('work', 'contact_id'))
contact_id = contact_id.setName('Contact ID').setResultsName('contact_id')

# Work Type
work_type = pp.oneOf(data.work_types())
work_type = work_type.setName('Work Type').setResultsName('cwr_work_type')

# Grand Rights Indicator
gr_indicator = field.boolean()
gr_indicator = gr_indicator.setName('Grand Rights Indicator').setResultsName('grand_rights_indicator')

# Composite Component Count
composite_count = field.numeric(data.field_size('work', 'composite_count'))
composite_count = composite_count.setName('Composite Component Count').setResultsName('composite_component_count')

# Date of Publication of Printed Edition
printed_edition_publication_date = field.date()
printed_edition_publication_date = printed_edition_publication_date.setName(
    'Date of Publication of Printed Edition').setResultsName('printed_edition_publication_date')

# Exceptional Clause
exceptional_clause = field.flag()
exceptional_clause = exceptional_clause.setName('Exceptional Clause').setResultsName('exceptional_clause')

# Opus Number
opus_number = field.alphanum(data.field_size('work', 'opus_number'))
opus_number = opus_number.setName('Opus Number').setResultsName('opus_number')

# Catalogue Number
catalogue_number = field.alphanum(data.field_size('work', 'catalogue'))
catalogue_number = catalogue_number.setName('Catalogue Number').setResultsName('catalogue_number')

# Priority Flag
priority_flag = field.flag()
priority_flag = priority_flag.setName('Priority Flag').setResultsName('priority_flag')

"""
Work patterns.
"""

work_record = special.lineStart + record_prefix_agreement + work_title + language_code + work_id + iswc + \
              copyright_date + copyright_number + musical_distribution_category + duration + recorded + \
              text_music_relationship + composite_type + version_type + excerpt_type + music_arrangement + \
              lyric_adaptation + contact_name + contact_id + work_type + gr_indicator + composite_count + \
              printed_edition_publication_date + exceptional_clause + opus_number + catalogue_number + priority_flag + \
              special.lineEnd

"""
Parsing actions for the patterns.
"""

work_record.setParseAction(lambda p: _to_work(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_work(parsed):
    """
    Transforms the final parsing result into a WorkRecord instance.

    :param parsed: result of parsing a Work transaction header
    :return: a WorkRecord created from the parsed record
    """
    print parsed
    return work.WorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                           parsed.work_id, parsed.title, parsed.version_type, parsed.musical_distribution_category,
                           printed_edition_publication_date=parsed.printed_edition_publication_date,
                           text_music_relationship=parsed.text_music_relationship,
                           language_code=parsed.language_code,
                           copyright_number=parsed.copyright_number,
                           copyright_date=parsed.copyright_date,
                           music_arrangement=parsed.music_arrangement,
                           lyric_adaptation=parsed.lyric_adaptation,
                           excerpt_type=parsed.excerpt_type,
                           composite_type=parsed.composite_type,
                           composite_component_count=parsed.composite_component_count,
                           iswc=parsed.iswc,
                           cwr_work_type=parsed.cwr_work_type,
                           duration=parsed.duration,
                           catalogue_number=parsed.catalogue_number,
                           opus_number=parsed.opus_number,
                           contact_id=parsed.contact_id,
                           contact_name=parsed.contact_name,
                           recorded_indicator=parsed.recorded_indicator,
                           priority_flag=parsed.priority_flag,
                           exceptional_clause=parsed.exceptional_clause,
                           grand_rights_indicator=parsed.grand_rights_indicator)