# -*- coding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration


"""
CWR Group record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Group fields.

These fields are:
- Record Type. One for the header and another for the trailer, both a pre-defined string.
- Group ID. Numeric.
- Version Number. Must be a predefined string.
- Batch Request ID. Numeric.
"""

# Version Number
version_number = pp.Literal(_config.field_value('group_header', 'version_number'))
version_number = version_number.setName('Version Number').setResultsName('version_number')
