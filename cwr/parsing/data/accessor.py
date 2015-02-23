# -*- encoding: utf-8 -*-

import os
import csv

import yaml


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
    _file_transaction_types = 'cwr_transaction_type.csv'

    _file_record_config = 'cwr_record_config.yml'
    _file_defaults = 'cwr_defaults.yml'

    _character_sets = None
    _record_types = None
    _sender_types = None
    _transaction_types = None

    _record_config = None
    _cwr_defaults = None

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
            self._character_sets = self.__read_csv_file(self._file_character_sets)

        return self._character_sets

    def cwr_defaults(self):
        """
        Current CWR standards defaults.

        :return: the current CWR standards defaults
        """
        if self._cwr_defaults is None:
            self._cwr_defaults = self.__read_yaml_file(self._file_defaults)

        return self._cwr_defaults

    def default_version(self):
        """
        The current version of the CWR standard.

        :return: the current version of the CWR standard
        """
        return self.cwr_defaults()['default_version']

    def record_type(self, record):
        """
        Returns the expected record type for the received record.

        The record is the internal name used to identify a record type.

        :param record: the id for the record type
        :return: the expected record type on the record prefix
        """
        return self.record_config()[record]['type']

    def field_size(self, record, field):
        """
        Returns the expected size for a record's field.

        The record and field are the internal name used to identify a record type.

        :param record: the id for the record type
        :param field: the id for the field
        :return: the expected size for the field on the record
        """
        return self.record_config()[record][field]['size']

    def field_value(self, record, field):
        """
        Returns the expected value for a record's field.

        The record and field are the internal name used to identify a record type.

        :param record: the id for the record type
        :param field: the id for the field
        :return: the expected value for the field on the record
        """
        return self.record_config()[record][field]['value']

    def record_config(self):
        """
        Configuration for the different record types.

        This is loaded from a YAML file.

        :return: the configuration for the different record types
        """
        if self._record_config is None:
            self._record_config = self.__read_yaml_file(self._file_record_config)

        return self._record_config

    def record_types(self):
        """
        Types of records.

        These are the initial three digit alphanumeric codes of the records.

        :return: the allowed CWR record type codes
        """
        if self._record_types is None:
            self._record_types = self.__read_csv_file(self._file_record_types)

        return self._record_types

    def sender_types(self):
        """
        Types of sender.

        These are the codes identifying file senders.

        :return: the allowed CWR file sender codes
        """
        if self._sender_types is None:
            self._sender_types = self.__read_csv_file(self._file_sender_types)

        return self._sender_types

    def transaction_types(self):
        """
        Types of transactions.

        These are the codes identifying group transactions.

        :return: the allowed CWR file transaction codes
        """
        if self._transaction_types is None:
            self._transaction_types = self.__read_csv_file(self._file_transaction_types)

        return self._transaction_types

    def __read_csv_file(self, file_name):
        """
        Parses a CSV file into a list.

        :param file_name: name of the CSV file
        :return: a list with the file's contents
        """
        result = []
        with open(os.path.join(self.__path(), os.path.basename(file_name)), 'rt') as csvfile:
            headers_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for type_row in headers_reader:
                for t in type_row:
                    result.append(t)
        return result

    def __read_yaml_file(self, file_name):
        """
        Parses a YAML file into a matrix.

        :param file_name: name of the YAML file
        :return: a matrix with the file's contents
        """
        with open(os.path.join(self.__path(), os.path.basename(file_name)), 'rt') as yamlfile:
            return yaml.load(yamlfile)