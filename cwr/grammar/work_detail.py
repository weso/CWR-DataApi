# -*- encoding: utf-8 -*-

from data.accessor import CWRTables, CWRConfiguration
from cwr.grammar import field, field_special, record, field_table, work
from cwr.work import AlternateTitleRecord, AuthoredWorkRecord, PerformingArtistRecord, RecordingDetailRecord


"""
CWR Work detail grammar.

This is for the following records:
- Alternate Title (ALT)
- Entire Work Title for Excerpts (EWT)
- Original Work Title for Versions (VER)
- Performing Artist (PER)
- Recording Detail (REC)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
ALT fields.
"""

# Alternate Title
alternate_title = field.alphanum(_config.field_size('alternate_title', 'alternate_title'))
alternate_title = alternate_title.setName('Alternate Title').setResultsName(
    'title')

"""
EWT fields.
"""

# Entire Work Title
entire_work_title = field.alphanum(_config.field_size('entire_work_title', 'entire_work_title'))
entire_work_title = entire_work_title.setName('Entire Work Title').setResultsName(
    'title')

"""
VER fields.
"""

# Original Work Title
original_title = field.alphanum(_config.field_size('original_work_title', 'original_title'))
original_title = original_title.setName('Original Work Title').setResultsName(
    'title')

"""
PER fields.
"""

# Performing Artist Last Name
performer_last_name = field.alphanum(_config.field_size('performing_artist', 'performer_last_name'))
performer_last_name = performer_last_name.setName('Performing Artist Last Name').setResultsName('last_name')

# Performing Artist First Name
performer_first_name = field.alphanum(_config.field_size('performing_artist', 'performer_first_name'))
performer_first_name = performer_first_name.setName('Performing Artist First Name').setResultsName('first_name')

"""
REC fields.
"""

# First Release Date
first_release = field.date()
first_release = first_release.setName('First Release Date').setResultsName('first_release_date')

# First Release Duration
first_release_duration = field.time()
first_release_duration = first_release_duration.setName('First Release Duration').setResultsName(
    'first_release_duration')

# First Album Title
first_title = field.alphanum(_config.field_size('recording_detail', 'first_album_title'))
first_title = first_title.setName('First Album Title').setResultsName('first_album_title')

# First Album Label
first_label = field.alphanum(_config.field_size('recording_detail', 'first_album_label'))
first_label = first_label.setName('First Album Label').setResultsName('first_album_label')

# First Release Catalog #
first_catalog = field.alphanum(_config.field_size('recording_detail', 'first_release_catalog_id'))
first_catalog = first_catalog.setName('First Release Catalog #').setResultsName('first_release_catalog_id')

"""
Author fields
"""

# Writer 1 Last Name
writer_1_last_name = field.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_1_last_name = writer_1_last_name.setName('Writer 1 Last Name').setResultsName(
    'last_name_1')

# Writer 1 First Name
writer_1_first_name = field.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_1_first_name = writer_1_first_name.setName('Writer 1 Last Name').setResultsName(
    'first_name_1')

# Writer 1 IPI Name #
writer_1_ipi_name = field_special.ipi_name_number()
writer_1_ipi_name = writer_1_ipi_name.setName('Writer 1 IPI Name #').setResultsName('ipi_name_1')

# Writer 1 IPI Base #
writer_1_ipi_base = field_special.ipi_base_number()
writer_1_ipi_base = writer_1_ipi_base.setName('Writer 1 IPI Base #').setResultsName('ipi_base_1')

# Writer 2 Last Name
writer_2_last_name = field.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_2_last_name = writer_2_last_name.setName('Writer 2 Last Name').setResultsName(
    'last_name_2')

# Writer 2 First Name
writer_2_first_name = field.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_2_first_name = writer_2_first_name.setName('Writer 2 Last Name').setResultsName('first_name_2')

# Writer 2 IPI Name #
writer_2_ipi_name = field_special.ipi_name_number()
writer_2_ipi_name = writer_2_ipi_name.setName('Writer 1 IPI Name #').setResultsName('ipi_name_2')

# Writer 2 IPI Base #
writer_2_ipi_base = field_special.ipi_base_number()
writer_2_ipi_base = writer_2_ipi_base.setName('Writer 1 IPI Base #').setResultsName('ipi_base_2')

# Source
source = field.alphanum(_config.field_size('entire_work_title', 'source'))
source = source.setName('Source').setResultsName('source')

# ISWC
iswc = field_special.iswc()
iswc = iswc.setResultsName('iswc')

"""
Patterns.
"""

alternate = field_special.lineStart + record.record_prefix(_config.record_type('alternate_title')) + \
            alternate_title + field_table.title_type() + field_table.language() + field_special.lineEnd

entire_title = field_special.lineStart + record.record_prefix(_config.record_type('entire_work_title')) + \
               entire_work_title + iswc + field_table.language() + writer_1_last_name + \
               writer_1_first_name + source + writer_1_ipi_name + \
               writer_1_ipi_base + writer_2_last_name + \
               writer_2_first_name + writer_2_ipi_name + writer_2_ipi_base + work.work_id + field_special.lineEnd

version = field_special.lineStart + record.record_prefix(_config.record_type('original_work_title')) + \
          original_title + iswc + field_table.language() + writer_1_last_name + \
          writer_1_first_name + source + writer_1_ipi_name + \
          writer_1_ipi_base + writer_2_last_name + \
          writer_2_first_name + writer_2_ipi_name + writer_2_ipi_base + work.work_id + field_special.lineEnd

performing = field_special.lineStart + record.record_prefix(_config.record_type('performing_artist')) + \
             performer_last_name + performer_first_name + field_special.ipi_name_number() + \
             field_special.ipi_base_number() + field_special.lineEnd

recording = field_special.lineStart + record.record_prefix(_config.record_type('recording_detail')) + first_release + \
            field_special.blank(_config.field_size('recording_detail', 'constant_1')) + \
            first_release_duration + field_special.blank(_config.field_size('recording_detail', 'constant_2')) + \
            first_title + first_label + first_catalog + field_special.ean_13() + field_special.isrc() + field_table.recording_formats() + \
            field_table.recording_techniques() + field_table.media_types() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

alternate.setParseAction(lambda p: _to_alternate_title(p))

entire_title.setParseAction(lambda p: _to_entire_title(p))

version.setParseAction(lambda p: _to_version_title(p))

performing.setParseAction(lambda p: _to_performing_artist(p))

recording.setParseAction(lambda p: _to_recording_detail(p))

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