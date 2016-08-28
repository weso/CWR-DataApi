# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
from abc import ABCMeta, abstractmethod

from cwr.parser.encoder.standart.field import CwrFieldEncoderFactory
from cwr.parser.encoder.dictionary import FileDictionaryEncoder, TransactionRecordDictionaryEncoder, \
    TransmissionDictionaryEncoder, GroupDictionaryEncoder, TransmissionHeaderDictionaryEncoder, \
    GroupHeaderDictionaryEncoder, GroupTrailerDictionaryEncoder, TransmissionTrailerDictionaryEncoder
from cwr.parser.encoder.common import Encoder
from cwr.record import TransactionRecord
from cwr.group import GroupHeader, GroupTrailer
from cwr.transmission import TransmissionHeader, TransmissionTrailer
import json
#from data_cwr.accessor import CWRTables

def _iso_handler(obj):
    """
    Transforms an object into it's ISO format, if possible.

    If the object can't be transformed, then an error is raised for the JSON
    parser.

    This is meant to be used on datetime instances, but will work with any
    object having a method called isoformat.

    :param obj: object to transform into it's ISO format
    :return: the ISO format of the object
    """
    if hasattr(obj, 'isoformat'):
        result = obj.isoformat()
    else:
        raise TypeError("Unserializable object {} of type {}".format(obj,
                                                                     type(obj)))

    return result

class CwrRecordEncoderException(Exception):
    pass


class CwrRecordEncoder(Encoder):
    """
    Abstract class for generate cwr string record. Uses field encoders
    """
    __metaclass__ = ABCMeta

    def __init__(self, record_configs, field_configs):
         super(CwrRecordEncoder, self).__init__()
         self._record_configs = record_configs
         self._field_encoder_factory = CwrFieldEncoderFactory(field_configs)

    @abstractmethod
    def get_record_dictionary_encoder(self, entity):
        """
        Get dictionary encoder
        """
        raise NotImplementedError('The head method must be implemented')

    def head(self, entity):
        """
        Return head of cwr string ('HDR' for example)
        """
        return entity.record_type

    @staticmethod
    def _get_best_result(possible_list):
        if len(possible_list) < 1:
            raise CwrRecordEncoderException()
        else:
            possible_list = sorted(possible_list, key=lambda item: -item['len'])
            return possible_list[0]['result']

    def build_field_encoders(self, rules, field_encoders=[[]], optional=False):
        for field in rules:
            if field.rule_type == 'field':
                for row in field_encoders:
                    encoder = self._field_encoder_factory.get_field_encoder(field[1], optional)
                    row.append(encoder)
            else:
                if field.list_type == 'optional':
                    field_encoders = self.build_field_encoders(field.rules, field_encoders=field_encoders,
                                                               optional=True)
                elif field.list_type == 'sequence':
                    field_encoders = self.build_field_encoders(field.rules, field_encoders=field_encoders,
                                                               optional=optional)
                elif field.list_type == 'option':
                    options = []
                    for row in field_encoders:
                        for option in field.rules:
                            if option.rule_type == 'field':
                                encoder = self._field_encoder_factory.get_field_encoder(option[1], optional)
                                options.append(row + [encoder])
                            else:
                                inner = self.build_field_encoders(option.rules, field_encoders=[list(row)], optional=optional)
                                for t in inner:
                                    options.append(t)
                    field_encoders = options
        return field_encoders

    def get_record_fields_encoders(self):
        field_encoders = []
        for record_config in self._record_configs:
            field_encoders += self.build_field_encoders(record_config.rules,  field_encoders=[[]],  optional=False)
        return field_encoders

    @staticmethod
    def try_encode(field_encoders, entity_dict):
        """
        Inner encoding and try return string from entity dictionary
        :param field_encoders:
        :param entity_dict:
        :return:
        """
        result = ''
        for field_encoder in field_encoders:
            try:
                result += field_encoder.encode(entity_dict)
            except KeyError as e:
                return False
        return result

    def get_entity_dict(self, entity):
        dict_encoder = self.get_record_dictionary_encoder(entity)
        return dict_encoder.encode(entity)

    def encode(self, entity):
        """
        Generate string of cwr format for all possible combinations of fields,
        accumulate and then elect the best. The best string it is who used most of all fields
        :param entity:
        :return:
        """
        possible_results = []
        entity_dict = self.get_entity_dict(entity)
        record_field_encoders = self.get_record_fields_encoders()
        for field_encoders in record_field_encoders:
            result = self.try_encode(field_encoders, entity_dict)
            if result:
                possible_results.append({'result': result, 'len': len(field_encoders)})
        cwr = self.head(entity) + self._get_best_result(possible_results) + "\r\n"
        return cwr


class TransactionCwrRecordEncoder(CwrRecordEncoder):

    def head(self, entity):
        return "{}{:0>8}{:0>8}".format(entity.record_type, entity.transaction_sequence_n, entity.record_sequence_n)

    def get_record_dictionary_encoder(self, entity):
        return TransactionRecordDictionaryEncoder()


class GroupHeaderCwrRecordEncoder(CwrRecordEncoder):

    def get_record_dictionary_encoder(self, entity):
        return GroupHeaderDictionaryEncoder()


class GroupTraileCwrRecordEncoder(CwrRecordEncoder):

    def get_record_dictionary_encoder(self, entity):
        return GroupTrailerDictionaryEncoder()

class TransmissionHeaderCwrRecordEncoder(CwrRecordEncoder):

    def get_record_dictionary_encoder(self, entity):
        return TransmissionHeaderDictionaryEncoder()

class TransmissionTrailerCwrRecordEncoder(CwrRecordEncoder):

    def get_record_dictionary_encoder(self, entity):
        return TransmissionTrailerDictionaryEncoder()


class CwrRecordEncoderFactory(object):
    """
    Factory for produce record encoders
    """

    def __init__(self, record_configs, field_configs):
        super(CwrRecordEncoderFactory, self).__init__()
        self._record_configs = self._process_record(record_configs)
        self._field_configs = field_configs

    @staticmethod
    def _process_record(rules):
        processed = {}
        for rule in rules:
            for rule_id in rule.head:
                if rule_id in processed:
                    processed[rule_id].append(rule)
                else:
                    processed[rule_id] = [rule]
        return processed

    def get_format_encoders(self, record_id):
        record_config = self._record_configs[record_id]
        templates = self.build_format_templates(record_config.rules, templates=[[]])
        return templates

    def get_encoder(self, entity):
        if entity.record_type not in self._record_configs:
            raise NameError('The record type %s not found in config %s' % entity.record_type)
        record_configs = self._record_configs[entity.record_type]
        if isinstance(entity, TransactionRecord):
            return TransactionCwrRecordEncoder(record_configs, self._field_configs)
        elif isinstance(entity, TransmissionHeader):
            return TransmissionHeaderCwrRecordEncoder(record_configs, self._field_configs)
        elif isinstance(entity, GroupHeader):
            return GroupHeaderCwrRecordEncoder(record_configs, self._field_configs)
        elif isinstance(entity, GroupTrailer):
            return GroupTraileCwrRecordEncoder(record_configs, self._field_configs)
        elif isinstance(entity, TransmissionTrailer):
            return TransmissionTrailerCwrRecordEncoder(record_configs, self._field_configs)
        else:
            raise NameError('The encoder not found for entity %s' % entity.__class__.__name__)
        return encoder
