# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Message record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

# Interested Party Last Name
ip_last_name = basic.alphanum(_config.field_size('ipa', 'ip_last_name'), compulsory=True)
ip_last_name = ip_last_name.setName('Interested Party Last Name').setResultsName('last_name')

# Interested Party Writer First Name
ip_name = basic.alphanum(_config.field_size('ipa', 'ip_name'))
ip_name = ip_name.setName('Interested Party Writer First Name').setResultsName('writer_name')
