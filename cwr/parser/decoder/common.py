# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging

from cwr.utils.reader import UTF8AdapterReader


"""
Base classes for implementing decoder parsers.

A decoder parser receives a data structure and returns an instance of a class from the domain model.

For example, it may receive a JSON and return a CWRFile instance.

All decoders are expected to implement the Decoder interface. This offers a single method which receives the data to
decode, and returns an equivalent model class instance.

Additionally, two decoders for handling grammar rules are included:
- GrammarDecoder, which decodes a string applying a Pyparsing grammar rule.
- GrammarFileDecoder, an extension of the previous decoder meant to work with files.

Note that in the context of the project these parsers are expected to be lossfull. Not all the data in the CWR files
is useful, some rows contains information which can be safely ignored, but also they may parse sources, such as JSON
structures, where additional and unneeded data has been added.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class Decoder(object):
    """
    Interface for implementing decoder parsers. These parser receive a data structure and return an instance of a class
    from the domain model.
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def decode(self, data):
        """
        Decodes the data, creating an instance of a class from the domain model.

        :param data: the data to decode
        :return: a class representing the data
        """
        raise NotImplementedError('The decode method must be implemented')


class GrammarDecoder(Decoder):
    """
    Decodes a string applying grammar rules to it, which are meant to be Pyparsing grammar rules.

    The actual parsing work will be done by this rule, and it is expected to include any action required to transform
    it into the returned value.

    Note that the decoder expects an string, but it can contain multiple lines, separated by the new line indicator.
    """

    def __init__(self, grammar):
        super(GrammarDecoder, self).__init__()
        self._grammar = grammar

    @property
    def grammar(self):
        """
        Grammar for decoding the string.

        This is meant to be a Pyparsing grammar rule, and it is expected to include an action for transforming the
        text into the expected result.

        :return: the grammar used for decoding the string
        """
        return self._grammar

    def decode(self, text):
        """
        Decodes the string, creating an instance of a class from the domain model.

        For this a Pyparsing grammar rule will be applied to the string.

        :param data: the data to decode
        :return: a class representing the data
        """
        return self._grammar.parseString(text)


class GrammarFileDecoder(GrammarDecoder):
    """
    Parses the contents of a file based on a Pyparsing grammar rules set.

    By default, this expects the file to be on the UTF-8 format.
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
