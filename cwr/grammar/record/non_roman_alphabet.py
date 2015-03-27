# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import NonRomanAlphabetAgreementPartyDictionaryDecoder, \
    NonRomanAlphabetPublisherNameDictionaryDecoder, NonRomanAlphabetWriterNameDictionaryDecoder, \
    NonRomanAlphabetTitleDictionaryDecoder, NonRomanAlphabetPerformanceDataDictionaryDecoder, \
    NonRomanAlphabetWorkDictionaryDecoder, NonRomanAlphabetOtherWriterDictionaryDecoder


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
    decoder = NonRomanAlphabetAgreementPartyDictionaryDecoder()
    return decoder.decode(parsed)


def _to_npn(parsed):
    """
    Transforms the final parsing result into an NPNRecord instance.

    :param parsed: result of parsing an NPN transaction
    :return: a NPNRecord created from the parsed record
    """
    decoder = NonRomanAlphabetPublisherNameDictionaryDecoder()
    return decoder.decode(parsed)


def _to_nwn(parsed):
    """
    Transforms the final parsing result into an NWNRecord instance.

    :param parsed: result of parsing an NWN transaction
    :return: a NWNRecord created from the parsed record
    """
    decoder = NonRomanAlphabetWriterNameDictionaryDecoder()
    return decoder.decode(parsed)


def _to_nat(parsed):
    """
    Transforms the final parsing result into an NATRecord instance.

    :param parsed: result of parsing an NAT transaction
    :return: a NATRecord created from the parsed record
    """
    decoder = NonRomanAlphabetTitleDictionaryDecoder()
    return decoder.decode(parsed)


def _to_npr(parsed):
    """
    Transforms the final parsing result into an NPRRecord instance.

    :param parsed: result of parsing an NPR transaction
    :return: a NPRRecord created from the parsed record
    """
    decoder = NonRomanAlphabetPerformanceDataDictionaryDecoder()
    return decoder.decode(parsed)


def _to_nra_work(parsed):
    """
    Transforms the final parsing result into an NRARecordWork instance.

    :param parsed: result of parsing an Work NRA transaction
    :return: a NRARecordWork created from the parsed record
    """
    decoder = NonRomanAlphabetWorkDictionaryDecoder()
    return decoder.decode(parsed)


def _to_now(parsed):
    """
    Transforms the final parsing result into an NOWRecord instance.

    :param parsed: result of parsing a NOW transaction
    :return: a NOWRecord created from the parsed record
    """
    decoder = NonRomanAlphabetOtherWriterDictionaryDecoder()
    return decoder.decode(parsed)