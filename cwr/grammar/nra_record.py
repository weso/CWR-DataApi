# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar import field, field_special, record, field_table, publisher
from cwr.agreement import NPARecord
from cwr.interested_party import NPNRecord


"""
CWR Non-Roman Alphabet records grammar.

This is for the following records:
- Non-Roman Alphabet Agreement Party Name (NPA)
- Non-Roman Alphabet Publisher Name (NPN)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
General fields.
"""

"""
NPA fields.
"""

# Interested Party Name
ip_name = field.alphanum(_config.field_size('npa', 'ip_name'), compulsory=True)
ip_name = ip_name.setName('Interested Party Name').setResultsName('ip_name')
ip_name.leaveWhitespace()

# Interested Party Writer First Name
ip_writer_name = field.alphanum(_config.field_size('npa', 'ip_writer_name'), compulsory=True)
ip_writer_name = ip_writer_name.setName('Interested Party Writer First Name').setResultsName('ip_writer_name')
ip_writer_name.leaveWhitespace()

"""
NPN fields.
"""

# Publisher Name
publisher_name = field.alphanum(_config.field_size('npn', 'name'), compulsory=True)
publisher_name = publisher_name.setName('Publisher Name').setResultsName('name')
publisher_name.leaveWhitespace()

"""
NRA patterns.
"""

npa = field_special.lineStart + record.record_prefix(
    _config.record_type(
        'npa')) + field_special.ip_id() + ip_name + ip_writer_name + field_table.language() + field_special.lineEnd

npn = field_special.lineStart + record.record_prefix(
    _config.record_type(
        'npn')) + publisher.sequence_n + field_special.ip_id(compulsory=True) + publisher_name + \
      field_table.language() + field_special.lineEnd

"""
Parsing actions for the patterns.
"""

npa.setParseAction(lambda a: _to_npa(a))

npn.setParseAction(lambda a: _to_npn(a))

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


def _to_npn(parsed):
    """
    Transforms the final parsing result into an NPNRecord instance.

    :param parsed: result of parsing an NPN transaction
    :return: a NPNRecord created from the parsed record
    """
    return NPNRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.sequence_n, parsed.ip_id, parsed.name, parsed.language)