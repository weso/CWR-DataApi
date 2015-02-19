# -*- encoding: utf-8 -*-

import os
import csv

"""
Accessor for the parsing data config files.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class ParserDataStorage(object):
    _file_record_types = 'cwr_record_type.csv'
    _file_sender_types = 'cwr_sender_type.csv'
    _file_character_sets = 'cwr_character_set.csv'

    _character_sets = None
    _record_types = None
    _sender_types = None

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __path(self):
        return os.path.dirname(__file__)

    def character_sets(self):
        """
        Allowed character sets.

        These are the type of character sets which a file may have.

        :return: the allowed character sets
        """
        if self._character_sets is None:
            self._character_sets = self.__read_file(self._file_character_sets)

        return self._character_sets

    def record_types(self):
        """
        Types of records.

        These are the initial three digit alphanumeric codes of the records.

        :return: the allowed CWR record type codes
        """
        if self._record_types is None:
            self._record_types = self.__read_file(self._file_record_types)

        return self._record_types

    def sender_types(self):
        """
        Types of sender.

        These are the codes identifying file senders.

        :return: the allowed CWR file sender codes
        """
        if self._sender_types is None:
            self._sender_types = self.__read_file(self._file_sender_types)

        return self._sender_types

    def __read_file(self, file_name):
        result = []
        with open(os.path.join(self.__path(), os.path.basename(file_name)), 'rt') as csvfile:
            headers_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for type_row in headers_reader:
                for t in type_row:
                    result.append(t)
        return result