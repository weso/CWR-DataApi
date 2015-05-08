# -*- coding: utf-8 -*-
import codecs
import time
import sys

import chardet

from cwr.parser.decoder.file import default_file_decoder


"""
Visual test for checking the parsing speed.

This is used to check how long it takes to read a file with a visual or manual check.

All the info will be printed on the console.
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
    print("Parsing speed test")
    path = raw_input("Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ")
    print '\n'
    print "Reading file %s" % (path)
    print '\n'

    times = 100

    print "The file will be read and parsed %s times. Then the average will be shown." % (times)

    time_total_avg = 0
    time_read_avg = 0
    time_parse_avg = 0

    for x in range(0, times):
        start = time.clock()
        file = _read(path)
        finish = time.clock()
        time_read = (finish - start)
        time_read_avg += time_read

        decoder = default_file_decoder()

        start = time.clock()
        data = decoder.decode(path)
        finish = time.clock()
        time_parse = (finish - start)
        time_parse_avg += time_parse

        time_total_avg += time_read + time_parse
        sys.stdout.write('.')

    time_total_avg = time_total_avg / times
    time_read_avg = time_read_avg / times
    time_parse_avg = time_parse_avg / times

    print('Average times:')
    print('Reading time: %s' % (time_read_avg))
    print('Parsing time: %s' % (time_parse_avg))
    print('Total time: %s' % (time_total_avg))