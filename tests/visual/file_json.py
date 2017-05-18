# -*- coding: utf-8 -*-
import codecs
import os
import time

from cwr.parser.decoder.file import default_file_decoder
from cwr.parser.encoder.cwrjson import JSONEncoder

"""
Visual test for transforming file into a JSON.

This is used to generate a JSON for other tests.

The full JSON will be stored into a file.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

if __name__ == '__main__':
    print('File to JSON test')
    path = input(
        'Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ')
    output = input(
        'Please enter the full path to the file where the results will be stored: ')
    print('\n')
    print(('Reading file %s' % path))
    print(('Storing output on %s' % output))
    print('\n')

    decoder = default_file_decoder()

    data = {}
    data['filename'] = os.path.basename(path)
    data['contents'] = codecs.open(path, 'r', 'latin-1').read()

    print(('Begins parsing CWR at %s' % time.ctime()))
    start = time.clock()
    data = decoder.decode(data)
    end = time.clock()
    time_parse = (end - start)

    print(('Parsed the file in %s seconds' % time_parse))
    print('\n')

    encoder = JSONEncoder()

    print(('Begins creating JSON at %s' % time.ctime()))
    start = time.clock()
    result = encoder.encode(data)
    end = time.clock()
    time_parse = (end - start)

    print(('Created the JSON in %s seconds' % time_parse))
    print('\n')

    start = time.clock()
    output = codecs.open(output, 'w', 'latin-1')
    end = time.clock()
    time_parse = (end - start)

    print(('Saved the JSON in %s seconds' % time_parse))

    output.write(result)
