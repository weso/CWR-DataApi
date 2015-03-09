# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration
from cwr.grammar.field import basic


"""
CWR Group record fields grammar.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
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

# Group ID
group_id = basic.numeric(_config.field_size('group_header', 'group_id'), compulsory=True)
group_id = group_id.setName('Group ID').setResultsName('group_id')

# Version Number
version_number = pp.Literal(_config.field_value('group_header', 'version_number'))
version_number = version_number.setName('Version Number').setResultsName('version_number')

# Batch Request ID
batch_request_id = basic.numeric(_config.field_size('group_header', 'batch_request_id'))
batch_request_id = batch_request_id.setName('Batch Request ID').setResultsName('batch_request_id')

"""
Unused fields.

These are fields which exist in the standard but are unused and ignored.

They are:
- SD Type
- Currency Indicator
- Total Monetary Value
"""

# SD Type
sd_type = basic.alphanum(_config.field_size('group_header', 'sd_type'))
sd_type = sd_type.setName('SD Type').setResultsName('sd_type')
sd_type.leaveWhitespace()

# Currency Indicator
currency_indicator = pp.Word(pp.alphanums + ' ',
                             exact=_config.field_size('group_trailer', 'currency_indicator'))
currency_indicator = currency_indicator.setName('Currency Indicator').setResultsName('currency_indicator')
currency_indicator.leaveWhitespace()

# Total Monetary Value
total_monetary_value = pp.Word(pp.alphanums + ' ',
                               exact=_config.field_size('group_trailer', 'total_monetary_value'))
total_monetary_value = total_monetary_value.setName('Total Monetary Value').setResultsName('total_monetary_value')
total_monetary_value.leaveWhitespace()
