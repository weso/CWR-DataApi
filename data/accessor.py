# -*- coding: utf-8 -*-

import os
import csv

import yaml


"""
Facades for accessing the configuration data.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'


class _FileReader(object):
    """
    Offers methods to read the data files.
    """

    # Singleton control object
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __path(self):
        """
        Returns the path to the folder in which this class is contained.

        As this class is to be on the same folder as the data files, this will be the data files folder.

        :return: path to the data files folder.
        """
        return os.path.dirname(__file__)

    def read_csv_file(self, file_name):
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

    def read_yaml_file(self, file_name):
        """
        Parses a YAML file into a matrix.

        :param file_name: name of the YAML file
        :return: a matrix with the file's contents
        """
        with open(os.path.join(self.__path(), os.path.basename(file_name)), 'rt') as yamlfile:
            return yaml.load(yamlfile)


class CWRConfiguration(object):
    """
    Offers methods to access the CWR configuration data.
    """

    def __init__(self):
        # Reader for the files
        self._reader = _FileReader()

        # Files containing the CWR info
        self._file_record_config = 'record_config.yml'
        self._file_record_type = 'record_type.yml'
        self._file_defaults = 'default_values.yml'

        # CWR configuration information
        self._record_config = None
        self._record_type = None
        self._cwr_defaults = None

        self._field_configs = {}

    def _load_record_config(self):
        """
        Loads the CWR configuration file, creating a matrix from it, and then returns this data.

        The file will only be loaded once.

        :return: the CWR configuration matrix
        """
        if self._record_config is None:
            self._record_config = self._reader.read_yaml_file(self._file_record_config)

        return self._record_config

    def _load_record_type(self):
        """
        Loads the CWR record type configuration file, creating a matrix from it, and then returns this data.

        The file will only be loaded once.

        :return: the CWR record type configuration matrix
        """
        if self._record_type is None:
            self._record_type = self._reader.read_yaml_file(self._file_record_type)

        return self._record_type

    def _load_cwr_defaults(self):
        """
        Loads the CWR default values file, creating a matrix from it, and then returns this data.

        The file will only be loaded once.

        :return: the CWR default values matrix
        """
        if self._cwr_defaults is None:
            self._cwr_defaults = self._reader.read_yaml_file(self._file_defaults)

        return self._cwr_defaults

    def load_field_config(self, id):
        """
        Loads the configuration fields file for the id.

        :param id: the id for the field
        :return: the fields configuration
        """
        if id not in self._field_configs:
            self._field_configs[id] = self._reader.read_yaml_file('field_config_%s.yml' % id)

        return self._field_configs[id]

    def default_version(self):
        """
        The current version of the CWR standard.

        :return: the current version of the CWR standard
        """
        return self._load_cwr_defaults()['default_version']

    def field_size(self, record, field):
        """
        Returns the expected size for a record's field.

        The record and field are the internal name used to identify a record type.

        :param record: the id for the record type
        :param field: the id for the field
        :return: the expected size for the field on the record
        """
        return self._load_record_config()[record][field]['size']

    def field_value(self, record, field):
        """
        Returns the expected value for a record's field.

        The record and field are the internal name used to identify a record type.

        :param record: the id for the record type
        :param field: the id for the field
        :return: the expected value for the field on the record
        """
        return self._load_record_config()[record][field]['value']

    def record_type(self, record):
        """
        Returns the expected record type for the received record.

        The record is the internal name used to identify a record type.

        :param record: the id for the record type
        :return: the expected record type on the record prefix
        """
        return self._load_record_type()[record]


class CWRTables(object):
    """
    Accesses the data inside CWR table files.

    This is used on the Lookup fields, to know which values are valid.

    The files are read only once, and then the data is stored to be returned each time it is required.
    """

    def __init__(self):
        self._file_values = {}
        # Reader for the files
        self._reader = _FileReader()

    def get_data(self, id):
        """
        Acquires the data from the table identified by the id.

        The file is read only once, consecutive calls to this method will return the sale collection.

        :param id: identifier for the table
        :return: all the values from the table
        """
        if not id in self._file_values:
            file = 'cwr_%s.csv' % id
            self._file_values[id] = self._reader.read_csv_file(file)

        return self._file_values[id]