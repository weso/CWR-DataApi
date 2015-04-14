# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod
import logging

import pyparsing as pp

from cwr.grammar.field import record as field_record
from cwr.parser.dictionary import *
from cwr.grammar.factory.rule import RuleFactory, DefaultGroupRuleFactory


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class DefaultPrefixBuilder(object):
    def __init__(self, config):
        self._config = config

    def get_prefix(self, id, factory):

        if id in self._config:
            config = self._config[id]

            if config['header_type'] == 'transaction':
                header = field_record.record_prefix(self._config[id]['record_type'], factory)
            elif config['header_type'] == 'record':
                header = field_record.record_type(self._config[id]['record_type'])
            else:
                header = None
        else:
            header = None

        return header


class RecordFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_record(self, id):
        raise NotImplementedError("The get_record method is not implemented")


class DefaultRecordFactory(RecordFactory, RuleFactory):
    """
    Factory for acquiring record rules.
    """

    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, record_configs, prefixer, field_factory):
        super(DefaultRecordFactory, self).__init__()
        # records already created
        self._records = {}
        # Logger
        self._logger = logging.getLogger(__name__)
        # Configuration for creating the record
        self._record_configs = record_configs
        # Fields factory
        self._field_factory = field_factory
        # Prefix builder
        self._prefixer = prefixer
        # Dictionary decoders
        self._decoders = {}

        factories = {'field': self}
        # TODO: This should not be stored inside this factory
        self._group_rule_factory = DefaultGroupRuleFactory(factories)

        # TODO: Do this somewhere else
        self._decoders['acknowledgement'] = AcknowledgementDictionaryDecoder()
        self._decoders['message'] = MessageDictionaryDecoder()
        self._decoders['agreement'] = AgreementDictionaryDecoder()
        self._decoders['territory_in_agreement'] = AgreementTerritoryDictionaryDecoder()
        self._decoders['additional_related_information'] = AdditionalRelatedInformationDictionaryDecoder()
        self._decoders['group_header'] = GroupHeaderDictionaryDecoder()
        self._decoders['group_trailer'] = GroupTrailerDictionaryDecoder()
        self._decoders['interested_party_agreement'] = InterestedPartyForAgreementDictionaryDecoder()
        self._decoders['nra_agreement_party'] = NonRomanAlphabetAgreementPartyDictionaryDecoder()
        self._decoders['nra_publisher_name'] = NonRomanAlphabetPublisherNameDictionaryDecoder()
        self._decoders['nra_writer_name'] = NonRomanAlphabetWriterNameDictionaryDecoder()
        self._decoders['nra_title'] = NonRomanAlphabetTitleDictionaryDecoder()
        self._decoders['nra_performance_data'] = NonRomanAlphabetPerformanceDataDictionaryDecoder()
        self._decoders['nra_work'] = NonRomanAlphabetWorkDictionaryDecoder()
        self._decoders['nra_other_writer'] = NonRomanAlphabetOtherWriterDictionaryDecoder()
        self._decoders['publisher'] = PublisherRecordDictionaryDecoder()
        self._decoders['publisher_territory'] = IPTerritoryOfControlDictionaryDecoder()
        self._decoders['transmission_header'] = TransmissionHeaderDictionaryDecoder()
        self._decoders['transmission_trailer'] = TransmissionTrailerDictionaryDecoder()
        self._decoders['work'] = WorkDictionaryDecoder()
        self._decoders['work_conflict'] = WorkDictionaryDecoder()
        self._decoders['work_alternate_title'] = AlternateTitleDictionaryDecoder()
        self._decoders['entire_work_title'] = AuthoredWorkDictionaryDecoder()
        self._decoders['original_work_title'] = AuthoredWorkDictionaryDecoder()
        self._decoders['performing_artist'] = PerformingArtistDictionaryDecoder()
        self._decoders['recording_detail'] = RecordingDetailDictionaryDecoder()
        self._decoders['work_origin'] = WorkOriginDictionaryDecoder()
        self._decoders['instrumentation_summary'] = InstrumentationSummaryDictionaryDecoder()
        self._decoders['instrumentation_detail'] = InstrumentationDetailDictionaryDecoder()
        self._decoders['component'] = ComponentDictionaryDecoder()
        self._decoders['writer'] = WriterRecordDictionaryDecoder()
        self._decoders['writer_publisher'] = PublisherForWriterDictionaryDecoder()
        self._decoders['writer_territory'] = IPTerritoryOfControlDictionaryDecoder()
        self._decoders['filename_new'] = FileTagDictionaryDecoder()
        self._decoders['filename_old'] = FileTagDictionaryDecoder()

    def get_record(self, id):

        record = self._build_record(id)

        prefix = self._prefixer.get_prefix(id, self._field_factory)

        if prefix is not None:
            record = prefix + record

        record = self._lineStart + \
                 record + \
                 self._lineEnd

        if id in self._decoders:
            decoder = self._decoders[id]
            record.setParseAction(lambda p: decoder.decode(p))

        return record.setResultsName(id)

    def get_rule(self, id, modifiers):
        compulsory = 'compulsory' in modifiers

        return self._field_factory.get_field(id, compulsory=compulsory)

    def _build_record(self, id):
        record_config = self._record_configs[id]

        return self._group_rule_factory.get_rule_group(record_config)