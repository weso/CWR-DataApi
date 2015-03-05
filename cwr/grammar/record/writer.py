# -*- encoding: utf-8 -*-

from data.accessor import CWRConfiguration
from cwr.grammar.record import publisher, society
from cwr.grammar.field import table, special, record, basic
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
General fields.
"""

# Writer Last Name
last_name = basic.alphanum(_config.field_size('writer', 'last_name'))
last_name = last_name.setName('Writer Last Name').setResultsName('last_name')

# Writer First Name
first_name = basic.alphanum(_config.field_size('writer', 'first_name'))
first_name = first_name.setName('Writer First Name').setResultsName('first_name')

# Writer Unknown Indicator
unknown = basic.flag()
unknown = unknown.setName('Writer Unknown Indicator').setResultsName('writer_unknown')

# Reversionary Indicator
reversionary = basic.flag()
reversionary = reversionary.setName('Reversionary Indicator').setResultsName('reversionary')

# First Recording Refusal Indicator
refusal = basic.flag()
refusal = refusal.setName('First Recording Refusal Indicator').setResultsName('first_record_refusal')

# Work For Hire Indicator
for_hire = basic.flag()
for_hire = for_hire.setName('Work For Hire Indicator').setResultsName('work_for_hire')

# Personal Number
personal_number = basic.numeric(_config.field_size('writer', 'personal_number'))
personal_number = personal_number.setName('Personal Number').setResultsName('personal_number')

"""
Patterns.
"""

writer = special.lineStart + record.record_prefix(
    _config.record_type('writer'), compulsory=True) + special.ip_id() + last_name + first_name + unknown + \
         table.writer_designation() + publisher.tax_id + special.ipi_name_number() + \
         society.pr_affiliation() + society.pr_share() + \
         society.mr_affiliation() + society.mr_share() + \
         society.sr_affiliation() + society.sr_share() + \
         reversionary + refusal + for_hire + special.blank(_config.field_size('writer', 'filler')) + \
         special.ipi_base_number() + personal_number + table.usa_license() + special.lineEnd

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