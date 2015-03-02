# -*- encoding: utf-8 -*-

import pyparsing as pp

from data.accessor import CWRConfiguration, CWRTables
from cwr.grammar import field, field_special, record
from cwr.agreement import NPARecord


"""
CWR Non-Roman Alphabet records grammar.

This is for the following records:
- Non-Roman Alphabet Agreement Party Name (NPA)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_tables = CWRTables()
_config = CWRConfiguration()

"""
General fields.
"""

# Interested Party #
ip_id = field_special.ip_id()

# Language Code
language = pp.oneOf(_tables.language_codes())
language_empty = pp.Regex('[ ]{2}')
language_empty = language_empty.setName('Language Code').setResultsName('language')
language_empty.leaveWhitespace()
language = language.setName('Language Code').setResultsName('language')

language_empty.setParseAction(pp.replaceWith(None))

language = language | language_empty
language = language.setName('Language Code').setResultsName('language')

"""
NPA fields.
"""

# Record Type for the territory in agreement
record_prefix_npa = record.record_prefix(_config.record_type('npa'))

# Interested Party Name
ip_name = field.alphanum(_config.field_size('npa', 'ip_name'), compulsory=True)
ip_name = ip_name.setName('Interested Party Name').setResultsName('ip_name')
ip_name.leaveWhitespace()

# Interested Party Writer First Name
ip_writer_name = field.alphanum(_config.field_size('npa', 'ip_writer_name'), compulsory=True)
ip_writer_name = ip_writer_name.setName('Interested Party Writer First Name').setResultsName('ip_writer_name')
ip_writer_name.leaveWhitespace()

"""
NPA patterns.
"""

npa = field_special.lineStart + record_prefix_npa + ip_id + ip_name + ip_writer_name + language + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

npa.setParseAction(lambda a: _to_npa(a))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_npa(parsed):
    """
    Transforms the final parsing result into an NPARecord instance.

    :param parsed: result of parsing an NPA transaction
    :return: a NPARecord created from the parsed record
    """
    return NPARecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.ip_name, parsed.ip_writer_name, parsed.ip_id, parsed.language)