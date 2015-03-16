# -*- coding: utf-8 -*-

import codecs

import chardet

"""
This is a small tool to read the contents of a file, trying to convert its contents to UTF-8.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Reader():
    def __init__(self):
        pass

    def read(self, contents):
        cwr = open(contents, 'rt')

        rawdata = cwr.readline()
        result = chardet.detect(rawdata)
        charenc = result['encoding']

        cwr = codecs.open(contents, 'r', 'latin-1')
        contents = cwr.readline()

        if charenc == 'UTF-8-SIG':
            contents = contents[3:]

        for line in cwr:
            contents += line

        return contents