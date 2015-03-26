# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.non_roman_alphabet import NonRomanAlphabetAgreementPartyRecord, NonRomanAlphabetWriterNameRecord, \
    NonRomanAlphabetTitleRecord, NonRomanAlphabetWorkRecord, NonRomanAlphabetOtherWriterRecord, \
    NonRomanAlphabetPerformanceDataRecord, NonRomanAlphabetPublisherNameRecord
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


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
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))

_factory_field = DefaultFieldFactory(_data, CWRTables())

_prefixer = PrefixBuilder(_config.record_types())
_factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

"""
NRA patterns.
"""

npa = _factory_record.get_transaction_record('npa')

npn = _factory_record.get_transaction_record('npn')

nwn = _factory_record.get_transaction_record('nwn')

nat = _factory_record.get_transaction_record('nat')

npr = _factory_record.get_transaction_record('npr')

nra_work = _factory_record.get_transaction_record('nra_work')

now = _factory_record.get_transaction_record('now')

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
    return NonRomanAlphabetAgreementPartyRecord(parsed.record_type, parsed.transaction_sequence_n,
                                                parsed.record_sequence_n,
                                                parsed.ip_name, parsed.ip_writer_name, parsed.ip_n,
                                                parsed.language_code)


def _to_npn(parsed):
    """
    Transforms the final parsing result into an NPNRecord instance.

    :param parsed: result of parsing an NPN transaction
    :return: a NPNRecord created from the parsed record
    """
    return NonRomanAlphabetPublisherNameRecord(parsed.record_type, parsed.transaction_sequence_n,
                                               parsed.record_sequence_n,
                                               parsed.publisher_sequence_n, parsed.ip_n, parsed.publisher_name,
                                               parsed.language_code)


def _to_nwn(parsed):
    """
    Transforms the final parsing result into an NWNRecord instance.

    :param parsed: result of parsing an NWN transaction
    :return: a NWNRecord created from the parsed record
    """
    return NonRomanAlphabetWriterNameRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                            parsed.writer_first_name, parsed.writer_last_name, parsed.ip_n,
                                            parsed.language_code)


def _to_nat(parsed):
    """
    Transforms the final parsing result into an NATRecord instance.

    :param parsed: result of parsing an NAT transaction
    :return: a NATRecord created from the parsed record
    """
    return NonRomanAlphabetTitleRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                       parsed.title, parsed.title_type, parsed.language_code)


def _to_npr(parsed):
    """
    Transforms the final parsing result into an NPRRecord instance.

    :param parsed: result of parsing an NPR transaction
    :return: a NPRRecord created from the parsed record
    """
    return NonRomanAlphabetPerformanceDataRecord(parsed.record_type, parsed.transaction_sequence_n,
                                                 parsed.record_sequence_n,
                                                 parsed.performing_artist_first_name, parsed.performing_artist_name,
                                                 parsed.ipi_name_n,
                                                 parsed.ipi_base_n,
                                                 parsed.language_code, parsed.performance_language, parsed.dialect)


def _to_nra_work(parsed):
    """
    Transforms the final parsing result into an NRARecordWork instance.

    :param parsed: result of parsing an Work NRA transaction
    :return: a NRARecordWork created from the parsed record
    """
    return NonRomanAlphabetWorkRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n,
                                      parsed.title, parsed.language_code)


def _to_now(parsed):
    """
    Transforms the final parsing result into an NOWRecord instance.

    :param parsed: result of parsing a NOW transaction
    :return: a NOWRecord created from the parsed record
    """
    return NonRomanAlphabetOtherWriterRecord(parsed.record_type, parsed.transaction_sequence_n,
                                             parsed.record_sequence_n,
                                             parsed.writer_first_name, parsed.writer_name, parsed.position,
                                             parsed.language_code)