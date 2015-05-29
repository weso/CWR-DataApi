# -*- coding: utf-8 -*-
import codecs
import time
import logging
import os

from cwr.parser.decoder.file import default_file_decoder
from cwr.utils.printer import CWRPrinter

"""
Visual test for checking a file contents.

This is used to make sure a file contents are correctly printed with a visual or manual check.

All the file contents will be printed on the console.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

if __name__ == '__main__':
    print('File contents parsing test')
    path = raw_input('Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ')
    output = raw_input('Please enter the full path to the file where the results will be stored: ')
    log = raw_input('Please enter the full path to the file where parsing log will be saved: ')
    print('\n')
    print('Reading file %s' % path)
    print('Storing output on %s' % output)
    print('Saving log on %s' % log)
    print('\n')

    logging.basicConfig(filename=log,
                        level=logging.DEBUG,
                        format='%(asctime)s.%(msecs)d %(levelname)s %(module)s - %(funcName)s: %(message)s')
    logger = logging.getLogger(__name__)

    decoder = default_file_decoder()

    data = {}
    data['filename'] = os.path.basename(path)
    data['contents'] = codecs.open(path, 'r', 'latin-1').read()

    start = time.clock()
    data = decoder.decode(data)
    end = time.clock()
    time_parse = (end - start)

    print('Parsed the file in %s seconds' % time_parse)
    print('\n')

    logger.info('Finished parsing n %s seconds' % time_parse)

    output = codecs.open(output, 'w', 'latin-1')

    printer = CWRPrinter()
    printer.print_file(data, output)
