# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import codecs

import chardet


"""
This is a small tool to read the contents of a file, trying to convert its contents to UTF-8.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class FileReader():
    """
    Reads a file contents.

    This is interface serves to add any additional operation which may be needed for the reading process, such as
    changing the file's encoding.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def read(self, file):
        pass


class UTF8AdapterReader(FileReader):
    """
    Reads a file's contents and transforms them into the UTF8 encoding.
    """

    def __init__(self):
        super(UTF8AdapterReader, self).__init__()

    def read(self, file):
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