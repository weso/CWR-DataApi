# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr import work
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Work grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = DefaultFieldFactory(_config.load_field_config('table'), CWRTables())
_work_factory = DefaultFieldFactory(_config.load_field_config('work'))

"""
Work patterns.
"""

work_record = field_special.lineStart + \
              field_record.record_prefix(_config.record_type('work'), compulsory=True) + \
              _work_factory.get_field('work_title', compulsory=True) + \
              _lookup_factory.get_field('language_code') + \
              _work_factory.get_field('submitter_work_n', compulsory=True) + \
              _work_factory.get_field('iswc') + \
              _work_factory.get_field('copyright_date') + \
              _work_factory.get_field('copyright_number') + \
              _lookup_factory.get_field('musical_work_distribution_category', compulsory=True) + \
              _work_factory.get_field('duration') + \
              _work_factory.get_field('recorded_indicator') + \
              _lookup_factory.get_field('text_music_relationship', compulsory=True) + \
              _lookup_factory.get_field('composite_type') + \
              _lookup_factory.get_field('version_type', compulsory=True) + \
              _lookup_factory.get_field('excerpt_type') + \
              _lookup_factory.get_field('music_arrangement') + \
              _lookup_factory.get_field('lyric_adaptation') + \
              _work_factory.get_field('contact_name') + \
              _work_factory.get_field('contact_id') + \
              _lookup_factory.get_field('work_type') + \
              _work_factory.get_field('grand_rights_indicator') + \
              _work_factory.get_field('composite_component_count') + \
              _work_factory.get_field('date_publication_printed_edition') + \
              _work_factory.get_field('exceptional_clause') + \
              _work_factory.get_field('opus_number') + \
              _work_factory.get_field('catalogue_number') + \
              _work_factory.get_field('priority_flag') + \
              field_special.lineEnd

conflict = field_special.lineStart + \
           field_record.record_prefix(_config.record_type('work_conflict'), compulsory=True) + \
           _work_factory.get_field('work_title') + \
           _lookup_factory.get_field('language_code') + \
           _work_factory.get_field('submitter_work_n') + \
           _work_factory.get_field('iswc') + \
           _work_factory.get_field('copyright_date') + \
           _work_factory.get_field('copyright_number') + \
           _lookup_factory.get_field('musical_work_distribution_category', compulsory=True) + \
           _work_factory.get_field('duration') + \
           _work_factory.get_field('recorded_indicator') + \
           _lookup_factory.get_field('text_music_relationship', compulsory=True) + \
           _lookup_factory.get_field('composite_type') + \
           _lookup_factory.get_field('version_type', compulsory=True) + \
           _lookup_factory.get_field('excerpt_type', compulsory=True) + \
           _lookup_factory.get_field('music_arrangement') + \
           _lookup_factory.get_field('lyric_adaptation') + \
           _work_factory.get_field('contact_name') + \
           _work_factory.get_field('contact_id') + \
           _lookup_factory.get_field('work_type') + \
           _work_factory.get_field('grand_rights_indicator') + \
           _work_factory.get_field('composite_component_count') + \
           _work_factory.get_field('date_publication_printed_edition') + \
           _work_factory.get_field('exceptional_clause') + \
           _work_factory.get_field('opus_number') + \
           _work_factory.get_field('catalogue_number') + \
           _work_factory.get_field('priority_flag') + \
           field_special.lineEnd

"""
Parsing actions for the patterns.
"""

work_record.setParseAction(lambda p: _to_work(p))
conflict.setParseAction(lambda p: _to_work(p))

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
    return work.WorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                           parsed.submitter_work_n, parsed.title, parsed.version_type,
                           parsed.musical_work_distribution_category,
                           date_publication_printed_edition=parsed.date_publication_printed_edition,
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
                           cwr_work_type=parsed.work_type,
                           duration=parsed.duration,
                           catalogue_number=parsed.catalogue_number,
                           opus_number=parsed.opus_number,
                           contact_id=parsed.contact_id,
                           contact_name=parsed.contact_name,
                           recorded_indicator=parsed.recorded_indicator,
                           priority_flag=parsed.priority_flag,
                           exceptional_clause=parsed.exceptional_clause,
                           grand_rights_indicator=parsed.grand_rights_indicator)