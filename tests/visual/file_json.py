# -*- coding: utf-8 -*-
import codecs

from cwr.parser.file import CWRFileDecoder
from cwr.parser.cwrjson import JSONEncoder


"""
Visual test for transforming file into a JSON.

This is used to generate a JSON for other tests.

The full JSON will be stored into a file.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

if __name__ == '__main__':
    print('File to JSON test')
    path = raw_input('Please enter the full path to a CWR file (e.g. c:/documents/file.cwr): ')
    output = raw_input('Please enter the full path to the file where the results will be stored: ')
    print('\n')
    print('Reading file %s' % (path))
    print('Storing output on %s' % (output))
    print('\n')

    decoder = CWRFileDecoder()

    data = decoder.decode(path)

    encoder = JSONEncoder()
    result = encoder.encode(data)

    output = codecs.open(output, 'w', 'latin-1')

    output.write(result)