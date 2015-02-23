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

# Fields
sequence_old = field.numeric(2).setName('Sequence Number').setResultsName('sequence_n')
sequence_new = field.numeric(4).setName('Sequence Number').setResultsName('sequence_n')
year = field.numeric(2).setName('Year').setResultsName('year')
sender = pp.Word(pp.alphanums, min=2, max=3).setName('Sender').setResultsName('sender')
receiver = pp.Word(pp.alphanums, min=2, max=3).setName('Received').setResultsName('receiver')
version_num = field.numeric_float(2, 1).setName('Version').setResultsName('version')

# Delimiters
header = pp.CaselessLiteral('CW').setName('Filename Header').suppress()
delimiter_version = pp.CaselessLiteral('.V').setName('Version Separator').suppress()
delimiter_ip = pp.Literal('_').setName('IPs separator').suppress()
delimiter_zip = pp.CaselessLiteral('.zip').setName('zip extension').setResultsName('version')

# CWR filename patterns
cwr_filename_old = special.lineStart + header + year + sequence_old + sender + delimiter_ip + receiver \
                   + ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd
cwr_filename = special.lineStart + header + year + sequence_new + sender + delimiter_ip + receiver + \
               ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd

# Parsing actions
delimiter_zip.setParseAction(lambda s: data.default_version())
year.setParseAction(lambda y: int('20' + y[0]))

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