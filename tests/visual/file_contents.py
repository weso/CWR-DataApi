# -*- coding: utf-8 -*-
import codecs
import time

import chardet

from cwr.grammar import file as rule_file
from cwr.utils.printer import CWRPrinter


"""
Visual test for checking a file contents.

This is used to make sure a file contents are correctly printed with a visual or manual check.

All the file contents will be printed on the console.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


def _read(file):
    cwr = open(file, 'rt')

    rawdata = cwr.readline()
    result = chardet.detect(rawdata)
    charenc = result['encoding']

    cwr = codecs.open(file, 'r', 'latin-1')
    file = cwr.readline()

    if charenc == 'UTF-8-SIG':
        file = file[3:]

    for line in cwr:
        file += line

    return file


if __name__ == '__main__':
    print("Write the file's path")
    path = raw_input("Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ")
    print '\n'
    print "Reading file %s" % (path)
    print '\n'

    start = time.clock()
    file = _read(path)
    end = time.clock()
    final = (end - start)

    print 'Read the file in %s seconds' % (final)
    print '\n'

    start = time.clock()
    data = rule_file.cwr_transmission.parseString(file)[0]
    end = time.clock()
    final = (end - start)

    print 'Parsed the file in %s seconds' % (final)
    print '\n'

    printer = CWRPrinter()
    printer.print_transmission(data)