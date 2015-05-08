# -*- coding: utf-8 -*-

from data_commonworks.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldTerminalRuleFactory
from data_commonworks.accessor import CWRTables
from cwr.grammar.factory.decorator import RecordRuleDecorator, GroupRuleDecorator
from cwr.grammar.factory.rule import DefaultRuleFactory
from cwr.parser.decoder.dictionary import *

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_config = CWRConfiguration()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))
_data.update(_config.load_field_config('filename'))

_factory_field = DefaultFieldTerminalRuleFactory(_data, CWRTables())

_rules = _config.load_transaction_config('common')
_rules.update(_config.load_record_config('common'))
_rules.update(_config.load_group_config('common'))

decoders = {}

decoders['acknowledgement'] = AcknowledgementDictionaryDecoder()
decoders['message'] = MessageDictionaryDecoder()
decoders['agreement'] = AgreementDictionaryDecoder()
decoders['territory_in_agreement'] = AgreementTerritoryDictionaryDecoder()
decoders['additional_related_information'] = AdditionalRelatedInformationDictionaryDecoder()
decoders['group_header'] = GroupHeaderDictionaryDecoder()
decoders['group_trailer'] = GroupTrailerDictionaryDecoder()
decoders['interested_party_agreement'] = InterestedPartyForAgreementDictionaryDecoder()
decoders['nra_agreement_party'] = NonRomanAlphabetAgreementPartyDictionaryDecoder()
decoders['nra_publisher_name'] = NonRomanAlphabetPublisherNameDictionaryDecoder()
decoders['nra_writer_name'] = NonRomanAlphabetWriterNameDictionaryDecoder()
decoders['nra_title'] = NonRomanAlphabetTitleDictionaryDecoder()
decoders['nra_performance_data'] = NonRomanAlphabetPerformanceDataDictionaryDecoder()
decoders['nra_work'] = NonRomanAlphabetWorkDictionaryDecoder()
decoders['nra_other_writer'] = NonRomanAlphabetOtherWriterDictionaryDecoder()
decoders['publisher'] = PublisherRecordDictionaryDecoder()
decoders['publisher_territory'] = IPTerritoryOfControlDictionaryDecoder()
decoders['transmission_header'] = TransmissionHeaderDictionaryDecoder()
decoders['transmission_trailer'] = TransmissionTrailerDictionaryDecoder()
decoders['work'] = WorkDictionaryDecoder()
decoders['work_conflict'] = WorkDictionaryDecoder()
decoders['work_alternate_title'] = AlternateTitleDictionaryDecoder()
decoders['entire_work_title'] = AuthoredWorkDictionaryDecoder()
decoders['original_work_title'] = AuthoredWorkDictionaryDecoder()
decoders['performing_artist'] = PerformingArtistDictionaryDecoder()
decoders['recording_detail'] = RecordingDetailDictionaryDecoder()
decoders['work_origin'] = WorkOriginDictionaryDecoder()
decoders['instrumentation_summary'] = InstrumentationSummaryDictionaryDecoder()
decoders['instrumentation_detail'] = InstrumentationDetailDictionaryDecoder()
decoders['component'] = ComponentDictionaryDecoder()
decoders['writer'] = WriterRecordDictionaryDecoder()
decoders['writer_publisher'] = PublisherForWriterDictionaryDecoder()
decoders['writer_territory'] = IPTerritoryOfControlDictionaryDecoder()
decoders['filename_new'] = FileTagDictionaryDecoder()
decoders['filename_old'] = FileTagDictionaryDecoder()

_decorators = {'transaction': RecordRuleDecorator(_factory_field, decoders),
               'record': RecordRuleDecorator(_factory_field, decoders),
               'group': GroupRuleDecorator()}
_group_rule_factory = DefaultRuleFactory(_rules, _factory_field, _decorators)

_group_rule_factory_filename = DefaultRuleFactory(_config.load_record_config('filename'), _factory_field)


def getRecordGrammar(id):
    return _group_rule_factory.get_rule(id)


def getFilenameGrammar(id):
    return _group_rule_factory_filename.get_rule(id)