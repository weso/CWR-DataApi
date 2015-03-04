# -*- encoding: utf-8 -*-

import pyparsing as pp

from cwr.file import FileTag
from cwr.grammar.field import basic, special
from data.accessor import CWRConfiguration


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

# Acquires data sources
_config = CWRConfiguration()

"""
Filename fields.

These fields are:
- Sequence Number (old and new). 2 or 4 alphanumeric characters.
- Year. 2 numeric characters.
- Sender. 2 or 3 alphanumeric characters.
- Receiver. 2 or 3 alphanumeric characters.
- Version Number. 2 digits float (one value for integer, one for decimal).

Each of these fields is parsed into a value as follows:
- Sequence Number (old and new). Integer.
- Year. Four digits integer (year in the current century).
- Sender. String.
- Receiver. String.
- Version Number. Float.
"""

# Sequence Number old
sequence_old = basic.numeric(2)
sequence_old = sequence_old.setName('Sequence Number').setResultsName('sequence_n')

# Sequence Number new
sequence_new = basic.numeric(4)
sequence_new = sequence_new.setName('Sequence Number').setResultsName('sequence_n')

# Year
year = basic.numeric(2)
year.setParseAction(lambda y: int('20' + y[0]))
year = year.setName('Year').setResultsName('year')

# Sender
sender = pp.Word(pp.alphanums, min=2, max=3)
sender = sender.setName('Sender').setResultsName('sender')

# Receiver
receiver = pp.Word(pp.alphanums, min=2, max=3)
receiver = receiver.setName('Received').setResultsName('receiver')

# Version number
version_num = basic.numeric_float(2, 1)
version_num = version_num.setName('Version').setResultsName('version')

"""
Delimiters.

These divide the distinct sections of the filename, and mostly can be ignored.

The only special case is if this is a zip file. In that case the extension will be parsed as if it were the version
node, but will return the default version.
"""

# Filename header
header = pp.CaselessLiteral('CW')
header.suppress()
header.setName('Filename Header')

# Version delimiter
delimiter_version = pp.CaselessLiteral('.V')
delimiter_version.suppress()
delimiter_version.setName('Version Separator')

# Sender and received delimiter
delimiter_ip = pp.Literal('_')
delimiter_ip.suppress()
delimiter_ip.setName('IPs separator')

# ZIP extension
delimiter_zip = pp.CaselessLiteral('.zip')
delimiter_zip.setParseAction(lambda s: _config.default_version())
delimiter_zip = delimiter_zip.setName('zip extension').setResultsName('version')

"""
Filename patterns.

This the grammatical structure for the old and new filename templates.
"""

# CWR filename patterns
cwr_filename_old = special.lineStart + header + year + sequence_old + sender + delimiter_ip + receiver \
                   + ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd
cwr_filename = special.lineStart + header + year + sequence_new + sender + delimiter_ip + receiver + \
               ((delimiter_version + version_num) | delimiter_zip) + special.lineEnd

"""
Parsing actions for the patterns.

Both the old and new filename will be parsed into a FileTag instance.
"""

cwr_filename.setParseAction(lambda p: _to_filetag(p))
cwr_filename_old.setParseAction(lambda p: _to_filetag(p))

# TRANSFORMATION METHODS

"""
Parsing methods.

These are the methods which transform nodes into instances of classes.
"""


def _to_filetag(parsed):
    """
    Transforms the final parsing result into a FileTag instance.

    :param parsed: result of parsing a file name
    :return: a FileTag created from the file name
    """
    return FileTag(parsed.year, parsed.sequence_n, parsed.sender, parsed.receiver, parsed.version)