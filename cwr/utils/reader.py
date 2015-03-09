# -*- encoding: utf-8 -*-
import sys
import codecs
import os

import chardet

from cwr.grammar import file as rule_file


"""
This is a small reader to show a CWR file contents on the console.

The reader is meant just as a quick check tool.
"""

__author__ = 'Borja Garrido Bear, Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _path():
    return os.path.dirname(__file__)


def read(file):
    print('Reading %s file' % file)
    cwr = open(os.path.join(_path(), os.path.basename(file)), 'rt')

    rawdata = cwr.readline()
    result = chardet.detect(rawdata)
    charenc = result['encoding']

    print('Detected the encoding as %s' % charenc)

    cwr = codecs.open(os.path.join(_path(), os.path.basename(file)), 'r', 'latin-1')
    file = cwr.readline()

    print('Initial line is %s' % file)
    if charenc == 'UTF-8-SIG':
        file = file[3:]
        print('Initial line is now %s' % file)

    for line in cwr:
        file += line
    print(file)
    print(rule_file.cwr_file.parseString(file))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        read(sys.argv[1])
    else:
        print('The file to read should be received as parameter')