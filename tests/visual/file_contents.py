# -*- coding: utf-8 -*-
import codecs
import time
import logging

from cwr.parser.file import CWRFileDecoder
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

if __name__ == '__main__':
    print('File contents parsing test')
    path = raw_input('Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ')
    output = raw_input('Please enter the full path to the file where the results will be stored: ')
    log = raw_input('Please enter the full path to the file where parsing log will be saved: ')
    print('\n')
    print('Reading file %s' % (path))
    print('Storing output on %s' % (output))
    print('Saving long on %s' % (log))
    print('\n')

    logging.basicConfig(filename=log,
                        level=logging.DEBUG,
                        )
    logger = logging.getLogger(__name__)

    decoder = CWRFileDecoder()

    start = time.clock()
    data = decoder.decode(path)
    end = time.clock()
    time_parse = (end - start)

    print('Parsed the file in %s seconds' % (time_parse))
    print('\n')

    logger.info('Finished parsing n %s seconds' % time_parse)

    output = codecs.open(output, 'w', 'latin-1')

    printer = CWRPrinter()
    printer.print_file(data, output)