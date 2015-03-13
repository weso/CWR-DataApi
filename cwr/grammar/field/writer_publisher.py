# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import special, basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Publisher IP #
publisher_ip_number = special.ip_n()
publisher_ip_number = publisher_ip_number.setName('Publisher IP #').setResultsName('publisher_ip_number')

# Publisher Name
publisher_name = basic.alphanum(_config.field_size('writer_publisher', 'publisher_name'))
publisher_name = publisher_name.setName('Publisher Name').setResultsName('publisher_name')

# Writer IP #
writer_ip_n = special.ip_n()
writer_ip_n = writer_ip_n.setName('Writer IP #').setResultsName('writer_ip_n')
