# -*- coding: utf-8 -*-

from abc import ABCMeta
import logging

import pyparsing as pp

from cwr.grammar.field import record as field_record
from cwr.parser.dictionary import *


"""
Record fields factories.
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__status__ = 'Development'

"""
Configuration classes.
"""


class PrefixBuilder(object):
    def __init__(self, config):
        self._config = config

    def get_prefix(self, id, factory):

        config = self._config[id]

        if config['header_type'] == 'transaction':
            header = field_record.record_prefix(self._config[id]['record_type'], factory)
        elif config['header_type'] == 'record':
            header = field_record.record_type(self._config[id]['record_type'])
        else:
            header = None

        return header


class RecordFactory(object):
    """
    Factory for acquiring record rules.
    """
    __metaclass__ = ABCMeta

    _lineStart = pp.lineStart.suppress()
    _lineStart.setName("Start of line")

    _lineEnd = pp.lineEnd.suppress()
    _lineEnd.setName("End of line")

    def __init__(self, record_configs, prefixer, field_factory):
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

    def _build_record(self, id):
        field_config = self._record_configs[id]

        record = None

        for group in field_config:
            if group['group_type'] == 'sequence':
                for field in group['fields']:
                    if 'compulsory' in field:
                        compulsory = field['compulsory']
                    else:
                        compulsory = False

                    field = self._field_factory.get_field(field['name'], compulsory=compulsory)

                    if record is None:
                        record = field
                    else:
                        record += field

        return record