# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.record import publisher
from cwr.grammar.field import table, special, record, basic
from cwr.agreement import NPARecord
from cwr.interested_party import NPNRecord, NWNRecord
from cwr.work import NATRecord, NPRRecord, NRARecordWork, NOWRecord


"""
CWR Non-Roman Alphabet records grammar.

This is for the following records:
- Non-Roman Alphabet Agreement Party Name (NPA)
- Non-Roman Alphabet Publisher Name (NPN)
- Non-Roman Alphabet Writer Name (NWN)
- Non-Roman Alphabet Title (NAT)
- Performance Data in non-roman alphabet (NPR)
- Non-Roman Alphabet Entire Work Title for Excerpts (NET)
- Non-Roman Alphabet Title for Components (NCT)
- Non-Roman Alphabet Original Title for Version (NVT)
- Non-Roman Alphabet Other Writer Name (NOW)
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
publisher_name = publisher_name.setName('Publisher Name').setResultsName('name')
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
performing_artist_name = performing_artist_name.setName('Performing Artist Name').setResultsName('name')

# Performing Artist Name
performing_artist_first_name = basic.alphanum(_config.field_size('npr', 'performing_artist_first_name'))
performing_artist_first_name = performing_artist_first_name.setName('Performing Artist First Name').setResultsName(
    'first_name')

# Performance Language
performance_language = table.language()
performance_language = performance_language.setName('Performance Language').setResultsName('performance_language')

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
writer_name = writer_name.setName('Writer Name').setResultsName('name')

# Writer Last Name
writer_first_name_now = basic.alphanum(_config.field_size('now', 'last_name'))
writer_first_name_now = writer_first_name_now.setName('Writer Last Name').setResultsName('first_name')

# Writer Position
writer_position = basic.numeric(_config.field_size('now', 'position'))
writer_position = writer_position.setName('Writer Position').setResultsName('position')

"""
NRA patterns.
"""

npa = special.lineStart + record.record_prefix(
    _config.record_type(
        'npa'), compulsory=True) + special.ip_id() + ip_name + ip_writer_name + table.language() + special.lineEnd

npn = special.lineStart + record.record_prefix(
    _config.record_type(
        'npn'), compulsory=True) + publisher.sequence_n + special.ip_id(compulsory=True) + publisher_name + \
      table.language() + special.lineEnd

nwn = special.lineStart + record.record_prefix(
    _config.record_type(
        'nwn'), compulsory=True) + special.ip_id() + writer_last_name + writer_first_name + \
      table.language() + special.lineEnd

nat = special.lineStart + record.record_prefix(
    _config.record_type(
        'nat'), compulsory=True) + nat_title + table.title_type() + table.language() + special.lineEnd

npr = special.lineStart + record.record_prefix(
    _config.record_type(
        'npr'), compulsory=True) + performing_artist_name + performing_artist_first_name + special.ipi_name_number() + \
      special.ipi_base_number() + table.language() + performance_language + dialect + special.lineEnd

nra_work = special.lineStart + record.record_prefix(
    _config.record_type('nra_work'), compulsory=True) + title + table.language() + special.lineEnd

now = special.lineStart + record.record_prefix(
    _config.record_type(
        'now'),
    compulsory=True) + writer_name + writer_first_name_now + table.language() + writer_position + special.lineEnd

"""
Parsing actions for the patterns.
"""

npa.setParseAction(lambda a: _to_npa(a))

npn.setParseAction(lambda a: _to_npn(a))

nwn.setParseAction(lambda a: _to_nwn(a))

nat.setParseAction(lambda a: _to_nat(a))

npr.setParseAction(lambda a: _to_npr(a))

nra_work.setParseAction(lambda a: _to_nra_work(a))

now.setParseAction(lambda a: _to_now(a))

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


def _to_nwn(parsed):
    """
    Transforms the final parsing result into an NWNRecord instance.

    :param parsed: result of parsing an NWN transaction
    :return: a NWNRecord created from the parsed record
    """
    return NWNRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.writer_first_name, parsed.writer_last_name, parsed.ip_id, parsed.language)


def _to_nat(parsed):
    """
    Transforms the final parsing result into an NATRecord instance.

    :param parsed: result of parsing an NAT transaction
    :return: a NATRecord created from the parsed record
    """
    return NATRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.title, parsed.title_type, parsed.language)


def _to_npr(parsed):
    """
    Transforms the final parsing result into an NPRRecord instance.

    :param parsed: result of parsing an NPR transaction
    :return: a NPRRecord created from the parsed record
    """
    return NPRRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.first_name, parsed.name, parsed.ipi_name, parsed.ipi_base,
                     parsed.language, parsed.performance_language, parsed.dialect)


def _to_nra_work(parsed):
    """
    Transforms the final parsing result into an NRARecordWork instance.

    :param parsed: result of parsing an Work NRA transaction
    :return: a NRARecordWork created from the parsed record
    """
    return NRARecordWork(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                         parsed.title, parsed.language)


def _to_now(parsed):
    """
    Transforms the final parsing result into an NOWRecord instance.

    :param parsed: result of parsing a NOW transaction
    :return: a NOWRecord created from the parsed record
    """
    return NOWRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                     parsed.first_name, parsed.name, parsed.position, parsed.language)