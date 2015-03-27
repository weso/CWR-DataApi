# -*- coding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.interested_party import Writer
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory
from cwr.parser.dictionary import WriterRecordDictionaryDecoder


"""
CWR Writer records grammar.

This is for the following records:
- Writer Controlled By Submitter (SWR)
- Other Writer (OWR)
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
Patterns.
"""

writer = _factory_record.get_transaction_record('writer')

"""
Parsing actions for the patterns.
"""

writer.setParseAction(lambda p: _to_writerrecord(p))

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_writer(parsed):
    """
    Transforms the final parsing result into an Writer instance.

    :param parsed: result of parsing the Writer info in a Writer record
    :return: a Writer created from the parsed record
    """
    return Writer(parsed.ip_n, parsed.personal_number, parsed.ipi_base_n, parsed.writer_first_name,
                  parsed.writer_last_name,
                  parsed.tax_id, parsed.ipi_name_n)


def _to_writerrecord(parsed):
    """
    Transforms the final parsing result into an WriterRecord instance.

    :param parsed: result of parsing a Writer record
    :return: an WriterRecord created from the parsed record
    """
    decoder = WriterRecordDictionaryDecoder()
    return decoder.decode(parsed)