# -*- coding: utf-8 -*-

from config_cwr.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldTerminalRuleFactory
from data_cwr.accessor import CWRTables
from cwr.grammar.factory.decorator import RecordRuleDecorator, GroupRuleDecorator
from cwr.grammar.factory.rule import DefaultRuleFactory
from cwr.parser.decoder.dictionary import *
from cwr.grammar.factory.adapter import *

"""
Grammar utilities for the test classes.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'

_config = CWRConfiguration()

adapters = {}

adapters['alphanum'] = AlphanumAdapter()
adapters['alphanum_ext'] = ExtendedAlphanumAdapter()
adapters['numeric'] = NumericAdapter()
adapters['boolean'] = BooleanAdapter()
adapters['flag'] = FlagAdapter()
adapters['date'] = DateAdapter()
adapters['time'] = TimeAdapter()
adapters['date_time'] = DateTimeAdapter()
adapters['blank'] = BlankAdapter()
adapters['lookup'] = LookupAdapter()
adapters['iswc'] = ISWCAdapter()
adapters['ipi_name_n'] = IPINameNumberAdapter()
adapters['ipi_base_n'] = IPIBaseNumberAdapter()
adapters['percentage'] = PercentageAdapter()
adapters['ean13'] = EAN13Adapter()
adapters['isrc'] = ISRCAdapter()
adapters['visan'] = VISANAdapter()
adapters['avi'] = AudioVisualKeydapter()
adapters['charset'] = CharSetAdapter()
adapters['alphanum_variable'] = VariableAlphanumAdapter()
adapters['numeric_float'] = NumericFloatAdapter()

_data = _config.load_field_config('table')
_data.update(_config.load_field_config('common'))
_data.update(_config.load_field_config('filename'))

_factory_field = DefaultFieldTerminalRuleFactory(_data, adapters, field_values=CWRTables())
_factory_table = DefaultFieldTerminalRuleFactory(_config.load_field_config('table'), adapters, field_values=CWRTables())

_rules = _config.load_transaction_config('common')
_rules.extend(_config.load_record_config('common'))
_rules.extend(_config.load_group_config('common'))

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

decoders_group = {}

decoders_group['transmission'] = TransmissionDictionaryDecoder()
decoders_group['group_info'] = GroupDictionaryDecoder()

_decorators = {'transaction_record': RecordRuleDecorator(_factory_field, decoders),
               'record': RecordRuleDecorator(_factory_field, decoders),
               'group': GroupRuleDecorator(decoders_group)}
_group_rule_factory = DefaultRuleFactory(_rules, _factory_field, _decorators)

_group_rule_factory_filename = DefaultRuleFactory(_config.load_record_config('filename'), _factory_field)


def get_record_grammar(id):
    return _group_rule_factory.get_rule(id)


def get_filename_grammar(id):
    return _group_rule_factory_filename.get_rule(id)