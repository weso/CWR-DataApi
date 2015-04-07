# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

from cwr.utils.reader import UTF8AdapterReader


"""
Offers base classes to parse data from CWR model instances.
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
        raise NotImplementedError('The decode method must be implemented')


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
        return self._grammar.parseString(text)[0]


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


class Encoder(object):
    """
    Interface for encoders. These are parsers which transform a a model class into another data.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def encode(self, data):
        """
        Encodes the data, creating an structure from a model object instance.

        :param data: the data to encode
        :return: a data structure created from the received data
        """
        raise NotImplementedError('The encode method must be implemented')
