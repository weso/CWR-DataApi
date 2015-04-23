# -*- coding: utf-8 -*-

from abc import abstractmethod

import pyparsing as pp

from cwr.grammar.field import record as field_record
from cwr.parser.dictionary import *
from cwr.grammar.factory.rule import RuleDecorator


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class RecordFactory(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def get_record(self, id):
        raise NotImplementedError("The get_record method is not implemented")


class RecordRuleDecorator(RuleDecorator):
    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, factory):
        super(RecordRuleDecorator, self).__init__()
        self._factory = factory

        self._decoders = {}
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

    def decorate(self, rule, data):
        sequence = []

        id = data['id']

        sequence.append(self._lineStart)

        prefix = self._get_prefix(data)

        if prefix is not None:
            sequence.append(prefix)

        sequence.append(rule)

        sequence.append(self._lineEnd)

        record = pp.And(sequence)

        if id in self._decoders:
            decoder = self._decoders[id]
            record.setParseAction(lambda p: decoder.decode(p))

        return record.setResultsName(id)

    def _get_prefix(self, config):
        rule_type = config['rule_type']

        if rule_type == 'transaction':
            header = field_record.record_prefix(config['record_type'], self._factory)
        elif rule_type == 'record':
            header = field_record.record_type(config['record_type'])
        else:
            header = None

        return header


class GroupRuleDecorator(RuleDecorator):
    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self):
        super(GroupRuleDecorator, self).__init__()

        self._decoders = {}
        # TODO: Do this somewhere else
        self._decoders['transmission'] = TransmissionDictionaryDecoder()
        self._decoders['group_info'] = GroupDictionaryDecoder()

    def decorate(self, rule, data):
        id = data['id']

        record = rule

        if id in self._decoders:
            decoder = self._decoders[id]
            record.setParseAction(lambda p: decoder.decode(p))

        return record.setResultsName(id)
