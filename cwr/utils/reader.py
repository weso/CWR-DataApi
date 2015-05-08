# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import codecs

import chardet


"""
Small tools for reading the contents of a file.

Mainly, this contains a class which helps to convert a file into the UTF-8 format. But this, sadly, does not work on
Python 3.
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
        """
        Processes the received file and returns it's contents.

        :param file: file being read
        """
        pass


class UTF8AdapterReader(FileReader):
    """
    Reads a file's contents and transforms them into the UTF8 encoding.

    Does not work on Python 3.
    """

    def __init__(self):
        super(UTF8AdapterReader, self).__init__()

    def read(self, file):
        """
        Processes the received file and returns it's contents adapted to the UTF-8 format.

        :param file: file being read
        """
        file_contents = open(file, 'rt')

        rawdata = file_contents.readline()
        result = chardet.detect(rawdata)
        charenc = result['encoding']

        file_contents = codecs.open(file, 'r', 'latin-1')
        file = file_contents.readline()

        if charenc == 'UTF-8-SIG':
            file = file[3:]

        for line in file_contents:
            file += line

        return file