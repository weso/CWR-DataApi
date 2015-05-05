# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging

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
        return self._grammar.parseString(text)


class GrammarFileDecoder(GrammarDecoder):
    """
    Parses the contents of a file based on a Pyparsing grammar rules set.
    """

    def __init__(self, grammar, reader=None):
        super(GrammarFileDecoder, self).__init__(grammar)
        self._logger = logging.getLogger(__name__)

        if reader is None:
            self._reader = UTF8AdapterReader()
        else:
            self._reader = reader

    def decode(self, path):
        self._logger.info('Begins reading file %s' % path)
        data = self.reader.read(path)
        self._logger.info('Finished reading file %s' % path)

        self._logger.info('Begins decoding file %s' % path)
        result = super(GrammarFileDecoder, self).decode(data)
        self._logger.info('Finished decoding file %s' % path)

        return result

    @property
    def reader(self):
        return self._reader
