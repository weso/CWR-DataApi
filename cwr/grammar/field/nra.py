# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic
from cwr.grammar.factory.field import LookupFieldFactory


"""
CWR NRA record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()
_lookup_factory = LookupFieldFactory()

"""
NPA fields.
"""

# Interested Party Name
ip_name = basic.alphanum(_config.field_size('nra', 'name'), compulsory=True)
ip_name = ip_name.setName('Interested Party Name').setResultsName('ip_name')
ip_name.leaveWhitespace()

# Interested Party Writer First Name
ip_writer_name = basic.alphanum(_config.field_size('nra', 'name'), compulsory=True)
ip_writer_name = ip_writer_name.setName('Interested Party Writer First Name').setResultsName('ip_writer_name')
ip_writer_name.leaveWhitespace()

"""
NPN fields.
"""

# Publisher Name
publisher_name = basic.alphanum(_config.field_size('npn', 'name'), compulsory=True)
publisher_name = publisher_name.setName('Publisher Name').setResultsName('publisher_name')
publisher_name.leaveWhitespace()

"""
NWN fields.
"""

# Writer Last Name
writer_last_name = basic.alphanum(_config.field_size('nra', 'name'), compulsory=True)
writer_last_name = writer_last_name.setName('Writer Last Name').setResultsName('writer_last_name')
writer_last_name.leaveWhitespace()

# Writer First Name
writer_first_name = basic.alphanum(_config.field_size('nra', 'name'), compulsory=True)
writer_first_name = writer_first_name.setName('Writer First Name').setResultsName('writer_first_name')
writer_first_name.leaveWhitespace()

"""
NAT fields.
"""

# Title
nat_title = basic.alphanum(_config.field_size('nat', 'title'), compulsory=True)
nat_title = nat_title.setName('Title').setResultsName('title')

"""
NPR fields.
"""

# Performing Artist Name
performing_artist_name = basic.alphanum(_config.field_size('npr', 'performing_artist_name'))
performing_artist_name = performing_artist_name.setName('Performing Artist Name').setResultsName(
    'performing_artist_name')

# Performing Artist Name
performing_artist_first_name = basic.alphanum(_config.field_size('npr', 'performing_artist_first_name'))
performing_artist_first_name = performing_artist_first_name.setName('Performing Artist First Name').setResultsName(
    'performing_artist_first_name')

# Dialect
dialect = basic.alphanum(_config.field_size('npr', 'dialect'))
dialect = dialect.setName('Dialect').setResultsName('dialect')

"""
Work NRA fields.
"""

# Title
title = basic.alphanum(_config.field_size('nra_work', 'title'))
title = title.setName('Title').setResultsName('title')

"""
NOW fields.
"""

# Writer Name
writer_name = basic.alphanum(_config.field_size('now', 'name'))
writer_name = writer_name.setName('Writer Name').setResultsName('writer_name')

# Writer Last Name
writer_first_name_now = basic.alphanum(_config.field_size('now', 'last_name'))
writer_first_name_now = writer_first_name_now.setName('Writer Last Name').setResultsName('writer_first_name')

# Writer Position
writer_position = basic.numeric(_config.field_size('now', 'position'))
writer_position = writer_position.setName('Writer Position').setResultsName('position')
