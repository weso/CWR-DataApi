# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Publisher IP #
publisher_ip_id = special.ip_id()
publisher_ip_id = publisher_ip_id.setName('Publisher IP #').setResultsName('publisher_id')

# Publisher Name
publisher_name = basic.alphanum(_config.field_size('writer_publisher', 'publisher_name'))
publisher_name = publisher_name.setName('Publisher Name').setResultsName('publisher_name')

# Writer IP #
writer_ip_id = special.ip_id()
writer_ip_id = writer_ip_id.setName('Writer IP #').setResultsName('writer_id')
