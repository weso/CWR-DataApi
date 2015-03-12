# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Work record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Work Title
work_title = basic.alphanum(_config.field_size('work', 'work_title'), compulsory=True)
work_title = work_title.setName('Work Title').setResultsName('title')

# Submitter Work Number
submitter_work_n = basic.alphanum(_config.field_size('work', 'work_id'), compulsory=True)
submitter_work_n = submitter_work_n.setName('Submitter Work Number').setResultsName('submitter_work_n')

# ISWC
iswc = special.iswc()
iswc = iswc.setResultsName('iswc')

# Copyright Date
copyright_date = basic.date()
copyright_date = copyright_date.setName('Copyright Date').setResultsName('copyright_date')

# Copyright Number
copyright_number = basic.alphanum(_config.field_size('work', 'copyright_number'))
copyright_number = copyright_number.setName('Copyright Number').setResultsName('copyright_number')

# Duration
duration = basic.time()
duration = duration.setName('Duration').setResultsName('duration')

# Recorded Indicator
recorded = basic.flag(compulsory=True)
recorded = recorded.setName('Recorded Indicator').setResultsName('recorded_indicator')

# Contact Name
contact_name = basic.alphanum(_config.field_size('work', 'contact_name'))
contact_name = contact_name.setName('Contact Name').setResultsName('contact_name')

# Contact ID
contact_id = basic.alphanum(_config.field_size('work', 'contact_id'))
contact_id = contact_id.setName('Contact ID').setResultsName('contact_id')

# Grand Rights Indicator
gr_indicator = basic.boolean()
gr_indicator = gr_indicator.setName('Grand Rights Indicator').setResultsName('grand_rights_indicator')

# Composite Component Count
composite_count = basic.numeric(_config.field_size('work', 'composite_count'))
composite_count = composite_count.setName('Composite Component Count').setResultsName('composite_component_count')

# Date of Publication of Printed Edition
date_publication_printed_edition = basic.date()
date_publication_printed_edition = date_publication_printed_edition.setName(
    'Date of Publication of Printed Edition').setResultsName('date_publication_printed_edition')

# Exceptional Clause
exceptional_clause = basic.flag()
exceptional_clause = exceptional_clause.setName('Exceptional Clause').setResultsName('exceptional_clause')

# Opus Number
opus_number = basic.alphanum(_config.field_size('work', 'opus_number'))
opus_number = opus_number.setName('Opus Number').setResultsName('opus_number')

# Catalogue Number
catalogue_number = basic.alphanum(_config.field_size('work', 'catalogue'))
catalogue_number = catalogue_number.setName('Catalogue Number').setResultsName('catalogue_number')

# Priority Flag
priority_flag = basic.flag()
priority_flag = priority_flag.setName('Priority Flag').setResultsName('priority_flag')
