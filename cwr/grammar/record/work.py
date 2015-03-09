# -*- encoding: utf-8 -*-

from data.accessor import CWRTables, CWRConfiguration
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import work as field_work
from cwr import work


"""
CWR Work grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
Work patterns.
"""

work_record = field_special.lineStart + field_record.record_prefix(_config.record_type('work'),
                                                                   compulsory=True) + field_work.work_title + \
              field_table.language() + field_work.work_id + field_work.iswc + \
              field_work.copyright_date + field_work.copyright_number + field_table.musical_distribution_category(
    compulsory=True) + field_work.duration + field_work.recorded + \
              field_table.text_music_relationship(
                  compulsory=True) + field_table.composite_type() + field_table.version_type(
    compulsory=True) + field_table.excerpt_type(compulsory=True) + field_table.music_arrangement() + \
              field_table.lyric_adaptation() + field_work.contact_name + field_work.contact_id + field_table.work_type() + field_work.gr_indicator + field_work.composite_count + \
              field_work.printed_edition_publication_date + field_work.exceptional_clause + field_work.opus_number + field_work.catalogue_number + field_work.priority_flag + \
              field_special.lineEnd

conflict = field_special.lineStart + field_record.record_prefix(_config.record_type('work_conflict'),
                                                                compulsory=True) + field_work.work_title + \
           field_table.language() + field_work.work_id + field_work.iswc + \
           field_work.copyright_date + field_work.copyright_number + field_table.musical_distribution_category(
    compulsory=True) + field_work.duration + field_work.recorded + \
           field_table.text_music_relationship(
               compulsory=True) + field_table.composite_type() + field_table.version_type(
    compulsory=True) + field_table.excerpt_type(compulsory=True) + field_table.music_arrangement() + \
           field_table.lyric_adaptation() + field_work.contact_name + field_work.contact_id + field_table.work_type() + field_work.gr_indicator + field_work.composite_count + \
           field_work.printed_edition_publication_date + field_work.exceptional_clause + field_work.opus_number + field_work.catalogue_number + field_work.priority_flag + \
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
                           parsed.work_id, parsed.title, parsed.version_type, parsed.musical_distribution_category,
                           printed_edition_publication_date=parsed.printed_edition_publication_date,
                           text_music_relationship=parsed.text_music_relationship,
                           language_code=parsed.language,
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