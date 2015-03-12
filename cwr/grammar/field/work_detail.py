# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Work detail records fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
ALT fields.
"""

# Alternate Title
alternate_title = basic.alphanum(_config.field_size('alternate_title', 'alternate_title'), extended=True)
alternate_title = alternate_title.setName('Alternate Title').setResultsName(
    'title')

"""
EWT fields.
"""

# Entire Work Title
entire_work_title = basic.alphanum(_config.field_size('entire_work_title', 'entire_work_title'))
entire_work_title = entire_work_title.setName('Entire Work Title').setResultsName(
    'title')

"""
VER fields.
"""

# Original Work Title
original_title = basic.alphanum(_config.field_size('original_work_title', 'original_title'))
original_title = original_title.setName('Original Work Title').setResultsName(
    'title')

"""
PER fields.
"""

# Performing Artist Last Name
performing_artist_last_name = basic.alphanum(_config.field_size('performing_artist', 'performer_last_name'))
performing_artist_last_name = performing_artist_last_name.setName('Performing Artist Last Name').setResultsName(
    'performing_artist_last_name')

# Performing Artist First Name
performing_artist_first_name = basic.alphanum(_config.field_size('performing_artist', 'performer_first_name'))
performing_artist_first_name = performing_artist_first_name.setName('Performing Artist First Name').setResultsName(
    'performing_artist_first_name')

"""
REC fields.
"""

# First Release Date
first_release = basic.date()
first_release = first_release.setName('First Release Date').setResultsName('first_release_date')

# First Release Duration
first_release_duration = basic.time()
first_release_duration = first_release_duration.setName('First Release Duration').setResultsName(
    'first_release_duration')

# First Album Title
first_title = basic.alphanum(_config.field_size('recording_detail', 'first_album_title'))
first_title = first_title.setName('First Album Title').setResultsName('first_album_title')

# First Album Label
first_label = basic.alphanum(_config.field_size('recording_detail', 'first_album_label'))
first_label = first_label.setName('First Album Label').setResultsName('first_album_label')

# First Release Catalog #
first_release_catalog_n = basic.alphanum(_config.field_size('recording_detail', 'first_release_catalog_id'))
first_release_catalog_n = first_release_catalog_n.setName('First Release Catalog #').setResultsName(
    'first_release_catalog_n')

"""
ORN fields.
"""

# Production Title
production_title = basic.alphanum(_config.field_size('work_origin', 'production_title'))
production_title = production_title.setName('Production Title').setResultsName('production_title')

# CD Identifier
cd_identifier = basic.alphanum(_config.field_size('work_origin', 'cd_identifier'))
cd_identifier = cd_identifier.setName('CD Identifier').setResultsName('cd_identifier')

# Cut Number
cut_number = basic.numeric(_config.field_size('work_origin', 'cut_number'))
cut_number = cut_number.setName('Cut Number').setResultsName('cut_number')

# Library
library = basic.alphanum(_config.field_size('work_origin', 'library'))
library = library.setName('Library').setResultsName('library')

# BLTVR
bltvr = basic.alphanum(_config.field_size('work_origin', 'bltvr'))
bltvr = bltvr.setName('BLTVR').setResultsName('bltvr')

# Production #
production_n = basic.alphanum(_config.field_size('work_origin', 'production_n'))
production_n = production_n.setName('Production #').setResultsName('production_n')

# Episode Title
episode_title = basic.alphanum(_config.field_size('work_origin', 'episode_title'))
episode_title = episode_title.setName('Episode Title').setResultsName('episode_title')

# Episode #
episode_n = basic.alphanum(_config.field_size('work_origin', 'episode_n'))
episode_n = episode_n.setName('Episode #').setResultsName('episode_n')

# Year of Production
year_production = basic.numeric(_config.field_size('work_origin', 'production_year'))
year_production = year_production.setName('Year of Production').setResultsName('year_production')

"""
INS fields.
"""

# Number of voices
number_voices = basic.numeric(_config.field_size('instrumentation_summary', 'voices'))
number_voices = number_voices.setName('Number of voices').setResultsName('number_voices')

# Instrumentation Description
instrumentation_description = basic.alphanum(_config.field_size('instrumentation_summary', 'description'))
instrumentation_description = instrumentation_description.setName('Instrumentation Description').setResultsName(
    'instrumentation_description')

"""
IND fields.
"""

# Number of players
number_players = basic.numeric(_config.field_size('instrumentation_detail', 'players'))
number_players = number_players.setName('Number of players').setResultsName('number_players')

"""
COM fields.
"""

# Title
component_title = basic.alphanum(_config.field_size('component', 'title'))
component_title = component_title.setName('Title').setResultsName('title')

# Duration
component_duration = basic.time()
component_duration = component_duration.setName('Duration').setResultsName('duration')

"""
Author fields
"""

# Writer 1 Last Name
writer_1_last_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_1_last_name = writer_1_last_name.setName('Writer 1 Last Name').setResultsName(
    'writer_1_last_name')

# Writer 1 First Name
writer_1_first_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_1_first_name = writer_1_first_name.setName('Writer 1 Last Name').setResultsName(
    'writer_1_first_name')

# Writer 1 IPI Name #
writer_1_ipi_name_n = special.ipi_name_number()
writer_1_ipi_name_n = writer_1_ipi_name_n.setName('Writer 1 IPI Name #').setResultsName('writer_1_ipi_name_n')

# Writer 1 IPI Base #
writer_1_ipi_base_n = special.ipi_base_number()
writer_1_ipi_base_n = writer_1_ipi_base_n.setName('Writer 1 IPI Base #').setResultsName('writer_1_ipi_base_n')

# Writer 2 Last Name
writer_2_last_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_2_last_name = writer_2_last_name.setName('Writer 2 Last Name').setResultsName(
    'writer_2_last_name')

# Writer 2 First Name
writer_2_first_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_2_first_name = writer_2_first_name.setName('Writer 2 Last Name').setResultsName('writer_2_first_name')

# Writer 2 IPI Name #
writer_2_ipi_name_n = special.ipi_name_number()
writer_2_ipi_name_n = writer_2_ipi_name_n.setName('Writer 1 IPI Name #').setResultsName('writer_2_ipi_name_n')

# Writer 2 IPI Base #
writer_2_ipi_base_n = special.ipi_base_number()
writer_2_ipi_base_n = writer_2_ipi_base_n.setName('Writer 1 IPI Base #').setResultsName('writer_2_ipi_base_n')

# Source
source = basic.alphanum(_config.field_size('entire_work_title', 'source'))
source = source.setName('Source').setResultsName('source')

# ISWC
iswc = special.iswc()
iswc = iswc.setResultsName('iswc')