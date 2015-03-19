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

    # Reader for the files
    _reader = _FileReader()

    # Files containing the CWR info
    _file_record_config = 'record_config.yml'
    _file_defaults = 'default_values.yml'
    _file_field_config_table = 'field_config_table.yml'

    # CWR configuration information
    _record_config = None
    _cwr_defaults = None
    _field_config_table = None

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

    def _load_field_config_table(self):
        """
        Loads the table fields configuration.

        The file will only be loaded once.

        :return: the table fields configuration
        """
        if self._field_config_table is None:
            self._field_config_table = self._reader.read_yaml_file(self._file_field_config_table)

        return self._field_config_table

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

    def lookup_field_data(self, field):
        """
        Returns the configuration data for the lookup fields.

        :param field: the id for the field
        :return: the configuration for that field
        """
        return self._load_field_config_table()[field]

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
    _file_publisher_type = 'cwr_publisher_type.csv'
    _file_special_agreement_indicator = 'cwr_special_agreement_indicator.csv'
    _file_usa_license_indicators = 'cwr_usa_license_indicator.csv'
    _file_writer_designation_codes = 'cwr_writer_designation_code.csv'
    _file_title_types = 'cwr_title_type.csv'
    _file_prior_royalty_status = 'cwr_prior_royalty_status.csv'
    _file_post_term_collection_status = 'cwr_post_term_collection_status.csv'
    _file_sales_manufacture_clause = 'cwr_sales_manufacture_clause.csv'
    _file_ie_indicator = 'cwr_ie_indicator.csv'
    _file_recording_format = 'cwr_recording_format.csv'
    _file_recording_technique = 'cwr_recording_technique.csv'
    _file_media_type = 'cwr_media_type.csv'
    _file_intended_purpose = 'cwr_intended_purpose.csv'
    _file_standard_instrumentation_type = 'cwr_standard_instrumentation_type.csv'
    _file_instrument = 'cwr_instrument.csv'
    _file_message_type = 'cwr_message_type.csv'
    _file_message_level = 'cwr_message_level.csv'
    _file_type_of_right = 'cwr_type_of_right.csv'
    _file_subject_code = 'cwr_subject_code.csv'

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
    _writer_designation_codes = None
    _title_types = None
    _prior_royalty_status = None
    _post_term_collection_status = None
    _sales_manufacture_clause = None
    _ie_indicator = None
    _recording_formats = None
    _recording_techniques = None
    _media_types = None
    _intended_purposes = None
    _standard_instrumentation_types = None
    _instruments = None
    _message_types = None
    _message_levels = None
    _type_of_rights = None
    _subject_codes = None

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

    def ie_indicator(self):
        """
        CWR I/E Indicator codes.

        :return: the allowed I/E Indicator codes
        """
        if self._ie_indicator is None:
            self._ie_indicator = self._reader.read_csv_file(self._file_ie_indicator)

        return self._ie_indicator

    def instruments(self):
        """
        CWR Instrument codes.

        :return: the allowed Instrument codes
        """
        if self._instruments is None:
            self._instruments = self._reader.read_csv_file(self._file_instrument)

        return self._instruments

    def intended_purposes(self):
        """
        CWR Intended Purpose codes.

        :return: the allowed Intended Purpose codes
        """
        if self._intended_purposes is None:
            self._intended_purposes = self._reader.read_csv_file(self._file_intended_purpose)

        return self._intended_purposes

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

    def media_types(self):
        """
        Media Type codes.

        :return: the allowed Media Type codes
        """
        if self._media_types is None:
            self._media_types = self._reader.read_csv_file(self._file_media_type)

        return self._media_types

    def message_levels(self):
        """
        Message Level codes.

        :return: the allowed Message Level codes
        """
        if self._message_levels is None:
            self._message_levels = self._reader.read_csv_file(self._file_message_level)

        return self._message_levels

    def message_types(self):
        """
        Message Type codes.

        :return: the allowed Message Type codes
        """
        if self._message_types is None:
            self._message_types = self._reader.read_csv_file(self._file_message_type)

        return self._message_types

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

    def post_term_collection_status(self):
        """
        Post-Term Collection Status codes.

        :return: the allowed Post-Term Collection Status codes
        """
        if self._post_term_collection_status is None:
            self._post_term_collection_status = self._reader.read_csv_file(self._file_post_term_collection_status)

        return self._post_term_collection_status

    def prior_royalty_status(self):
        """
        Prior Royalty Status codes.

        :return: the allowed Prior Royalty Status codes
        """
        if self._prior_royalty_status is None:
            self._prior_royalty_status = self._reader.read_csv_file(self._file_prior_royalty_status)

        return self._prior_royalty_status

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

    def recording_formats(self):
        """
        Types of recordings.

        :return: the allowed CWR recording format codes
        """
        if self._recording_formats is None:
            self._recording_formats = self._reader.read_csv_file(self._file_recording_format)

        return self._recording_formats

    def recording_techniques(self):
        """
        Types of recording techniques.

        :return: the allowed CWR recording technique codes
        """
        if self._recording_techniques is None:
            self._recording_techniques = self._reader.read_csv_file(self._file_recording_technique)

        return self._recording_techniques

    def sales_manufacture_clause(self):
        """
        Sales/Manufacture Clause.

        :return: the allowed CWR Sales/Manufacture Clause codes
        """
        if self._sales_manufacture_clause is None:
            self._sales_manufacture_clause = self._reader.read_csv_file(self._file_sales_manufacture_clause)

        return self._sales_manufacture_clause

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

    def standard_instrumentation_types(self):
        """
        Standard Instrumentation Types.

        :return: the allowed Standard Instrumentation Type codes
        """
        if self._standard_instrumentation_types is None:
            self._standard_instrumentation_types = self._reader.read_csv_file(self._file_standard_instrumentation_type)

        return self._standard_instrumentation_types

    def subject_codes(self):
        """
        Subject Codes.

        :return: the allowed Subject Code codes
        """
        if self._subject_codes is None:
            self._subject_codes = self._reader.read_csv_file(self._file_subject_code)

        return self._subject_codes

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

    def title_types(self):
        """
        Title Types.

        :return: the allowed Title Type codes
        """
        if self._title_types is None:
            self._title_types = self._reader.read_csv_file(self._file_title_types)

        return self._title_types

    def type_of_rights(self):
        """
        Type of Right.

        :return: the allowed Type of Right codes.
        """
        if self._type_of_rights is None:
            self._type_of_rights = self._reader.read_csv_file(self._file_type_of_right)

        return self._type_of_rights

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

    def writer_designation_codes(self):
        """
        Writer Designation codes.

        :return: the allowed CWR Writer Designation codes
        """
        if self._writer_designation_codes is None:
            self._writer_designation_codes = self._reader.read_csv_file(self._file_writer_designation_codes)

        return self._writer_designation_codes