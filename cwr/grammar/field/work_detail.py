# -*- encoding: utf-8 -*-

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
performer_last_name = basic.alphanum(_config.field_size('performing_artist', 'performer_last_name'))
performer_last_name = performer_last_name.setName('Performing Artist Last Name').setResultsName('last_name')

# Performing Artist First Name
performer_first_name = basic.alphanum(_config.field_size('performing_artist', 'performer_first_name'))
performer_first_name = performer_first_name.setName('Performing Artist First Name').setResultsName('first_name')

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
first_catalog = basic.alphanum(_config.field_size('recording_detail', 'first_release_catalog_id'))
first_catalog = first_catalog.setName('First Release Catalog #').setResultsName('first_release_catalog_id')

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
production_n = production_n.setName('Production #').setResultsName('production_id')

# Episode Title
episode_title = basic.alphanum(_config.field_size('work_origin', 'episode_title'))
episode_title = episode_title.setName('Episode Title').setResultsName('episode_title')

# Episode #
episode_n = basic.alphanum(_config.field_size('work_origin', 'episode_n'))
episode_n = episode_n.setName('Episode #').setResultsName('episode_id')

# Year of Production
year_production = basic.numeric(_config.field_size('work_origin', 'production_year'))
year_production = year_production.setName('Year of Production').setResultsName('production_year')

"""
INS fields.
"""

# Number of voices
number_voices = basic.numeric(_config.field_size('instrumentation_summary', 'voices'))
number_voices = number_voices.setName('Number of voices').setResultsName('voices')

# Instrumentation Description
instr_description = basic.alphanum(_config.field_size('instrumentation_summary', 'description'))
instr_description = instr_description.setName('Instrumentation Description').setResultsName('description')

"""
IND fields.
"""

# Number of players
players_n = basic.numeric(_config.field_size('instrumentation_detail', 'players'))
players_n = players_n.setName('Number of players').setResultsName('players')

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
    'last_name_1')

# Writer 1 First Name
writer_1_first_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_1_first_name = writer_1_first_name.setName('Writer 1 Last Name').setResultsName(
    'first_name_1')

# Writer 1 IPI Name #
writer_1_ipi_name = special.ipi_name_number()
writer_1_ipi_name = writer_1_ipi_name.setName('Writer 1 IPI Name #').setResultsName('ipi_name_1')

# Writer 1 IPI Base #
writer_1_ipi_base = special.ipi_base_number()
writer_1_ipi_base = writer_1_ipi_base.setName('Writer 1 IPI Base #').setResultsName('ipi_base_1')

# Writer 2 Last Name
writer_2_last_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_last_name'))
writer_2_last_name = writer_2_last_name.setName('Writer 2 Last Name').setResultsName(
    'last_name_2')

# Writer 2 First Name
writer_2_first_name = basic.alphanum(_config.field_size('entire_work_title', 'writer_first_name'))
writer_2_first_name = writer_2_first_name.setName('Writer 2 Last Name').setResultsName('first_name_2')

# Writer 2 IPI Name #
writer_2_ipi_name = special.ipi_name_number()
writer_2_ipi_name = writer_2_ipi_name.setName('Writer 1 IPI Name #').setResultsName('ipi_name_2')

# Writer 2 IPI Base #
writer_2_ipi_base = special.ipi_base_number()
writer_2_ipi_base = writer_2_ipi_base.setName('Writer 1 IPI Base #').setResultsName('ipi_base_2')

# Source
source = basic.alphanum(_config.field_size('entire_work_title', 'source'))
source = source.setName('Source').setResultsName('source')

# ISWC
iswc = special.iswc()
iswc = iswc.setResultsName('iswc')