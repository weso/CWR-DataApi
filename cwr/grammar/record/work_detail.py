# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import work as field_work
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import work_detail as field_work_detail
from cwr.work import AlternateTitleRecord, AuthoredWorkRecord, PerformingArtistRecord, RecordingDetailRecord, \
    WorkOriginRecord, InstrumentationSummaryRecord, InstrumentationDetailRecord, ComponentRecord


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
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Patterns.
"""

alternate = field_special.lineStart + field_record.record_prefix(_config.record_type('alternate_title'),
                                                                 compulsory=True) + \
            field_work_detail.alternate_title + field_table.title_type() + field_table.language() + field_special.lineEnd

entire_title = field_special.lineStart + field_record.record_prefix(_config.record_type('entire_work_title'),
                                                                    compulsory=True) + \
               field_work_detail.entire_work_title + field_work_detail.iswc + field_table.language() + field_work_detail.writer_1_last_name + \
               field_work_detail.writer_1_first_name + field_work_detail.source + field_work_detail.writer_1_ipi_name + \
               field_work_detail.writer_1_ipi_base + field_work_detail.writer_2_last_name + \
               field_work_detail.writer_2_first_name + field_work_detail.writer_2_ipi_name + field_work_detail.writer_2_ipi_base + field_work.work_id + field_special.lineEnd

version = field_special.lineStart + field_record.record_prefix(_config.record_type('original_work_title'),
                                                               compulsory=True) + \
          field_work_detail.original_title + field_work_detail.iswc + field_table.language() + field_work_detail.writer_1_last_name + \
          field_work_detail.writer_1_first_name + field_work_detail.source + field_work_detail.writer_1_ipi_name + \
          field_work_detail.writer_1_ipi_base + field_work_detail.writer_2_last_name + \
          field_work_detail.writer_2_first_name + field_work_detail.writer_2_ipi_name + field_work_detail.writer_2_ipi_base + field_work.work_id + field_special.lineEnd

performing = field_special.lineStart + field_record.record_prefix(_config.record_type('performing_artist'),
                                                                  compulsory=True) + \
             field_work_detail.performer_last_name + field_work_detail.performer_first_name + field_special.ipi_name_number() + \
             field_special.ipi_base_number() + field_special.lineEnd

recording = field_special.lineStart + field_record.record_prefix(_config.record_type('recording_detail'),
                                                                 compulsory=True) + field_work_detail.first_release + \
            field_special.blank(_config.field_size('recording_detail', 'constant_1')) + \
            field_work_detail.first_release_duration + field_special.blank(
    _config.field_size('recording_detail', 'constant_2')) + \
            field_work_detail.first_title + field_work_detail.first_label + field_work_detail.first_catalog + field_special.ean_13() + field_special.isrc() + field_table.recording_formats() + \
            field_table.recording_techniques() + field_table.media_types() + field_special.lineEnd

origin = field_special.lineStart + field_record.record_prefix(_config.record_type('work_origin'),
                                                              compulsory=True) + field_table.intended_purposes() + \
         field_work_detail.production_title + field_work_detail.cd_identifier + field_work_detail.cut_number + field_work_detail.library + field_work_detail.bltvr + field_special.visan() + field_work_detail.production_n + \
         field_work_detail.episode_title + field_work_detail.episode_n + field_work_detail.year_production + field_special.avi() + field_special.lineEnd

inst_summary = field_special.lineStart + field_record.record_prefix(
    _config.record_type('instrumentation_summary'), compulsory=True) + field_work_detail.number_voices + \
               field_table.standard_instrumentations() + field_work_detail.instr_description + field_special.lineEnd

inst_detail = field_special.lineStart + field_record.record_prefix(_config.record_type('instrumentation_detail'),
                                                                   compulsory=True) + \
              field_table.instruments() + field_work_detail.players_n + field_special.lineEnd

component = field_special.lineStart + field_record.record_prefix(_config.record_type('component'),
                                                                 compulsory=True) + field_work_detail.component_title + \
            field_work_detail.iswc + field_work.work_id + field_work_detail.component_duration + field_work_detail.writer_1_last_name + field_work_detail.writer_1_first_name + field_work_detail.writer_1_ipi_name + \
            field_work_detail.writer_2_last_name + field_work_detail.writer_2_first_name + field_work_detail.writer_2_ipi_name + field_work_detail.writer_1_ipi_base + \
            field_work_detail.writer_2_ipi_base + field_special.lineEnd

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
                                parsed.title, parsed.title_type, parsed.language)


def _to_entire_title(parsed):
    """
    Transforms the final parsing result into an AuthoredWorkRecord instance.

    :param parsed: result of parsing an Entire Title record
    :return: a AuthoredWorkRecord created from the parsed record
    """
    return AuthoredWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                              parsed.title, parsed.work_id, parsed.first_name_1, parsed.last_name_1,
                              parsed.first_name_2, parsed.last_name_2, parsed.ipi_base_1,
                              parsed.ipi_name_1, parsed.ipi_base_2, parsed.ipi_name_2,
                              parsed.source, parsed.language, parsed.iswc)


def _to_version_title(parsed):
    """
    Transforms the final parsing result into an AuthoredWorkRecord instance.

    :param parsed: result of parsing an Original Work Title for Versions record
    :return: a AuthoredWorkRecord created from the parsed record
    """
    return AuthoredWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                              parsed.title, parsed.work_id, parsed.first_name_1, parsed.last_name_1,
                              parsed.first_name_2, parsed.last_name_2, parsed.ipi_base_1,
                              parsed.ipi_name_1, parsed.ipi_base_2, parsed.ipi_name_2,
                              parsed.source, parsed.language, parsed.iswc)


def _to_performing_artist(parsed):
    """
    Transforms the final parsing result into an PerformingArtistRecord instance.

    :param parsed: result of parsing a Performing Artist record
    :return: a PerformingArtistRecord created from the parsed record
    """
    return PerformingArtistRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                  parsed.last_name, parsed.first_name, parsed.ipi_name, parsed.ipi_base)


def _to_recording_detail(parsed):
    """
    Transforms the final parsing result into an RecordingDetailRecord instance.

    :param parsed: result of parsing a Recording Detail record
    :return: a RecordingDetailRecord created from the parsed record
    """
    return RecordingDetailRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                 parsed.first_release_date, parsed.first_release_duration, parsed.first_album_title,
                                 parsed.first_album_label, parsed.first_release_catalog_id, parsed.ean_13, parsed.isrc,
                                 parsed.recording_format, parsed.recording_technique, parsed.media_type)


def _to_work_origin(parsed):
    """
    Transforms the final parsing result into an WorkOriginRecord instance.

    :param parsed: result of parsing a Work Origin record
    :return: a WorkOriginRecord created from the parsed record
    """
    return WorkOriginRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                            parsed.intended_purpose, parsed.production_title, parsed.cd_identifier, parsed.cut_number,
                            parsed.library, parsed.bltvr, parsed.visan, parsed.production_id, parsed.episode_title,
                            parsed.episode_id, parsed.production_year, parsed.avi)


def _to_instrumentation_summary(parsed):
    """
    Transforms the final parsing result into an InstrumentationSummaryRecord instance.

    :param parsed: result of parsing an Instrumentation Summary record
    :return: a InstrumentationSummaryRecord created from the parsed record
    """
    return InstrumentationSummaryRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                        parsed.voices, parsed.standard_instrumentation, parsed.description)


def _to_instrumentation_detail(parsed):
    """
    Transforms the final parsing result into an InstrumentationDetailRecord instance.

    :param parsed: result of parsing an Instrumentation Detail record
    :return: a InstrumentationDetailRecord created from the parsed record
    """
    return InstrumentationDetailRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                       parsed.instruments, parsed.players)


def _to_component(parsed):
    """
    Transforms the final parsing result into an ComponentRecord instance.

    :param parsed: result of parsing an Component Detail record
    :return: a ComponentRecord created from the parsed record
    """
    return ComponentRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n, parsed.title,
                           parsed.last_name_1, parsed.work_id, parsed.first_name_1, parsed.first_name_2,
                           parsed.last_name_2, parsed.ipi_base_1, parsed.ipi_name_1, parsed.ipi_base_2,
                           parsed.ipi_name_2, parsed.iswc, parsed.duration)