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
