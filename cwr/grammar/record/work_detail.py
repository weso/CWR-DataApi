# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import work_detail as field_work_detail
from cwr.work import AlternateTitleRecord, AuthoredWorkRecord, PerformingArtistRecord, RecordingDetailRecord, \
    WorkOriginRecord, InstrumentationSummaryRecord, InstrumentationDetailRecord, ComponentRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables


"""
CWR Work detail grammar.

This is for the following records:
- Alternate Title (ALT)
- Entire Work Title for Excerpts (EWT)
- Original Work Title for Versions (VER)
- Performing Artist (PER)
- Recording Detail (REC)
- Work Origin (ORN)
- Instrumentation Summary (INS)
- Instrumentation Detail (IND)
- Component (COM)
- Additional Related Information (ARI)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = DefaultFieldFactory(_config.load_field_config('table'), CWRTables())
_work_factory = DefaultFieldFactory(_config.load_field_config('work'))
_work_detail_factory = DefaultFieldFactory(_config.load_field_config('work_detail'))

"""
Patterns.
"""

alternate = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('alternate_title'), compulsory=True) + \
            field_work_detail.alternate_title + \
            _lookup_factory.get_field('title_type') + \
            _lookup_factory.get_field('language_code') + \
            field_special.lineEnd

entire_title = field_special.lineStart + \
               field_record.record_prefix(_config.record_type('entire_work_title'), compulsory=True) + \
               _work_detail_factory.get_field('entire_work_title') + \
               field_work_detail.iswc + \
               _lookup_factory.get_field('language_code') + \
               _work_detail_factory.get_field('writer_1_last_name') + \
               _work_detail_factory.get_field('writer_1_first_name') + \
               field_work_detail.source + \
               field_work_detail.writer_1_ipi_name_n + \
               field_work_detail.writer_1_ipi_base_n + \
               _work_detail_factory.get_field('writer_2_last_name') + \
               _work_detail_factory.get_field('writer_2_first_name') + \
               field_work_detail.writer_2_ipi_name_n +\
               field_work_detail.writer_2_ipi_base_n + \
               _work_factory.get_field('submitter_work_n') + \
               field_special.lineEnd

version = field_special.lineStart + \
          field_record.record_prefix(_config.record_type('original_work_title'), compulsory=True) + \
          _work_detail_factory.get_field('original_title') + \
          field_work_detail.iswc + \
          _lookup_factory.get_field('language_code') + \
          _work_detail_factory.get_field('writer_1_last_name') + \
          _work_detail_factory.get_field('writer_1_first_name') + \
          field_work_detail.source + \
          field_work_detail.writer_1_ipi_name_n + \
          field_work_detail.writer_1_ipi_base_n + \
          _work_detail_factory.get_field('writer_2_last_name') + \
          _work_detail_factory.get_field('writer_2_first_name') + \
          field_work_detail.writer_2_ipi_name_n + \
          field_work_detail.writer_2_ipi_base_n + \
          _work_factory.get_field('submitter_work_n') + \
          field_special.lineEnd

performing = field_special.lineStart + \
             field_record.record_prefix(_config.record_type('performing_artist'), compulsory=True) + \
             _work_detail_factory.get_field('performing_artist_last_name') + \
             _work_detail_factory.get_field('performing_artist_first_name') + \
             field_special.ipi_name_number() + \
             field_special.ipi_base_number() + \
             field_special.lineEnd

recording = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('recording_detail'), compulsory=True) + \
            _work_detail_factory.get_field('first_release_date') + \
            field_special.blank(_config.field_size('recording_detail', 'constant_1')) + \
            _work_detail_factory.get_field('first_release_duration') + \
            field_special.blank(_config.field_size('recording_detail', 'constant_2')) + \
            _work_detail_factory.get_field('first_album_title') + \
            _work_detail_factory.get_field('first_album_label') + \
            _work_detail_factory.get_field('first_release_catalog_n') + \
            field_special.ean_13() + field_special.isrc() + \
            _lookup_factory.get_field('recording_format') + \
            _lookup_factory.get_field('recording_technique') + \
            _lookup_factory.get_field('media_type') + \
            field_special.lineEnd

origin = field_special.lineStart + \
         field_record.record_prefix(_config.record_type('work_origin'), compulsory=True) + \
         _lookup_factory.get_field('intended_purpose') + \
         _work_detail_factory.get_field('production_title') + \
         _work_detail_factory.get_field('cd_identifier') + \
         _work_detail_factory.get_field('cut_number') + \
         _work_detail_factory.get_field('library') + \
         _work_detail_factory.get_field('bltvr') + \
         field_special.visan() + \
         _work_detail_factory.get_field('production_n') + \
         _work_detail_factory.get_field('episode_title') + \
         _work_detail_factory.get_field('episode_n') + \
         _work_detail_factory.get_field('year_production') + \
         field_special.audio_visual_key() + \
         field_special.lineEnd

inst_summary = field_special.lineStart + \
               field_record.record_prefix(_config.record_type('instrumentation_summary'), compulsory=True) + \
               field_work_detail.number_voices + \
               _lookup_factory.get_field('standard_instrumentation_type') + \
               field_work_detail.instrumentation_description + \
               field_special.lineEnd

inst_detail = field_special.lineStart + \
              field_record.record_prefix(_config.record_type('instrumentation_detail'), compulsory=True) + \
              _lookup_factory.get_field('instrument') + \
              _work_detail_factory.get_field('number_players') + \
              field_special.lineEnd

component = field_special.lineStart + \
            field_record.record_prefix(_config.record_type('component'), compulsory=True) + \
            _work_detail_factory.get_field('component_title') + \
            field_work_detail.iswc + \
            _work_factory.get_field('submitter_work_n') + \
            _work_detail_factory.get_field('component_duration') + \
            _work_detail_factory.get_field('writer_1_last_name') + \
            _work_detail_factory.get_field('writer_1_first_name') + \
            field_work_detail.writer_1_ipi_name_n + \
            _work_detail_factory.get_field('writer_2_last_name') + \
            _work_detail_factory.get_field('writer_2_first_name') + \
            field_work_detail.writer_2_ipi_name_n + \
            field_work_detail.writer_1_ipi_base_n + \
            field_work_detail.writer_2_ipi_base_n + \
            field_special.lineEnd

"""
Parsing actions for the patterns.
"""

alternate.setParseAction(lambda p: _to_alternate_title(p))

entire_title.setParseAction(lambda p: _to_entire_title(p))

version.setParseAction(lambda p: _to_version_title(p))

performing.setParseAction(lambda p: _to_performing_artist(p))

recording.setParseAction(lambda p: _to_recording_detail(p))

origin.setParseAction(lambda p: _to_work_origin(p))

inst_summary.setParseAction(lambda p: _to_instrumentation_summary(p))

inst_detail.setParseAction(lambda p: _to_instrumentation_detail(p))

component.setParseAction(lambda p: _to_component(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_alternate_title(parsed):
    """
    Transforms the final parsing result into an AlternateTitleRecord instance.

    :param parsed: result of parsing an Alternate Title record
    :return: a AlternateTitleRecord created from the parsed record
    """
    return AlternateTitleRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                parsed.title, parsed.title_type, parsed.language_code)


def _to_entire_title(parsed):
    """
    Transforms the final parsing result into an AuthoredWorkRecord instance.

    :param parsed: result of parsing an Entire Title record
    :return: a AuthoredWorkRecord created from the parsed record
    """
    return AuthoredWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                              parsed.title, parsed.submitter_work_n, parsed.writer_1_first_name,
                              parsed.writer_1_last_name,
                              parsed.writer_2_first_name, parsed.writer_2_last_name, parsed.writer_1_ipi_base_n,
                              parsed.writer_1_ipi_name_n, parsed.writer_2_ipi_base_n, parsed.writer_2_ipi_name_n,
                              parsed.source, parsed.language_code, parsed.iswc)


def _to_version_title(parsed):
    """
    Transforms the final parsing result into an AuthoredWorkRecord instance.

    :param parsed: result of parsing an Original Work Title for Versions record
    :return: a AuthoredWorkRecord created from the parsed record
    """
    return AuthoredWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                              parsed.title, parsed.submitter_work_n, parsed.writer_1_first_name,
                              parsed.writer_1_last_name,
                              parsed.writer_2_first_name, parsed.writer_2_last_name, parsed.writer_1_ipi_base_n,
                              parsed.writer_1_ipi_name_n, parsed.writer_2_ipi_base_n, parsed.writer_2_ipi_name_n,
                              parsed.source, parsed.language_code, parsed.iswc)


def _to_performing_artist(parsed):
    """
    Transforms the final parsing result into an PerformingArtistRecord instance.

    :param parsed: result of parsing a Performing Artist record
    :return: a PerformingArtistRecord created from the parsed record
    """
    return PerformingArtistRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                  parsed.performing_artist_last_name, parsed.performing_artist_first_name,
                                  parsed.ipi_name_n, parsed.ipi_base_n)


def _to_recording_detail(parsed):
    """
    Transforms the final parsing result into an RecordingDetailRecord instance.

    :param parsed: result of parsing a Recording Detail record
    :return: a RecordingDetailRecord created from the parsed record
    """
    return RecordingDetailRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                 parsed.first_release_date, parsed.first_release_duration, parsed.first_album_title,
                                 parsed.first_album_label, parsed.first_release_catalog_n, parsed.ean_13, parsed.isrc,
                                 parsed.recording_format, parsed.recording_technique, parsed.media_type)


def _to_work_origin(parsed):
    """
    Transforms the final parsing result into an WorkOriginRecord instance.

    :param parsed: result of parsing a Work Origin record
    :return: a WorkOriginRecord created from the parsed record
    """
    return WorkOriginRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                            parsed.intended_purpose, parsed.production_title, parsed.cd_identifier, parsed.cut_number,
                            parsed.library, parsed.bltvr, parsed.visan, parsed.production_n, parsed.episode_title,
                            parsed.episode_n, parsed.year_production, parsed.audio_visual_key)


def _to_instrumentation_summary(parsed):
    """
    Transforms the final parsing result into an InstrumentationSummaryRecord instance.

    :param parsed: result of parsing an Instrumentation Summary record
    :return: a InstrumentationSummaryRecord created from the parsed record
    """
    return InstrumentationSummaryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                        parsed.number_voices, parsed.standard_instrumentation_type,
                                        parsed.instrumentation_description)


def _to_instrumentation_detail(parsed):
    """
    Transforms the final parsing result into an InstrumentationDetailRecord instance.

    :param parsed: result of parsing an Instrumentation Detail record
    :return: a InstrumentationDetailRecord created from the parsed record
    """
    return InstrumentationDetailRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                       parsed.instrument, parsed.number_players)


def _to_component(parsed):
    """
    Transforms the final parsing result into an ComponentRecord instance.

    :param parsed: result of parsing an Component Detail record
    :return: a ComponentRecord created from the parsed record
    """
    return ComponentRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n, parsed.title,
                           parsed.writer_1_last_name, parsed.submitter_work_n, parsed.writer_1_first_name,
                           parsed.writer_2_first_name,
                           parsed.writer_2_last_name, parsed.writer_1_ipi_base_n, parsed.writer_1_ipi_name_n,
                           parsed.writer_2_ipi_base_n,
                           parsed.writer_2_ipi_name_n, parsed.iswc, parsed.duration)