# -*- encoding: utf-8 -*-

import os
import csv

import yaml


"""
Facades for accessing the configuration data.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
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

    # Reader for the files
    _reader = _FileReader()

    # Files containing the CWR info
    _file_record_config = 'record_config.yml'
    _file_defaults = 'default_values.yml'

    # CWR configuration information
    _record_config = None
    _cwr_defaults = None

    # Singleton control object
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state

    def _load_record_config(self):
        """
        Loads the CWR configuration file, creating a matrix from it, and then returns this data.

        The file will only be loaded once.

        :return: the CWR configuration matrix
        """
        if self._record_config is None:
            self._record_config = self._reader.read_yaml_file(self._file_record_config)

        return self._record_config

    def _load_cwr_defaults(self):
        """
        Loads the CWR default values file, creating a matrix from it, and then returns this data.

        The file will only be loaded once.

        :return: the CWR default values matrix
        """
        if self._cwr_defaults is None:
            self._cwr_defaults = self._reader.read_yaml_file(self._file_defaults)

        return self._cwr_defaults

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
        return self._load_record_config()[record]['type']


class CWRTables(object):
    """
    Offers methods to access the CWR Lookup Tables data.
    """

    # Reader for the files
    _reader = _FileReader()

    # Files for the tables
    _file_record_types = 'cwr_record_type.csv'
    _file_sender_types = 'cwr_sender_type.csv'
    _file_agreement_types = 'cwr_agreement_type.csv'
    _file_agreement_roles = 'cwr_agreement_role.csv'
    _file_transaction_types = 'cwr_transaction_type.csv'
    _file_composite_type = 'cwr_composite_type.csv'
    _file_work_type = 'cwr_work_type.csv'
    _file_lyric_adaptation = 'cwr_lyric_adaptation.csv'
    _file_music_arrangement = 'cwr_music_arrangement.csv'
    _file_version_type = 'cwr_version_type.csv'
    _file_excerpt_type = 'cwr_excerpt_type.csv'
    _file_tmr = 'cwr_text_music_relationship.csv'
    _file_mwdc = 'cwr_musical_work_distribution_category.csv'
    _file_language_codes = 'cwr_language_code.csv'
    _file_character_sets = 'cwr_character_set.csv'
    _file_transaction_status = 'cwr_transaction_status.csv'
    _file_tis = 'cwr_tis.csv'
    _file_society_codes = 'cwr_society_code.csv'
    _file_publisher_type = 'cwr_society_code.csv'
    _file_special_agreement_indicator = 'cwr_special_agreement_indicator.csv'
    _file_usa_license_indicators = 'cwr_usa_license_indicator.csv'

    # Data loaded from the tables
    _composite_types = None
    _work_types = None
    _lyric_adaptations = None
    _music_arrangement = None
    _record_types = None
    _sender_types = None
    _agreement_types = None
    _agreement_roles = None
    _transaction_types = None
    _version_types = None
    _excerpt_types = None
    _tmr = None
    _mwdc = None
    _language_codes = None
    _character_sets = None
    _transaction_status = None
    _tis = None
    _society_codes = None
    _publisher_type = None
    _special_agreement_indicator = None
    _usa_license_indicators = None

    def agreement_roles(self):
        """
        Roles for Agreements.

        :return: the allowed CWR Agreement role codes
        """
        if self._agreement_roles is None:
            self._agreement_roles = self._reader.read_csv_file(self._file_agreement_roles)

        return self._agreement_roles

    def agreement_types(self):
        """
        Types of Agreement.

        These are the allowed Agreement types.

        :return: the allowed CWR Agreement type codes
        """
        if self._agreement_types is None:
            self._agreement_types = self._reader.read_csv_file(self._file_agreement_types)

        return self._agreement_types

    def character_sets(self):
        """
        Allowed character sets.

        These are the type of character sets which a file may have.

        :return: the allowed character sets
        """
        if self._character_sets is None:
            self._character_sets = self._reader.read_csv_file(self._file_character_sets)

        return self._character_sets

    def composite_types(self):
        """
        Composite Types.

        :return: the allowed CWR Composite Type codes
        """
        if self._composite_types is None:
            self._composite_types = self._reader.read_csv_file(self._file_composite_type)

        return self._composite_types

    def excerpt_types(self):
        """
        CWR Excerpt Types.

        :return: the allowed Excerpt Type codes
        """
        if self._excerpt_types is None:
            self._excerpt_types = self._reader.read_csv_file(self._file_excerpt_type)

        return self._excerpt_types

    def language_codes(self):
        """
        Allowed language codes.

        :return: the allowed language codes
        """
        if self._language_codes is None:
            self._language_codes = self._reader.read_csv_file(self._file_language_codes)

        return self._language_codes

    def lyric_adaptations(self):
        """
        Lyric Adaptation codes.

        :return: the allowed CWR Lyric Adaptation codes
        """
        if self._lyric_adaptations is None:
            self._lyric_adaptations = self._reader.read_csv_file(self._file_lyric_adaptation)

        return self._lyric_adaptations

    def music_arrangements(self):
        """
        Music Arrangement codes.

        :return: the allowed Music Arrangement codes
        """
        if self._music_arrangement is None:
            self._music_arrangement = self._reader.read_csv_file(self._file_music_arrangement)

        return self._music_arrangement

    def musical_work_distribution_categories(self):
        """
        Musical Work Distribution Categories.

        These are the allowed Musical Work Distribution Categories.

        :return: the allowed Musical Work Distribution Categories codes
        """
        if self._mwdc is None:
            self._mwdc = self._reader.read_csv_file(self._file_mwdc)

        return self._mwdc

    def publisher_types(self):
        """
        Publisher Types.

        :return: the allowed Publisher Type codes
        """
        if self._publisher_type is None:
            self._publisher_type = self._reader.read_csv_file(self._file_publisher_type)

        return self._publisher_type

    def record_types(self):
        """
        Types of records.

        These are the initial three digit alphanumeric codes of the records.

        :return: the allowed CWR record type codes
        """
        if self._record_types is None:
            self._record_types = self._reader.read_csv_file(self._file_record_types)

        return self._record_types

    def sender_types(self):
        """
        Types of sender.

        These are the codes identifying file senders.

        :return: the allowed CWR file sender codes
        """
        if self._sender_types is None:
            self._sender_types = self._reader.read_csv_file(self._file_sender_types)

        return self._sender_types

    def society_codes(self):
        """
        Society Codes.

        :return: the allowed rights societies codes
        """
        if self._society_codes is None:
            self._society_codes = self._reader.read_csv_file(self._file_society_codes)

        return self._society_codes

    def special_agreement_indicators(self):
        """
        Special Agreement Indicators.

        :return: the allowed Special Agreement Indicator codes
        """
        if self._special_agreement_indicator is None:
            self._special_agreement_indicator = self._reader.read_csv_file(self._file_special_agreement_indicator)

        return self._special_agreement_indicator

    def text_music_relationships(self):
        """
        Text-Music Relationships.

        These are the allowed Text-Music Relationship code.

        :return: the allowed Text-Music Relationship codes
        """
        if self._tmr is None:
            self._tmr = self._reader.read_csv_file(self._file_tmr)

        return self._tmr

    def tis_codes(self):
        """
        TIS codes.

        :return: the allowed TIS codes
        """
        if self._tis is None:
            values = self._reader.read_csv_file(self._file_tis)
            self._tis = []
            for code in values:
                value = code
                while len(value) < 4:
                    value = '0' + value
                self._tis.append(value)

        return self._tis

    def transaction_status(self):
        """
        Transaction Status codes

        :return: the allowed CWR file transaction status codes
        """
        if self._transaction_status is None:
            self._transaction_status = self._reader.read_csv_file(self._file_transaction_status)

        return self._transaction_status

    def transaction_types(self):
        """
        Types of transactions.

        These are the codes identifying group transactions.

        :return: the allowed CWR file transaction codes
        """
        if self._transaction_types is None:
            self._transaction_types = self._reader.read_csv_file(self._file_transaction_types)

        return self._transaction_types

    def usa_license_indicators(self):
        """
        USA License Indicator.

        :return: the allowed CWR USA License Indicator codes
        """
        if self._usa_license_indicators is None:
            self._usa_license_indicators = self._reader.read_csv_file(self._file_usa_license_indicators)

        return self._usa_license_indicators

    def version_types(self):
        """
        Version Types.

        :return: the allowed Version Type codes
        """
        if self._version_types is None:
            self._version_types = self._reader.read_csv_file(self._file_version_type)

        return self._version_types

    def work_types(self):
        """
        Work Type codes.

        :return: the allowed CWR Work Type codes
        """
        if self._work_types is None:
            self._work_types = self._reader.read_csv_file(self._file_work_type)

        return self._work_types