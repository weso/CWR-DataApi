# -*- coding: utf-8 -*-
import os
import logging

from cwr.file import CWRFile, FileTag
from cwr.parser.common import GrammarDecoder, GrammarFileDecoder
from cwr.parser.common import Decoder
from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldTerminalRuleFactory
from data.accessor import CWRTables
from cwr.grammar.factory.rule import DefaultRuleFactory
from cwr.grammar.factory.decorator import RecordRuleDecorator, GroupRuleDecorator


"""
Parsers for decoding CWR files, creating a graph of CWR classes from them.

While the decoder classes are accessible, they are meant to be used directly only when creating custom versions,
by default the factory methods default_file_decoder() and default_filename_decoder() should be used to acquire
the decoders to use when reading a file.

The default_file_decoder() will return a decoder which parses a CWR file complying with the standard, while the
default_filename_decoder() method will return a decoder which parses a CWR filename which follows the old or the new
file naming convention.

The file decoder will also parse the filename, using the second parser for it, and return a CWRFile instance. The
filename decoder will return a FileTag.

The base classes used on these parsers are FileDecoder and FileNameDecoder, both of them requiring information about
the grammar to be used when parsing.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


def default_file_decoder():
    """
    Creates a decoder which parses a CWR file, creating a CWRFile class instance from it.

    :return: a CWR file decoder for the default standard
    """
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))

    _factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

    _rules = _config.load_transaction_config('common')
    _rules.update(_config.load_record_config('common'))
    _rules.update(_config.load_group_config('common'))

    _decorators = {'transaction': RecordRuleDecorator(_factory_field),
                   'record': RecordRuleDecorator(_factory_field),
                   'group': GroupRuleDecorator()}
    _group_rule_factory = DefaultRuleFactory(_rules, _factory_field, _decorators)

    return FileDecoder(_group_rule_factory.get_rule('transmission'), default_filename_decoder())


def default_filename_decoder():
    """
    Creates a decoder which parses CWR filenames following the old or the new convention.

    :return: a CWR filename decoder for the old and the new conventions
    """
    _config = CWRConfiguration()

    _data = _config.load_field_config('table')
    _data.update(_config.load_field_config('common'))
    _data.update(_config.load_field_config('filename'))

    _factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

    _group_rule_factory = DefaultRuleFactory(_config.load_record_config('filename'), _factory_field)

    grammar_old = _group_rule_factory.get_rule('filename_old')
    grammar_new = _group_rule_factory.get_rule('filename_new')

    return FileNameDecoder(grammar_old, grammar_new)


class FileDecoder(Decoder):
    """
    Parses a CWR file, both its contents and the file name, to create a CWRFile instance.

    As the CWRFile contains a FileTag, this decoder will also try to decode the file's name.

    For this it will use a second decoder, which will take care of the filename.
    """

    def __init__(self, grammar, filename_decoder):
        super(FileDecoder, self).__init__()

        # Logger
        self._logger = logging.getLogger(__name__)

        self._filename_decoder = filename_decoder
        self._file_decoder = GrammarFileDecoder(grammar)

    def decode(self, path):
        """
        Parses the file, creating a CWRFile from it.

        :param path: path to the file to parse
        :return: a CWRFile instance
        """
        filename = self._filename_decoder.decode(os.path.basename(path))

        transmission = self._file_decoder.decode(path)[0]

        return CWRFile(filename, transmission)


class FileNameDecoder(Decoder):
    """
    Parses a CWR filename to create a FileTag instance. It is meant to take care of the old and the new naming
    conventions, and so it will require one grammar rule for each.

    If the filename does not conform any of the two conventions, then an empty FileTag will be returned.
    """

    def __init__(self, grammar_old, grammar_new):
        super(FileNameDecoder, self).__init__()

        self._filename_decoder_old = GrammarDecoder(grammar_old)
        self._filename_decoder_new = GrammarDecoder(grammar_new)

    def decode(self, filename):
        """
        Parses the filename, creating a FileTag from it.

        It will try both the old and the new conventions, if the filename does not conform any of them, then an empty
        FileTag will be returned.

        :param filename: filename to parse
        :return: a FileTag instance
        """
        try:
            file_tag = self._filename_decoder_new.decode(filename)
        except:
            try:
                file_tag = self._filename_decoder_old.decode(filename)
            except:
                file_tag = FileTag(0, 0, '', '', '')

        return file_tag
