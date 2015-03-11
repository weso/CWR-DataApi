# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import publisher as field_publisher
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import nra as field_nra
from cwr.nra import NPARecord, NWNRecord, NATRecord, NRARecordWork, NOWRecord, NPRRecord, NPNRecord


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
NRA patterns.
"""

npa = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'npa'),
    compulsory=True) + field_special.ip_id() + field_nra.ip_name + field_nra.ip_writer_name + field_table.language() + field_special.lineEnd

npn = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'npn'), compulsory=True) + field_publisher.publisher_sequence_n + field_special.ip_id(
    compulsory=True) + field_nra.publisher_name + \
      field_table.language() + field_special.lineEnd

nwn = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'nwn'), compulsory=True) + field_special.ip_id() + field_nra.writer_last_name + field_nra.writer_first_name + \
      field_table.language() + field_special.lineEnd

nat = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'nat'),
    compulsory=True) + field_nra.nat_title + field_table.title_type() + field_table.language() + field_special.lineEnd

npr = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'npr'),
    compulsory=True) + field_nra.performing_artist_name + field_nra.performing_artist_first_name + field_special.ipi_name_number() + \
      field_special.ipi_base_number() + field_table.language() + field_nra.performance_language + field_nra.dialect + field_special.lineEnd

nra_work = field_special.lineStart + field_record.record_prefix(
    _config.record_type('nra_work'), compulsory=True) + field_nra.title + field_table.language() + field_special.lineEnd

now = field_special.lineStart + field_record.record_prefix(
    _config.record_type(
        'now'),
    compulsory=True) + field_nra.writer_name + field_nra.writer_first_name_now + field_table.language() + field_nra.writer_position + field_special.lineEnd

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
                     parsed.publisher_sequence_n, parsed.ip_id, parsed.name, parsed.language)


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