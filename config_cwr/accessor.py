# -*- coding: utf-8 -*-

import os

import yaml
from cwr.grammar.factory.config import rule_config_file

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

    def __init__(self):
        self._parser = rule_config_file

    def __path(self):
        """
        Returns the path to the folder in which this class is contained.

        As this class is to be on the same folder as the data files, this will
        be the data files folder.

        :return: path to the data files folder.
        """
        return os.path.dirname(__file__)

    def read_yaml_file(self, file_name):
        """
        Parses a YAML file into a matrix.

        :param file_name: name of the YAML file
        :return: a matrix with the file's contents
        """
        with open(os.path.join(self.__path(), os.path.basename(file_name)),
                  'rt') as yamlfile:
            return yaml.load(yamlfile)

    def read_config_file(self, file_name):
        """
        Reads a CWR grammar config file.

        :param file_name: name of the text file
        :return: the file's contents
        """
        with open(os.path.join(self.__path(), os.path.basename(file_name)),
                  'rt') as file_config:
            return self._parser.parseString(file_config.read())


class CWRConfiguration(object):
    """
    Offers methods to access the CWR configuration data.
    """

    def __init__(self):
        # Reader for the files
        self._reader = _FileReader()

        # Files containing the CWR info
        self._file_defaults = 'default_values.yml'

        # CWR configuration information
        self._record_config = None
        self._cwr_defaults = None

        self._field_configs = {}
        self._group_configs = {}
        self._record_configs = {}
        self._transaction_configs = {}

    def _load_cwr_defaults(self):
        """
        Loads the CWR default values file, creating a matrix from it, and then
        returns this data.

        The file will only be loaded once.

        :return: the CWR default values matrix
        """
        if self._cwr_defaults is None:
            self._cwr_defaults = self._reader.read_yaml_file(
                self._file_defaults)

        return self._cwr_defaults

    def load_field_config(self, file_id):
        """
        Loads the configuration fields file for the id.

        :param file_id: the id for the field
        :return: the fields configuration
        """
        if file_id not in self._field_configs:
            self._field_configs[file_id] = self._reader.read_yaml_file(
                'field_config_%s.yml' % file_id)

        return self._field_configs[file_id]

    def load_group_config(self, file_id):
        """
        Loads the configuration fields file for the id.

        :param file_id: the id for the field
        :return: the fields configuration
        """
        if file_id not in self._group_configs:
            self._group_configs[file_id] = self._reader.read_config_file(
                'group_config_%s.cml' % file_id)

        return self._group_configs[file_id]

    def load_record_config(self, file_id):
        """
        Loads the configuration fields file for the id.

        :param file_id: the id for the field
        :return: the fields configuration
        """
        if file_id not in self._record_configs:
            self._record_configs[file_id] = self._reader.read_config_file(
                'record_config_%s.cml' % file_id)

        return self._record_configs[file_id]

    def load_transaction_config(self, file_id):
        """
        Loads the configuration fields file for the id.

        :param file_id: the id for the field
        :return: the fields configuration
        """
        if file_id not in self._transaction_configs:
            self._transaction_configs[file_id] = self._reader.read_config_file(
                'transaction_config_%s.cml' % file_id)

        return self._transaction_configs[file_id]

    def default_version(self):
        """
        The current version of the CWR standard.

        :return: the current version of the CWR standard
        """
        return self._load_cwr_defaults()['default_version']
