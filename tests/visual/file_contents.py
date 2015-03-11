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
    print("File contents parsing test")
    path = raw_input("Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ")
    output = raw_input("Please enter the full path to the file where the results will be stored: ")
    print '\n'
    print "Reading file %s" % (path)
    print "Storing output on %s" % (output)
    print '\n'

    start = time.clock()
    file = _read(path)
    end = time.clock()
    time_read = (end - start)

    print 'Read the file in %s seconds' % (time_read)
    print '\n'

    start = time.clock()
    data = rule_file.cwr_transmission.parseString(file)[0]
    end = time.clock()
    time_parse = (end - start)

    print 'Parsed the file in %s seconds' % (time_parse)
    print '\n'

    print 'In total the process took %s seconds' % (time_read + time_parse)
    print '\n'

    output = codecs.open(output, 'w', 'latin-1')

    printer = CWRPrinter()
    printer.print_transmission(data, output)