# -*- coding: utf-8 -*-
import os
from abc import ABCMeta, abstractmethod

from cwr.grammar.file import cwr_transmission as rule_file
from cwr.grammar.filename import cwr_filename_old as rule_filename
from cwr.file import CWRFile
from cwr.utils.reader import UTF8AdapterReader


"""
Offers classes to parse data into CWR model instances.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Decoder(object):
    """
    Interface for decoders. These are parsers which transform an input into a graph of model classes.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def decode(self, data):
        """
        Decodes the data, creating a graph of model classes.

        :param data: the data to decode
        :return: a graph of model classes
        """
        pass


class GrammarDecoder(Decoder):
    """
    Parses a string based on a Pyparsing grammar rules set.
    """

    def __init__(self, grammar):
        super(GrammarDecoder, self).__init__()
        self._grammar = grammar

    @property
    def grammar(self):
        return self._grammar

    def decode(self, text):
        return self._grammar().parseString(text)[0]


class GrammarFileDecoder(GrammarDecoder):
    """
    Parses the contents of a file based on a Pyparsing grammar rules set.
    """

    def __init__(self, grammar, reader=None):
        super(GrammarFileDecoder, self).__init__(grammar)

        if reader is None:
            self._reader = UTF8AdapterReader()
        else:
            self._reader = reader

    def decode(self, path):
        return super(GrammarFileDecoder, self).decode(self.reader.read(path))

    @property
    def reader(self):
        return self._reader


class CWRFileDecoder(object):
    """
    Parses a CWR file, both its contents and the file name, to create a CWRFile instance.
    """

    def __init__(self):
        self._filename_decoder = GrammarDecoder(rule_filename)
        self._file_decoder = GrammarFileDecoder(rule_file)

    def decode(self, path):
        filename = self._filename_decoder.decode(os.path.basename(path))
        transmission = self._file_decoder.decode(path)

        return CWRFile(filename, transmission)