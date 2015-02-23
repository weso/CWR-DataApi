# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.file import FileTag
from cwr.parsing.grammar import field, special
from cwr.parsing.data.accessor import ParserDataStorage

"""
CWR file name grammar.

This stores grammar for parsing the CWR file name.

As the file name is a very precise type of string, this parsing will be lossless, meaning that all the information
from the file name will be always parsed into the resulting object.

CWR file names follow the pattern CWyynnnnsss_rrr.Vxx, where each section means the following:
CW - Header indicating it is a CWR file.
yy - Year.
nnnn - Sequence. This was originally 2 numbers, later changed to 4.
sss - Sender. 2 or 3 digits.
rrr - Receiver. 2 or 3 digits.
xx - Version of the CWR standard (version x.x).

There are two parsing patterns offered, one for the new format and one for the old.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

# Acquires config data source
data = ParserDataStorage()

# FIELDS
sequence_old = field.numeric(2)
sequence_old.setName('Sequence Number')
sequence_old.setResultsName('sequence_n')

sequence_new = field.numeric(4)
sequence_new.setName('Sequence Number')
sequence_new.setResultsName('sequence_n')

year = field.numeric(2)
year.setParseAction(lambda y: int('20' + y[0]))
year.setName('Year')
year.setResultsName('year')

sender = pp.Word(pp.alphanums, min=2, max=3)
sender.setName('Sender')
sender.setResultsName('sender')

receiver = pp.Word(pp.alphanums, min=2, max=3)
receiver.setName('Received')
receiver.setResultsName('receiver')

version_num = field.numeric_float(2, 1)
version_num.setName('Version')
version_num.setResultsName('version')

# DELIMITERS
header = pp.CaselessLiteral('CW')
header.suppress()
header.setName('Filename Header')

delimiter_version = pp.CaselessLiteral('.V')
delimiter_version.suppress()
delimiter_version.setName('Version Separator')

delimiter_ip = pp.Literal('_')
delimiter_ip.suppress()
delimiter_ip.setName('IPs separator')

delimiter_zip = pp.CaselessLiteral('.zip')
delimiter_zip.setParseAction(lambda s: data.default_version())
delimiter_zip.setName('zip extension')
delimiter_zip.setResultsName('version')

# CWR filename patterns
cwr_filename_old = special.lineStart + header + year + sequence_old + sender + delimiter_ip + receiver \
                   + ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd
cwr_filename = special.lineStart + header + year + sequence_new + sender + delimiter_ip + receiver + \
               ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd

# Parsing actions
cwr_filename.setParseAction(lambda p: _to_filetag(p))
cwr_filename_old.setParseAction(lambda p: _to_filetag(p))

# TRANSFORMATION METHODS

"""
These are the methods which transform nodes into instances of classes.
"""


def _to_filetag(parsed):
    """
    Transforms the final parsing result into a FileTag instance.

    :param parsed: result of parsing a file name
    :return: a FileTag created from the file name
    """
    return FileTag(parsed.year, parsed.sequence_n, parsed.sender, parsed.receiver, parsed.version)