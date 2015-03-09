# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.field import table as field_table
from cwr.grammar.field import special as field_special
from cwr.grammar.field import record as field_record
from cwr.grammar.field import society as field_society
from cwr.grammar.field import writer as field_writer
from cwr.grammar.field import publisher as field_publisher
from cwr.interested_party import Writer, WriterRecord


"""
CWR Writer records grammar.

This is for the following records:
- Writer Controlled By Submitter (SWR)
- Other Writer (OWR)
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires data sources
_config = CWRConfiguration()

"""
Patterns.
"""

writer = field_special.lineStart + field_record.record_prefix(
    _config.record_type('writer'),
    compulsory=True) + field_special.ip_id() + field_writer.last_name + field_writer.first_name + field_writer.unknown + \
         field_table.writer_designation() + field_publisher.tax_id + field_special.ipi_name_number() + \
         field_society.pr_affiliation() + field_society.pr_share() + \
         field_society.mr_affiliation() + field_society.mr_share() + \
         field_society.sr_affiliation() + field_society.sr_share() + \
         field_writer.reversionary + field_writer.refusal + field_writer.for_hire + field_special.blank(
    _config.field_size('writer', 'filler')) + \
         field_special.ipi_base_number() + field_writer.personal_number + field_table.usa_license() + field_special.lineEnd

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
    return Writer(parsed.ip_id, parsed.personal_number, parsed.ipi_base, parsed.first_name, parsed.last_name,
                  parsed.tax_id, parsed.ipi_name)


def _to_writerrecord(parsed):
    """
    Transforms the final parsing result into an WriterRecord instance.

    :param parsed: result of parsing a Writer record
    :return: an WriterRecord created from the parsed record
    """
    writer_data = _to_writer(parsed)

    return WriterRecord(parsed.record_type, parsed.transaction_sequence_n, parsed.record_sequence_n, writer_data,
                        parsed.writer_designation, parsed.work_for_hire, parsed.writer_unknown, parsed.reversionary,
                        parsed.first_record_refusal, parsed.usa_license, parsed.pr_society,
                        parsed.pr_share, parsed.mr_society, parsed.mr_share,
                        parsed.sr_society, parsed.sr_share)